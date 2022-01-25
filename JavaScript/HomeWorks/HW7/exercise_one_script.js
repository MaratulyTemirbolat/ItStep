let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
canvas.style.zIndex = '1';


let xCoordinate = undefined, yCoordinate = undefined;
const circleRadius = 100;

// canvas.onmousemove = function(event){
//     xCoordinate = event.offsetX;
//     yCoordinate = event.offsetY;
//     ctx.clearRect(0,0,canvas.width,canvas.height);
//     ctx.beginPath();
//     ctx.moveTo(xCoordinate + circleRadius,yCoordinate);
//     ctx.arc(xCoordinate,yCoordinate,circleRadius,0,2*Math.PI);
//     ctx.stroke();
// }

canvas.onclick = function(event){
    // ctx.moveTo(event.offsetX,event.offsetY);
    ctx.lineTo(event.offsetX,event.offsetY);
    ctx.stroke();
}