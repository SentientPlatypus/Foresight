var mainCanvas = document.getElementById("mainCanvas");
var c = mainCanvas.getContext("2d");

var x = mainCanvas.width / 2;
var y = mainCanvas.height / 2;
var arrowWidth = 20;
var arrowHeight = 40;
var arrowColor = "blue";
var arrowSpeed = 2;
var arrowDirection = 1; // 1 for up, -1 for down

function drawArrow() {
    c.clearRect(0, 0, mainCanvas.width, mainCanvas.height);

    c.fillStyle = arrowColor;
    c.beginPath();
    c.moveTo(x, y);
    c.lineTo(x - arrowWidth / 2, y + arrowHeight * arrowDirection);
    c.lineTo(x + arrowWidth / 2, y + arrowHeight * arrowDirection);
    c.closePath();
    c.fill();

    // Change direction if the arrow reaches the canvas boundaries
    if (y <= arrowHeight / 2 || y >= mainCanvas.height - arrowHeight / 2) {
        arrowDirection *= -1;
    }

    // Update the arrow's position
    y += arrowSpeed * arrowDirection;

    requestAnimationFrame(drawArrow);
}

drawArrow();