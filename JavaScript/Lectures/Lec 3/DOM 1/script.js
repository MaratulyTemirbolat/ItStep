// let el = document.getElementById("el")
// console.log(el.id)

// let els = document.getElementsByClassName("main")
// console.log(els)

// let els = document.getElementsByTagName("div")
// console.log(els)

// -------------------------

// let el = document.querySelector(".main")
// console.log(el)

// let els = document.querySelectorAll("#el")
// console.log(els)

// let el = document.getElementById("el")
// console.log(el.textContent)
// el.textContent = "Новое значение"
// el.textContent = "<h1>Новое значение</h1>"

// el.innerHTML = "<h1>Новое значение</h1>"
// el.style.color = "orange"
// el.style.backgroundColor = "orange"
// el.href = "https://ya.ru"
// console.log(el.className)

// let el = document.querySelector("#el")
// let btn = document.querySelector("#btn")

// function handler(){
//     el.style.color = "orange"
// }

// btn.onclick = handler
// let mainElements = document.getElementsByClassName("main")

// btn.onclick = function(){
//     for (let item of mainElements){
//         item.style.color = "green"
//     }
// }

// Задания: 1, 3, 4

let el = document.querySelector("#el")
let min = 10
let max = 20

let randomNumber = Math.floor(Math.random()*(max-min)+min)

el.textContent = randomNumber