// require()
// import * as dat from '../../../../node_modules/dat.gui'

var mainCanvas = document.getElementById("mainCanvas");
var c = mainCanvas.getContext("2d");
// const gui = new dat.GUI();

mainCanvas.width = innerWidth;
mainCanvas.height = innerHeight;


const wave = {
    y: mainCanvas.height / 2,
    length: 0.01,
    amplitude: 0.01,
    frequency: 0.015
};

const strokeColor = {
    h:176,
    s:100,
    l:75
}

const backgroundColor = {
    r: 20,
    g: 20,
    b: 20,
    a: 1
}

// gui.add(wave, 'y');

c.lineWidth = 3;

var mousex = 0;
var mousey = 0;

document.addEventListener("mousemove", () => {
    mousex = event.clientX; // Gets Mouse X
    mousey = event.clientY; // Gets Mouse Y
});




console.log(mousey)
let increment = wave.frequency;
function animate() {
    requestAnimationFrame(animate);
    // c.clearRect(0,0, mainCanvas.width, mainCanvas.height);
    c.fillStyle = `rgba(${backgroundColor.r}, ${backgroundColor.g}, ${
        backgroundColor.b
      }, ${backgroundColor.a})`
    c.fillRect(0, 0, mainCanvas.width, mainCanvas.height);


    c.beginPath();
    c.moveTo(0, mainCanvas.height / 2);
    
    for (let i = 0; i < mainCanvas.width; i+=100)
    {
        c.lineTo(i, Math.random() * mainCanvas.height + 1);
    }
    c.strokeStyle = `hsl(${strokeColor.h}, ${strokeColor.s}%, ${strokeColor.l}%)`;
    c.stroke();
    wave.amplitude = (mousey - wave.y)
    increment += wave.frequency;

}

animate();
