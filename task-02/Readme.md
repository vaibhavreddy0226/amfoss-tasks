# 🏆 HackerRank Contest 

This folder contains my solutions for **Task 2** of the amFOSS tasks, which was a HackerRank contest consisting of 5 questions.  
Out of these, I solved **2 questions** successfully using **Python 🐍**.  

---

## 📌 Problems I Solved  

### 1️⃣ Race 10  
**Problem Summary:**  
Alice is standing at point `a`, and there are two prize locations `x` and `y`. Bob can start at any other point except `a`. We need to check if Bob can reach **both prize locations strictly faster** than Alice. If yes, print `"YES"`, otherwise `"NO"`.

**My Approach 🧠:**  
- First, I noticed that Bob only has a chance if Alice is **between** the two prize points.  
- If Alice is outside the interval formed by `x` and `y`, then Bob can always find a point on the other side and reach earlier.  
- But if Alice is **inside** that interval, then no matter where Bob stands, Alice will always be closer to at least one prize.  

So the check reduces to:  
- If `a <= x or a >= y` → Bob can win (`YES`).  
- Else → Bob cannot (`NO`).  


**Concepts Used:**

* Interval checking 📏
* Simple conditionals and swapping values
* Logic simplification (converted problem to range inclusion/exclusion check)

---

### 2️⃣ Count '1'

**Problem Summary:**
We start with a binary string of length `n`. For each position `i`, we flip the character at index `i` (1 → 0 or 0 → 1). After flipping, we count the total number of `1`s across all these new strings.

**My Approach 🧠:**

* First, I counted how many `1`s are already present (`ones_in_original`).
* Then, for every position `i` in the string:

  * If the character is `1`: flipping it reduces the count of `1`s by 1.
  * If the character is `0`: flipping it increases the count of `1`s by 1.
* Accumulate the results for all positions → final answer.

This avoided generating all strings explicitly (which would be inefficient).

**Concepts Used:**

* String traversal & `.count()` method
* Smart counting instead of brute force
* Flipping logic (thinking in terms of impact on total count instead of actually building strings)

---

👉 The codes are available inside the [task-02](task-02) folder of this repository.  

You can check my HackerRank status — my username is `U4AID24027`.

---

## ⚙️ Tools & Language

* Language: **Python 3** 🐍
* Platform: **HackerRank Contest** 💻

---


✨ That’s how I solved 2/5 questions in the HackerRank contest!
