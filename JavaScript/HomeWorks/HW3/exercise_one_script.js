let openModalWindowButton = document.getElementById("open-modal");

let modalWindow = document.getElementsByClassName("modal-window")[0];

let closeModalWindowButton = document.getElementById("close-modal")

openModalWindowButton.onclick = function(){
    modalWindow.style.display = "block";
}
closeModalWindowButton.onclick = function(){
    modalWindow.style.display = "none";
}