// for (let i = 0; i < 10; i++){
//     document.write(i)
//     document.write("<br>")
// }
// myFn()
// function myFn(){
//     console.log("Моя функция работает") 
// }

// let a = myFn
// a()
// let b = 12
// let anonymFn = function(){
//     let c = 14
//     console.log("Анонимная функция")
//     let a = function(){
//         console.log(b,c)
//     }
//     a()
// }
// anonymFn()

// let arr = [1, 5, 8, 9]
// console.log(arr[1])

// let student = {
//     name: "Oleg",
//     age: 26
// }
// let student2 = student
// student2.name = "Andrew"
// console.log(student.name)
// student.group = "PYE-211"

// let arr = [1, 5, 8, 9]
// console.log(arr.length)

// let n = 7
// console.log( n.toExponential() )

// let arr = [1, 5, 8, 9]

// arr.push(42)
// arr.pop()
// arr.unshift(42)
// arr.shift()
// console.log(arr)

// let str = arr.join("")
// console.log(str)
// arr.splice(1)
// arr.splice(0, 2)
// arr.splice(1, 2, 0, 0, 0, 0)
// arr.splice(2, 0, 7)
// console.log(arr)

// let arr = [1, 5, 8, 9]

// for (let i = 0; i < arr.length; i++){
//     document.write(arr[i] + "<br>")
// }

// for (let item of arr){
//     document.write(item + " ")
// }

// let str = "Это моя строка"
// console.log(str[2])
// console.log(str.length)
// let str2 = str.substring(4, 10)
// let str2 = str.slice(4, -1)
// console.log(str2)
// let str = "Это моя строка"
// console.log( str.split("") )

let age = 29
let str = `Мне ${age} лет`
console.log(str)