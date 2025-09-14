# ⚔️ BattleCraft — CSS Master Trials 

This folder contains my **CSSBattle** recreations for **Task-08** of the `amfoss-tasks` repo — a hands-on set of pixel-art puzzles where you recreate target images using **pure HTML & CSS**.
I attempted **15** daily challenges and completed **7/15** so far. Each battle lives in its own folder: `battle-01`, `battle-02`, … `battle-15`.
Open the folders `battle-01` → `battle-07` to see the code & screenshots for the ones I finished.

---

## ✅ Status — Progress

* **Completed:** 7 / 15
  `battle-01/` `battle-02/` `battle-03/` `battle-04/` `battle-05/` `battle-06/` `battle-07/`
* **Remaining:** 8 / 15
  `battle-08/` … `battle-15/` (will complete next)

Each completed folder contains:

* `index.html` — the solution (pure HTML + CSS)
* `screenshot.png` — the rendered result for quick review

---

## 🧭 How to view a solution

Open any battle folder and do as following:

* double-click

  * Open `index.html` directly in your browser.


---

## 🛠 Techniques I used 

I focused on minimal, readable solutions while trying to match the target as close as possible:

* **`box-shadow` cloning** — duplicate a single block many times.
* **Pseudo elements** (`::before`, `::after`) — add extra shapes without extra markup.
* **`border` / `outline` tricks** — create hollow squares and frames.
* **`transform` / `translate`** — precise placement with fewer values.
* **`repeating-linear-gradient` & gradients** — patterns, stripes, and fills.
* **CSS variables & `calc()`** — make offsets easy to tweak.
* **`clip-path`** (only when necessary) — for non-rectangular cuts.
* **Flexbox / Grid** (very lightly) — centering or baseline alignment where useful.
* **Single-div solutions** where possible (box-shadow + pseudo elements) — compact and elegant.

---

## ✏️ How I approached each battle

1. Inspect the target and block-out a pixel grid mentally.
2. Decide whether a **box-shadow** clone or **pseudo-element** strategy fits best.
3. Build a single base block (the repeated pixel), then copy with shadows or offsets.
4. Iterate on offsets & sizes until alignment is tight.
5. Keep trimming CSS — remove redundant properties and merge shadows to reduce code size.

---

## ⚠️ Challenges & learnings

* Pixel-perfect alignment is fiddly — small offsets change the whole look.
* `box-shadow` is powerful but gets messy if you overuse it — group shadows logically.
* Some targets are simpler using two elements (e.g., a frame + inner accent), while others can be done with one clever `div`.

---

## 📁 File structure

```
task-08/
├─ battle-01/
│  ├─ index.html
│  └─ screenshot.png
├─ battle-02/
│  └─ ...

```

---

## 🎯 Goals / Next steps

* Finish the remaining **8 battles** and push them as `battle-08` → `battle-15`.

