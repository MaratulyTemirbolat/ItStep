// let h1 = document.createElement("h1")
// h1.textContent = "Привет"
// h1.className = "my-class"

// console.log(h1)

// let container = document.getElementById("container")

// container.append(h1)
// container.prepend(h1)
// container.after(h1)
// container.before(h1)
// container.replaceWith(h1)
// container.replaceChild(h1, container.lastElementChild)
// container.insertBefore(h1, container.lastElementChild)

// h1.onclick = function(){
//     this.remove()
// }
// container.append(h1)
// let container = document.getElementById("container")

// let items = ["Хлеб", "Молоко", "Арбуз"]

// let ul = document.createElement("ul")
// for (let item of items){
//     let li = document.createElement("li")
//     li.textContent = item
//     ul.append(li)
// }
// container.append(ul)

let btn = document.querySelector("#btn")

btn.onclick = function(event){
    // console.log(event)
    // event.preventDefault()
    console.log("button")
}
let container = document.querySelector("#container")
container.onclick = function(event){
    // console.log(event)
    event.stopPropagation()
}
document.body.onclick = function(){
    console.log("body")
}


// document.body.oncontextmenu = function(event){
//     event.preventDefault();
//     // return false
// }

window.onkeydown = function(event){
    // console.log(event.key)
    // event.preventDefault()
    if (event.key == "r" && event.ctrlKey){
        event.preventDefault()
        document.body.style.backgroundColor = "red"
    } else 
    if (event.key == "w"){
        document.body.style.backgroundColor = "white"
    }

}