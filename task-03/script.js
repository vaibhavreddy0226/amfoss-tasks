const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

const center = { x: canvas.width / 2, y: canvas.height / 2 };

let isDrawing = false;
let points = [];
let timer = null;
let timeLeft = 5;
let timeout = false;
let targetRadius = 0;

function resetGame() {
  points = [];
  isDrawing = false;
  timeout = false;
  clearInterval(timer);
  timeLeft = 5;
  targetRadius = 0;
  document.getElementById("status").textContent = "Click to start drawing! Accuracy: --%";
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawCenterPoint();
}

function drawCenterPoint() {
  ctx.fillStyle = "#ffcc5c";
  ctx.beginPath();
  ctx.arc(center.x, center.y, 5, 0, 2 * Math.PI);
  ctx.fill();
}

function startTimer() {
  clearInterval(timer);
  timeLeft = 5;

  timer = setInterval(() => {
    timeLeft--;
    if (timeLeft <= 0 && !isDrawing) {
      clearInterval(timer);
      timeout = true;
      showResult("Time's up!");
    }
    updateAccuracy();
  }, 1000);
}

function calculateAccuracy() {
  if (points.length < 2 || targetRadius === 0) return 0;

  let totalError = 0;
  for (let pt of points) {
    const dx = pt.x - center.x;
    const dy = pt.y - center.y;
    const dist = Math.sqrt(dx * dx + dy * dy);
    totalError += Math.abs(dist - targetRadius);
  }
  const avgError = totalError / points.length;
  return Math.max(0, (1 - avgError / targetRadius) * 100).toFixed(1);
}

function updateAccuracy() {
  const accuracy = calculateAccuracy();
  document.getElementById("status").textContent = `Drawing... Accuracy: ${accuracy}%`;
}

function showResult(message) {
  if (points.length < 10) return;

  const accuracy = calculateAccuracy();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = "#ff6f61";
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (let i = 0; i < points.length; i++) {
    const pt = points[i];
    if (i === 0) ctx.moveTo(pt.x, pt.y);
    else ctx.lineTo(pt.x, pt.y);
  }
  ctx.stroke();

  document.getElementById("status").textContent = `Accuracy: ${accuracy}% - ${message}`;
  isDrawing = false;
}

canvas.addEventListener("mousedown", (e) => {
  if (timeout) {
    resetGame();
    return;
  }

  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  if (!isDrawing) {
    const dx = x - center.x;
    const dy = y - center.y;
    targetRadius = Math.sqrt(dx * dx + dy * dy);
    points = [{ x, y }];
    isDrawing = true;
    startTimer();
    document.getElementById("status").textContent = "Drawing... Accuracy: --%";
  } else {
    points.push({ x, y });

    if (points.length > 10) {
      const start = points[0];
      const dx = x - start.x;
      const dy = y - start.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 15) { // Tightened threshold for more precision
        showResult("Circle completed!");
      }
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCenterPoint();
    ctx.strokeStyle = "#ffcc5c";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i < points.length; i++) {
      const pt = points[i];
      if (i === 0) ctx.moveTo(pt.x, pt.y);
      else ctx.lineTo(pt.x, pt.y);
    }
    ctx.stroke();
    updateAccuracy();
  }
});

canvas.addEventListener("mousemove", (e) => {
  if (!isDrawing || timeout) return;

  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  points.push({ x, y });

  if (points.length > 10) {
    const start = points[0];
    const dx = x - start.x;
    const dy = y - start.y;
    const dist = Math.sqrt(dx * dx + dy * dy);
    if (dist < 15) { // Tightened threshold for more precision
      showResult("Circle completed!");
    }
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawCenterPoint();
  ctx.strokeStyle = "#ffcc5c";
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (let i = 0; i < points.length; i++) {
    const pt = points[i];
    if (i === 0) ctx.moveTo(pt.x, pt.y);
    else ctx.lineTo(pt.x, pt.y);
  }
  ctx.stroke();
  updateAccuracy();
});

canvas.addEventListener("mouseup", () => {
  isDrawing = false;
});

// Initial setup
resetGame();