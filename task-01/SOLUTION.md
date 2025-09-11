## ⚡ Pre-Setup (Before the magic begins)  

Before starting, I had to prep my system with a few essentials:  

- Install **Git** 🌀  
- Install **GitHub CLI (`gh`)**  
- Install **Python3** 🐍  
- Link my global GitHub username + email (important because the spell files only run properly if linked!)  

---

## 🧩 Task Structure  

- The folder has **8 mini directories** named `01` to `08`  
- Each directory contains **5 text files**: `Spell_01.txt` → `Spell_05.txt`  
- There’s a **Spellbook** 📖 subdirectory, which holds the actual Python spell files.  
- The **4 parts of the secret code** are hidden across these files & branches.  

👉 Once I located the correct spell file, I copied it into the **Spellbook** and ran it with:  

```bash
python3 Spell_XY.txt
````

That gave me one part of the secret code. All parts went into the **codes** folder along with a `Part_x.txt` file for each stage.

---

## 🚀 How the Adventure Unfolded

### 1️⃣ Enter the Maze

* Cloned the repo using:

  ```bash
  git clone https://github.com/KshitijThareja/TheCommandLineCup.git
  ```
* Created a new `codes` directory to store all my progress.
* Rule: push after every challenge ⚔️

---

### 2️⃣ First Challenge — The Blast-Ended Skrewt 🦂🔥

* Located the right spell by solving:

  * Directory = first perfect number
  * File = differentiation of `(x² - 7x)` w\.r.t `x`
* Found the file → copied to **Spellbook** → executed with Python3 → got secret code ✨

---

### 3️⃣ Second Challenge — The Giant Spider 🕷️

* Solved with chemistry 🧪:

  * Used the atomic number of the element first used in semiconductors
  * Extracted digits → figured out directory & file
* Ran it, got the next code 🗝️
* Learned to explore remote branches with:

  ```bash
  git branch -a
  git checkout <branch_name>
  ```

---

### 4️⃣ Third Challenge — The Sphinx 🦁❓

* Switched to a branch named after Professor Lupin’s subject
* Solved the riddle → answer was a shape-shifting creature 🪄
* Googled the counter-spell → found the Python file with that name
* Imported the file into main branch using:

  ```bash
  git checkout <remote-branch> <relative-path>
  ```
* Ran it to unlock the next part of the code ✅

---

### 5️⃣ Fourth Challenge — The Graveyard ⚰️⚡

* Faced **Lord Voldemort** himself 😈
* The spell was hidden in the **commit logs**
* Used:

  ```bash
  git log
  ```
* Extracted the right commit → spell revealed → executed it 🪄

---

### 6️⃣ The Endgame 🎉

* Collected all 4 parts of the code in `codes/` folder as `Part_1.txt ... Part_4.txt`
* Concatenated them into `finalcode.txt` 💎
* Deleted extra files, leaving only the final code.
* Decoded the **base64 secret** with:

  ```bash
  echo <base64string> | base64 --decode
  ```
* And BOOM 💥 the ultimate secret was revealed.

---

## 🛠️ Commands I Used

Here’s my spell arsenal 🪄:

* `ls` → list files
* `mkdir` → make directories
* `touch` → create empty files
* `nano` → edit files
* `cat` → view contents
* `python3 filename.txt` → run spell files
* `git checkout branchname` → switch branches
* `git checkout <branch> <path>` → copy files across branches
* `git log` → view commit logs
* and many more tiny tricks… ⚔️

Commands to push my work🫸:

* `git add .` → tells Git “Hey, include all my changes in the next snapshot.” 
* `git commit -m "message"` → creates a snapshot of your changes and attaches a description so you remember what you did. 
* `git push` → sends your committed changes up to the GitHub repository, making them visible online. 

---

## 🌟 Final Thoughts

The **Terminal Wizard** was a magical start to my `amfoss-tasks` repo. ✨
It mixed Linux commands, Git, riddles, maths, and even a bit of Harry Potter lore into one adventure.

This folder stands as my **wizard’s diary** 🧙 for Task 1, documenting every spell I cast on my terminal journey. 
