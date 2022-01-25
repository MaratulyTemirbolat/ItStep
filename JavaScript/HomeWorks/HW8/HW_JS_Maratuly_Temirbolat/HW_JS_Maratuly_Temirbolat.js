let darkButton = document.getElementById("dark-button");
let lightButton = document.getElementById("ligth-button");
let colorfullButton = document.getElementById("colorfull-button");

console.log(localStorage.getItem("color"))

darkButton.onclick = function(){
    document.body.style.backgroundColor = "black";
    localStorage.setItem("color","black");   
}
lightButton.onclick = function(){
    document.body.style.backgroundColor = "white";
    localStorage.setItem("color","white");
}
colorfullButton.onclick = function(){
    document.body.style.backgroundColor = "yellow";
    localStorage.setItem("color","yellow");
}

if(localStorage.getItem("color") != null){
    document.body.style.backgroundColor = localStorage.getItem("color")
}