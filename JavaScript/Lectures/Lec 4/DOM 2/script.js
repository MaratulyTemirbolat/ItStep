// let container = document.getElementById("container")

// let date = new Date()
// container.textContent = date

// container.textContent = date.toLocaleString()

// container.textContent = date.getMilliseconds()
// container.textContent = date.getSeconds()
// container.textContent = date.getMinutes()
// container.textContent = date.getHours()
// container.textContent = date.getDate()
// container.textContent = date.getMonth()
// container.textContent = date.getFullYear()
// container.textContent = date.getDay()

// date.setMilliseconds(10000)
// date.setSeconds(11)
// date.setMinutes(25)
// date.setHours(25)
// date.setDate(1)
// date.setMonth(11)
// date.setFullYear(2020)

// let date = new Date(2015, 9, 1, 12, 45, 32, 1500)
// let date = new Date(2015, 9)
// let date = new Date(2015)
// container.textContent = date.toLocaleString()
// let date = new Date(2022, 2, 24)
// let now = new Date()
// container.textContent = date - now

// function changeText(){
//     container.textContent += "!!!"
// }
// // setTimeout(changeText, 2000)
// let timerId = setInterval(changeText, 2000)
// // clearInterval(timerId)
// // console.log(timerId)
// setTimeout(function(){
//     clearInterval(timerId)
// }, 5000)

// let container = document.getElementById("container")
// let nextYear = (new Date()).getFullYear() + 1
// let nextNewYear = new Date(nextYear, 0, 1)

// function calc(){
//     let now = new Date()
//     let diff = nextNewYear - now
//     let sec = Math.floor(diff / 1000)
//     let min = Math.floor(sec / 60)
//     let hours = Math.floor(min / 60)
//     let days = Math.floor(hours / 24)
//     container.textContent = 
//     `${days} ${hours % 24} ${min % 60} ${sec % 60}`
// }

// setInterval(calc, 1000)

// let container = document.getElementById("container")
// console.log( container.parentElement )
// console.log( container.nextElementSibling )
// console.log( container.previousElementSibling )
// console.log( container.firstElementChild )
// console.log( container.lastElementChild )
// console.log( container.children )

// console.log( container.parentNode )
// console.log( container.nextSibling )
// console.log( container.previousSibling )
// console.log( container.firstChild )
// console.log( container.lastChild )
// console.log( container.childNodes )
// let divs = container.querySelectorAll("div")
// console.log(divs)

let btn = document.querySelector("#btn"),
    input = document.querySelector("#input")

btn.onclick = function(){
    console.log(input.value)
}
btn.onmouseenter = function(){
    console.log("enter")
}
btn.onmouseout = function(){
    console.log("out")
}