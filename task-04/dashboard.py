import csv
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QCheckBox, QLabel, QComboBox, QHeaderView
from PySide6.QtGui import QFont
from db_utils import get_db_connection

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 Movie Dashboard")
        self.resize(1100, 600)
        layout = QVBoxLayout(self)

        title = QLabel("🎬 Movie Database Explorer")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)

        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit(placeholderText="Search by Director, Actor, or Year...")
        search_layout.addWidget(self.search_bar)

        self.genre_dropdown = QComboBox()
        self.genre_dropdown.addItem("All Genres")
        self.load_genres()
        search_layout.addWidget(self.genre_dropdown)

        self.search_btn = QPushButton("🔍 Search")
        self.search_btn.clicked.connect(self.execute_search)
        search_layout.addWidget(self.search_btn)
        layout.addLayout(search_layout)

        self.columns = ["Series_Title", "Released_Year", "Genre", "IMDB_Rating", "Director", "Star1", "Star2", "Star3"]
        col_layout = QHBoxLayout()
        self.column_checkboxes = {col: QCheckBox(col.replace("_", " ")) for col in self.columns}
        for cb in self.column_checkboxes.values():
            cb.setChecked(True)
            col_layout.addWidget(cb)
        layout.addLayout(col_layout)

        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        bottom_layout = QHBoxLayout()
        self.export_btn = QPushButton("⬇️ Export CSV")
        self.export_btn.clicked.connect(self.export_csv)
        bottom_layout.addWidget(self.export_btn)
        self.status = QLabel("")
        bottom_layout.addWidget(self.status)
        layout.addLayout(bottom_layout)
        self.last_conditions = ""

    def load_genres(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Genre FROM movies ORDER BY Genre")
        for genre in cursor.fetchall():
            if genre[0]:
                self.genre_dropdown.addItem(genre[0])
        conn.close()

    def execute_search(self):
        query_text = self.search_bar.text().strip()
        selected_cols = [col for col, cb in self.column_checkboxes.items() if cb.isChecked()]
        if not selected_cols:
            self.status.setText("⚠️ Please select at least one column.")
            return

        sql = f"SELECT {', '.join(selected_cols)} FROM movies WHERE 1=1"
        params = []
        if self.genre_dropdown.currentText() != "All Genres":
            sql += " AND Genre = %s"
            params.append(self.genre_dropdown.currentText())
        if query_text:
            sql += " AND (Director LIKE %s OR Star1 LIKE %s OR Star2 LIKE %s OR Star3 LIKE %s OR Released_Year = %s)"
            params.extend([f"%{query_text}%"]*4 + [query_text])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params)
        results = cursor.fetchall()
        self.table.setRowCount(len(results))
        self.table.setColumnCount(len(selected_cols))
        self.table.setHorizontalHeaderLabels(selected_cols)

        for row_idx, row in enumerate(results):
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.last_conditions = f"Genre={self.genre_dropdown.currentText()}, Search={query_text}, Columns={', '.join(selected_cols)}"
        self.status.setText(f"✅ {len(results)} results found.")
        conn.close()

    def export_csv(self):
        with open("exported_results.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([f"Search Conditions: {self.last_conditions}"])
            writer.writerow([self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())])
            for row in range(self.table.rowCount()):
                writer.writerow([self.table.item(row, col).text() if self.table.item(row, col) else "" for col in range(self.table.columnCount())])
            writer.writerow([])
        self.status.setText("✅ Exported to exported_results.csv")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dashboard()
    win.show()
    sys.exit(app.exec())