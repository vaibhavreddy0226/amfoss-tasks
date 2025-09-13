# 🎮 TimeTickQuiz  

Welcome to **TimeTickQuiz** – Task-05 of my **amfoss-tasks** repo!  
This is a **CLI-based quiz game** built as a magical adventure inside the **TimeTick Library ⏳📚**.  

It uses the **Open Trivia API** to bring you timed multiple-choice quizzes with dynamic categories and difficulty levels.  
I optimized the code, fixed profile saving, ensured correct scoring, and added colorful output to make the game more engaging! ✨  

---

## 📖 Overview  

This project fulfills the **TimeTickQuiz** requirements by:  

- 👤 **User Profiles** → Stored in `profiles.json` with username, score, high score & difficulty.  
- 🌐 **API Integration** → Fetching multiple-choice questions from the Open Trivia API.  
- ⏱ **Timer per Question** → Implemented with `threading.Timer`.  
- 🎨 **Rich Console Output** → Using the `rich` library for colored text & tables.  
- 🧩 **Difficulty Auto-Adjusts** →  
  - Easy: ≤ 20  
  - Medium: > 20  
  - Hard: > 50  
- ⚡ **Optimized Code** → Reduced 148 lines → 119 lines (~19.6% shorter).  
- 🛠 **Bug Fixes** → Fixed `profiles.json` saving, correct session scoring, cleaner console logs.  

---

## 🛠 Setup & Installation  

First, clone the repo and move into **Task-05 folder**:  

```bash
git clone https://github.com/<your-username>/amfoss-tasks.git
cd amfoss-tasks/task-05
````

Now set up a virtual environment 🔮:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies 📦:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Move into the `src/` folder and run the game:

```bash
cd src
python3 main.py
```

When you run it:

1. Enter your **username**.
2. Select the **number of questions (1–20)**.
3. Choose a **time limit (10–30 seconds)**.
4. Pick a **category** (shown in a rich table).
5. Select **difficulty** (or let it adjust automatically).

Your progress will be stored in `profiles.json` and high scores will only update if you beat your previous best! 🏆

---

## ✅ Task Completion

* **User Profiles** → Implemented in `user_profile.py`. Handles username, score, high score, and difficulty.
* **API Integration** → `quiz_engine.py` fetches questions based on user’s choice.
* **User Inputs** → `main.py` asks for username, question count, time limit, category, and difficulty.
* **Timer** → `threading.Timer` ensures each question has a limit.
* **Rich Output** → Blue questions, ✅ green for correct, ❌ red for wrong, and tables for results.


---

## 📂 File Structure

```
task-05/
│── src/
│   ├── main.py          # Launches the quiz, handles inputs
│   ├── quiz_engine.py   # Fetches questions, runs quiz & timer
│   ├── user_profile.py  # Manages profiles and scoring
│   └── utils.py         # Profile I/O and category fetching
│
│── profiles.json        # Stores user data
│── requirements.txt     # Dependencies: requests, rich
│── README.md            # You’re reading it right now 😄
```

---

## 🐛 Challenges & Solutions

* ⚠️ **ModuleNotFoundError** → Fixed by adding `requests` & `rich` to `requirements.txt`.
* ⚠️ **profiles.json not updating** → Solved with absolute paths & permissions (`chmod 666 profiles.json`).
* ⚠️ **Incorrect scoring** → Fixed session reset + proper high score updates.
* ⚠️ **Console clutter** → Removed debug messages.
* ⚠️ **Task misalignment** → Updated to support user-selected categories, time, difficulty, and auto-adjusting difficulty levels.

---

## 🚀 Final Words

This was one of the most fun tasks – a mix of coding, problem-solving, and **bringing magic to the terminal** 🪄💻.
You can find the code inside the **`task-05`** folder of this repo.

Enjoy the game and try beating your own high score 🏅🔥!

