// let myVar = 10
// console.log(myVar)
// myVar = "aaa"
// myVar = true
// alert("hello world")

// console.log("5" === 5)
// let age = prompt("Сколько вам лет")
// console.log(age)

// let agree = confirm("Вы согласны")
// console.log(agree)

// let n = prompt("число")
// console.log(Number(n) + 10)
// console.log(parseInt(n) + 10)
// console.log(parseFloat(n) + 10)
// console.log(+n + 10)

// let a = 5
// // a++ //постфиксный
// // ++a //префиксный
// // a--
// // --a
// console.log(a)
// console.log(a++)
// console.log(a)

// let age = prompt("Ваш возраст")
// if (age < 18) {
//     alert("Вам сюда нельзя")
//     console.log("ДОП")
// } else if (age > 120) {
//     alert("Вы слишком старый")
// }
          
// let a = 5 < 2 ? 0 : 1
// console.log(a)

// let a = +prompt("цифру")

// switch(a) {
//     case 1: 
//         console.log("one")
//         break
//     case 2:
//         console.log("two")
//         break
//     default:
//         console.log("я не знаю таких цифр")
// }

let month = +prompt("Введите номер месяца")
switch(month){
    case 12: 
    case 1: 
    case 2: console.log("Зима"); break;
    case 3:
    case 4:
    case 5: console.log("Весна"); break;
    case 6:
    case 7:
    case 8: console.log("Лето"); break;
    case 9:
    case 10:
    case 11: console.log("Осень"); break;
    default: console.log("Такого месяца нет")
}