# 🎨 Draw a Perfect Circle!  

Welcome to **Draw a Perfect Circle** – Task-03 of my **amfoss-tasks** repo!  
Inspired by Neal Wu’s legendary **neal.fun/perfect-circle**, this project challenges you to draw the most accurate circle possible 🟢.  

You get **5 seconds** ⏳ to draw a circle around a fixed **red dot** 🎯.  
Your accuracy is calculated using a strict **maximum deviation + circularity-based formula**, so **wavy or sloppy circles get punished** (70–80% accuracy), while near-perfect ones hit **95%+**.  

I also added **dark/light mode 🌙☀️**, **mode selection (Easy/Medium/Hardcore)** and **session storage for best scores**.  

---

## 📖 Overview  

This project provides an **interactive circle-drawing game** with:  

- 🖌 **Canvas Drawing** → Freehand drawing on an HTML5 canvas.  
- 🎯 **Red Center Dot** → Fixed at center, size varies by mode:  
  - Easy: 10px  
  - Medium: 5px  
  - Hardcore: 3px  
- 📏 **Stricter Accuracy** → Maximum deviation + radius variance used to penalize bends.  
- 💾 **Session Storage** → Tracks best score across attempts.  
- 🎛 **Modes & Toggles** → Mode selector, reset button, dark/light mode toggle.  
- ⏱ **Timer** → 5-second countdown with bonus scoring if completed faster.  

---

## ✅ Task Requirements Fulfilled  

- **Canvas Drawing**: HTML5 Canvas API (`arc`, `lineTo`, `clearRect`) for drawing red center dot & user path.  
- **Mouse Events**: `mousedown`, `mousemove`, `mouseup` for freehand circle drawing.  
- **Geometric Accuracy**:  
  - Maximum deviation from initial radius.  
  - Variance penalty for uneven bends.  
  - Ray-casting to check if the red dot is inside.  
- **Session Storage**: Stores best score (`sessionStorage`) → shown in the status area.  
- **Scoring Feedback**:  
  - Easy: +8% accuracy bonus.  
  - Medium: Standard scoring.  
  - Hardcore: -12% penalty, tiny dot, no real-time feedback.  
  - Time Bonus: +5% if completed in ≤ 3 seconds.  
- **Error Handling**:  
  - ❌ “The red dot is not inside your circle!”  
  - ⏳ “Time’s up! Draw a proper circle!”  

---

## 🛠 Setup & How to Run  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/<your-username>/amfoss-tasks.git
   cd amfoss-tasks/task-03
   ```

2. **Open in Browser**:
   Simply open `index.html` in any modern browser (Chrome/Firefox/Edge).
   No backend or installation required ✅

3. **Play the Game**:

   * Click **Start/Reset**.
   * Draw a circle around the **red dot** within **5 seconds**.
   * Check your score and try to beat your **best accuracy** 🔥

---

## 📂 File Structure

```
task-03/
│── index.html    # Game layout with canvas, mode selector, buttons, audio
│── styles.css    # Dark/Light mode styles, layout adjustments
│── script.js     # Circle-drawing logic, accuracy checks, timer, sound
```

---

## 🐛 Challenges & Solutions

* 🎯 **Accuracy Precision** → Used max deviation + variance penalty to punish wavy circles (\~70–80%). Perfect ones land \~95%+.
* 🟥 **Center Point Check** → Ray-casting algorithm ensures the circle actually **encloses the dot**.
* ⏱ **Timer Logic** → Implemented a strict **5s countdown**, resetting properly between attempts.
* 🌗 **UI Polish** → Added **dark/light toggle** and mode selector for flexible gameplay.
