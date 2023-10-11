//////////////////////////////////////////////// INITIALIZE
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

ctx.imageSmoothingEnabled = true;
ctx.imageSmoothingQuality = 'high';

//////////////////////////////////////////////// IMAGES
const myImg = new Image();
myImg.onload = (e)=>{...};
myImg.onerror = (e)=>{...};
myImg.src = "PATH";

ctx.drawImage(myImg, x, y);
ctx.drawImage(myImg, x, y, w, h);
ctx.drawImage(myImg, srcX, srcY, srcW, srcH, x, y, w, h);

//////////////////////////////////////////////// KEYBOARD
const keys = {};
document.addEventListener("keydown", (e) =>{
  if (e.keyCode === 40){ keys[e.keyCode] = true}; // 40D, 39R, 38U, 37L, 32Space,
}, false);

///////////////////////////////////////////////// MOUSE
document.addEventListener("mousemove", (e) =>{
  const canvasRect = canvas.getBoundingClientRect();
  const mx = Math.round(c.clientX - canvasRect.left);
  const my = Math.round(c.clientY - canvasRect.top);

////////////////////////////////////////////////// AUDIO
const beat = new Audio("path.mp3|.wav");
beat.play();
beat.pause();
beat.load();
	
///////////////////////////////////////////////// TEXT
ctx.font = '25px Arial';
ctx.textAlign = 'right';
ctx.textBaseline = 'bottom';

ctx.fillText("Hello world", x, y);

/////////////////////////////////////////////////  FIGURES
ctx.fillStyle = 'CSS COLOR';
ctx.strokeStyle = 'CSS COLOR';
ctx.lineWidth = 5;

ctx.fillRect(x, y, w, h); // RECTANGLE

ctx.beginPath(); // CIRCLE
ctx.arc(x, y, R, 0, 2 * Math.PI);
ctx.fill(); // ctx.stroke();
ctx.endPath();

ctx.beginPath(); // LINE
ctx.moveTo(10, 10);
ctx.lineTo(100, 100);
ctx.stroke();
ctx.endPath();

const svgPath = new Path2D('M24.85.ETC.SVG_DATA'); // SVG
ctx.beginPath();
ctx.stroke(path);
ctx.fill(path);
ctx.endPath();

/////////////////////////////////////////////// TRANSFORMS
ctx.translate(figureX, figureY);
ctx.rotate(Math.PI / 180 * (figureAngle + 90));
ctx.translate(-figureX, -figureY);

ctx.drawFigure();
ctx.setTransform(1, 0, 0, 1, 0, 0);

/////////////////////////////////////////////// GAME LOOP
let prevTime = Date.now();
const gameLoop = () => {
  let currentTime = Date.now();
  let deltaTime = currentTime - prevTime;
  let secondsPassed = deltaTime / 1000;
  let fps = 1 / secondsPassed;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  update(deltaTime);
  draw();
  prevTime = currentTime;
  window.requestAnimationFrame(gameLoop);
}

/////////////////////////////////////////////// ADVANCED
// pixel manipulation https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas
