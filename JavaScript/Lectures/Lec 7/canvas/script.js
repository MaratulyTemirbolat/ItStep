// navigator.geolocation.getCurrentPosition(function(position){
//     console.log(position)
// })

let canvas = document.getElementById("canvas")

let ctx = canvas.getContext("2d")
// ctx.strokeRect(100, 100, 300, 500)
// ctx.fillRect(100, 100, 300, 500)

// for (let i = 0; i < 160; i++){
//     for (let j = 0; j < 90; j++) {
//         // if ( (i + j) % 2 == 0 ) {
//         //     ctx.fillRect(i * 100, j * 100, 100, 100)
//         // } else {
//         //     ctx.strokeRect(i * 100, j * 100, 100, 100)
//         // }
//         let r = Math.random()*256
//         let g = Math.random()*256
//         let b = Math.random()*256
//         ctx.fillStyle = `rgb(${r},${g},${b})`
//         ctx.fillRect(i * 10, j * 10, 10, 10)
//     }
// }

// ctx.moveTo(800, 450)
// ctx.lineTo(100, 450)
// ctx.lineTo(100, 100)
// // ctx.lineTo(800,450)
// ctx.stroke()
// ctx.lineWidth = 20
// // ctx.strokeStyle = "orange"
// // ctx.fillStyle = "rgb(125, 25, 10)"
// // ctx.fill()
// ctx.beginPath()
// ctx.arc(1100, 200, 200, 45 * Math.PI / 180, 315 * Math.PI / 180, true)
// // ctx.stroke()
// ctx.fill()

// ctx.lineWidth = 10
// canvas.onmousemove = function(event){
//     ctx.clearRect(0, 0, canvas.width, canvas.height)
//     ctx.beginPath()
//     ctx.moveTo(0, 0)
//     // ctx.quadraticCurveTo(event.offsetX, event.offsetY, 0, 900)
//     ctx.bezierCurveTo(event.offsetX, event.offsetY, 
//                       canvas.width, 0,
//                       canvas.width, canvas.height)
//     ctx.stroke()
// }

// let img = document.createElement('img')
// // let img = new Image()
// img.src = "cat.jpg"
// img.onload = function(){
//     // ctx.drawImage(img, 200, 200)
//     // ctx.drawImage(img, 200, 200, 400, 100)
//     ctx.drawImage(img, 
//         0, 200,
//         200, 200,
//         800, 450,
//         400, 400)
// }

// let grad = ctx.createLinearGradient(0, 0, 1600, 900)
// grad.addColorStop(0, "red")
// grad.addColorStop(0.5, "yellow")
// grad.addColorStop(1, "blue")
// ctx.fillStyle = grad
// // ctx.fillRect(0, 0, 1600, 900)
// canvas.onmousemove = function(event) {
//     ctx.clearRect(0, 0, 1600, 900)
//     ctx.fillRect(event.offsetX - 100, event.offsetY - 100, 200, 200)
// }

// let grad = ctx.createRadialGradient(800, 450, 10, 
//                                     800, 450, 800)
// grad.addColorStop(0, "black")
// grad.addColorStop(1, "white")

// ctx.fillStyle = grad
// ctx.fillRect(0, 0, 1600, 900)
// canvas.onmousemove = function(event){
//     ctx.clearRect(0, 0, 1600, 900)
//     let grad = ctx.createRadialGradient(
//         800, 450, 10, 
//         event.offsetX, event.offsetY, 800)
//     grad.addColorStop(0, "black")
//     grad.addColorStop(1, "white")

//     ctx.fillStyle = grad
//     ctx.fillRect(0, 0, 1600, 900)
// }

// let x = 0, y = 0;
// let cx = 1, cy = 1;
// function draw(time){
//     console.log(time)
//     ctx.clearRect(0, 0, canvas.width, canvas.height)
//     ctx.fillRect(x, y, 200, 100)
//     if (x > canvas.width - 200 || x < 0) cx *= -1
//     if (y > canvas.height - 100 || y < 0) cy *= -1
//     x += cx
//     y += cy
//     requestAnimationFrame(draw)
// }
// // setInterval(draw, 10)
// requestAnimationFrame(draw)

let x = 0
let d = 20
let cd = -1
ctx.fillStyle = "yellow"
function draw(){
    ctx.clearRect(0, 0, 1600, 900)
    ctx.beginPath()
    
    ctx.arc(x, 450, 200, (0 + d) * Math.PI / 180, (360 - d) * Math.PI / 180)
    ctx.lineTo(x, 450)
    if (d < 5 || d > 45) cd *= -1
    d += cd
    ctx.fill()
    x += 5
    if (x > 1800) x = -200
    requestAnimationFrame(draw)
}

requestAnimationFrame(draw)