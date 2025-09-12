import sys, os
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMovie
from dashboard import Dashboard

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 Loading CineScope...")
        self.resize(800, 500)
        self.bg_label = QLabel(self)
        self.bg_label.setScaledContents(True)
        self.movie = QMovie(os.path.join(os.path.dirname(__file__), "assets", "background.gif"))
        self.bg_label.setMovie(self.movie)
        self.movie.start()
        QTimer.singleShot(4000, self.show_dashboard)

    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def show_dashboard(self):
        self.movie.stop()
        self.close()
        self.dashboard = Dashboard()
        self.dashboard.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec())
