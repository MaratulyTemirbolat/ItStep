let buttonSwitch = document.getElementById("switch-colors");
let trafficLights = document.getElementsByClassName("shape");
let counter = -1;
const maxNumber = 3;

buttonSwitch.onclick = function(){
    counter ++;
    if(counter == maxNumber) counter = 0;
    
    if(counter == 0){
        trafficLights[0].style.backgroundColor = "limegreen";
        trafficLights[1].style.backgroundColor = "grey";
        trafficLights[2].style.backgroundColor = "grey";
    } 
    else if(counter == 1){
        trafficLights[0].style.backgroundColor = "grey";
        trafficLights[1].style.backgroundColor = "yellow";
        trafficLights[2].style.backgroundColor = "grey";
    }
    else if(counter == 2){
        trafficLights[0].style.backgroundColor = "grey";
        trafficLights[1].style.backgroundColor = "grey";
        trafficLights[2].style.backgroundColor = "red";
    }
}