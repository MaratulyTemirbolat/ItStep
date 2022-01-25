// document.cookie = "username=Ruslan;max-age=600"
// let cookies = document.cookie.split(/[=;]/)
// let index = cookies.indexOf("username")
// console.log(cookies)
// if (index != -1) {
//     document.write("Hello, " + cookies[index + 1])
// } else {
//     document.write("Hello, noname")
// }

// let list = document.getElementById("list"),
// inp = document.getElementById("inp"),
// btn = document.getElementById("btn")

// let listArr = []
// btn.onclick = function(){
//     let item = document.createElement("li")
//     item.textContent = inp.value
//     list.append(item)
//     listArr.push(inp.value)
//     localStorage.setItem("list", listArr)
// }

// if (localStorage.getItem("list")) {
//     listArr = localStorage.getItem("list").split(",")
//     for(let value of listArr) {
//         let item = document.createElement("li")
//         item.textContent = value
//         list.append(item)
//     }
// }

let regexp = /\d{1,3}/g
let str = "случайный текст 1 123 фффф 12  сссс"
// let res = str.search(regexp)
// let res = str.match(regexp)
// let res = str.replace(regexp, "___")
// let res = regexp.test(str)
let res = regexp.exec(str)
console.log(res)