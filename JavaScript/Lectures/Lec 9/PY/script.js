// let student = {
//     name: 'Oleg',
//     id: 1,
//     grades: [12, 11, 10]
// }

// let jsonString = `{
//     "name": "Oleg",
//     "age": 20,
//     "admin": false,
//     "grades": [
//         12,
//         11,
//         10
//     ]
// }`

// let jsonObj = JSON.parse(jsonString)
// console.log(jsonObj)

// let jsonString = JSON.stringify(student)
// console.log(jsonString)

// let loginInp = document.querySelector('#login'),
//     passwordInp = document.querySelector('#password'),
//     saveBtn = document.querySelector("#save")

// saveBtn.onclick = function () {
//     let saveObj = {
//         login: loginInp.value,
//         password: passwordInp.value
//     }
//     let str = JSON.stringify(saveObj)
//     localStorage.setItem("data", str)
// }

// let savedData = localStorage.getItem("data")

// if (savedData != null) {
//     let objFromLS = JSON.parse(savedData)
//     loginInp.value = objFromLS.login
//     passwordInp.value = objFromLS.password
// }

// let url = "https://reqres.in/api/users"

// let xhr = new XMLHttpRequest()

// let sendBtn = document.querySelector("#send"),
//     resDiv = document.querySelector("#res")

// sendBtn.onclick = function () {
//     resDiv.innerHTML = ""
//     xhr.open("GET", url)
//     xhr.send()
// }

// xhr.onreadystatechange = function () {
//     if (xhr.readyState == 4 && xhr.status == 200) {
//         let data = JSON.parse(xhr.response)
//         console.log(data)
//         for (let item of data.data) {
//             let itemContainer = document.createElement("div")
//             let nameBlock = document.createElement("h4")
//             nameBlock.textContent = item.first_name + " " + item.last_name
//             let emailBlock = document.createElement("p")
//             emailBlock.textContent = item.email
//             let photo = document.createElement("img")
//             photo.src = item.avatar
//             itemContainer.append(nameBlock, emailBlock, photo)
//             resDiv.append(itemContainer)
//         }
//     }
// }

// let url = "https://reqres.in/api/users"
// let sendBtn = document.querySelector("#send"),
//     resDiv = document.querySelector("#res")

// sendBtn.onclick = function () {
//     fetch(url)
//         .then(data => data.json())
//         .then(data => {
//             console.log(data)
//             for (let item of data.data) {
//                 let itemContainer = document.createElement("div")
//                 let nameBlock = document.createElement("h4")
//                 nameBlock.textContent = item.first_name + " " + item.last_name
//                 let emailBlock = document.createElement("p")
//                 emailBlock.textContent = item.email
//                 let photo = document.createElement("img")
//                 photo.src = item.avatar
//                 itemContainer.append(nameBlock, emailBlock, photo)
//                 resDiv.append(itemContainer)
//             }
//         })
// }

/*
    data => data.json()
    function(data) {
        return data.json()
    }

*/