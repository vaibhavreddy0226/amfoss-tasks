# 🎬 CineScope Dashboard  

Welcome to **Task-04** of my **amfoss-tasks** repo – **CineScope Dashboard**.  
This project is an **interactive movie database visualizer** built with **MySQL + PySide6**. It lets you search, filter, and explore movie data from a CSV file, with a clean GUI and export feature.  

---

## 📖 Overview  

This task was all about combining **databases with UI**. I achieved this by:  
- Creating a **MySQL database** and importing data from `movies.csv`.  
- Building a **PySide6-based dashboard** for searching and filtering movies.  
- Adding an **Export to CSV** feature for saving filtered results.  
- Improving the UI with a **splash screen** and responsive design.  
- Writing **optimized, maintainable Python code**.  

✨ End result: A **user-friendly app** to explore movies by director, actor, year, or genre with smooth performance.  

---

## 🛠 Setup and Installation  

Follow these steps to set up and run the project:  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/<your-username>/amfoss-tasks.git
   cd amfoss-tasks/task-04
   ```

2. **Create Virtual Environment** 🌐

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies** 📦

   ```bash
   pip install PySide6 mysql-connector-python
   ```

4. **Setup MySQL Database** 🗄

   * Ensure MySQL is running with user: `vaibhav`, password: `vaibhav`.
   * Run the scripts:

     ```bash
     python3 create_table.py
     python3 import_csv.py
     ```

5. **Run the App** 🚀

   ```bash
   python3 main.py
   ```

---

## ✅ Task Completion

### 1. Import Data into MySQL 📥

* **Scripts**: `create_table.py`, `import_csv.py`
* Created `movies_db` database and `movies` table.
* Inserted CSV data into MySQL with type conversions (`int`, `float`).
* Centralized DB logic in `db_utils.py` for reusability.

### 2. Connect UI to Database 🔗

* **Script**: `dashboard.py`
* Built dynamic SQL queries for searching by **director, actor, year, and genre**.
* Populated genre dropdown dynamically using SQL.
* Displayed results in a **responsive QTableWidget**.

### 3. Export to CSV 📤

* Added button to export filtered results to `exported_results.csv`.
* Included search context (filters, columns).
* Supported multiple exports in one file (append mode).

### 4. Improve the UI 🎨

* Added **splash screen** with `background.gif`.
* Used **QHeaderView\.Stretch** for responsive columns.
* Added **status messages** with emojis (✅ success, ⚠️ errors).

---

## 📂 File Structure

```
task-04/
│── assets/
│   └── background.gif       # Splash screen animation
│── movies.csv               # Movie dataset
│── db_utils.py              # Centralized DB connection (6 lines)
│── create_table.py          # Create database & movies table
│── import_csv.py            # Import movies.csv into DB
│── dashboard.py             # Main dashboard logic (UI + DB)
│── main.py                  # Entry point (splash + dashboard)
```

---

## 💻 Usage

1. Search movies by **director, actor, year, or keyword**.
2. Filter movies by **genre** from the dropdown.
3. Select/deselect **columns** to display in results.
4. Export filtered data using the **Export CSV** button.

---

## 🐛 Challenges & Fixes

* **ModuleNotFoundError (PySide6)** → Installed missing dependency.
* **TypeError in QHeaderView** → Fixed with `QHeaderView.Stretch`.
* **Redundant DB logic** → Centralized into `db_utils.py`.
* **UI scaling issues** → Fixed with responsive layouts and GIF scaling.

---

## 🌟 Enhancements

* ✅ Splash screen for polished UX.
* ✅ Cleaner, maintainable, and shorter code.
* ✅ Export feature for analysis/sharing.

---

## 📜 Submission Files

  * `db_utils.py`
  * `create_table.py`
  * `import_csv.py`
  * `main.py`
  * `dashboard.py`
  * `movies.csv`
  * `assets/background.gif`

