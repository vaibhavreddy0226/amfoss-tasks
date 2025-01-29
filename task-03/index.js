const playSound = (key) => {
  const sounds = {
    w: "sounds/crash.mp3",
    a: "sounds/kick-bass.mp3",
    s: "sounds/snare.mp3",
    d: "sounds/tom-1.mp3",
    j: "sounds/tom-2.mp3",
    k: "sounds/tom-3.mp3",
    l: "sounds/tom-4.mp3",
  };

  const soundFile = sounds[key];

  if (soundFile) {
    const audio = new Audio(soundFile);
    audio.play();
    addButtonAnimation(key);
  } 
};

const handleButtonClick = (event) => {
  const buttonKey = event.target.innerHTML;
  playSound(buttonKey);
};

const handleKeydown = (event) => {
  playSound(event.key);
};

const addButtonAnimation = (key) => {
  const button = document.querySelector(.${key});
  if (button) {
    button.classList.add("pressed");
    setTimeout(() => button.classList.remove("pressed"), 100);
  }
};

document.querySelectorAll(".drum").forEach((button) => {
  button.addEventListener("click", handleButtonClick);
});

document.addEventListener("keydown", handleKeydown);

const initializeDrumButtons = () => {
  const buttons = document.querySelectorAll(".drum");
  const keys = ["w", "a", "s", "d", "j", "k", "l"];
  buttons.forEach((button, index) => {
    button.innerHTML = keys[index];
    button.classList.add(keys[index]);
  });
};

initializeDrumButtons();