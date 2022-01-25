let passedTime = document.querySelector('span');
let btn = document.querySelector('button');

let isSwitchOn = false;
const oneSecond = 1;
let timeId = undefined;
btn.onclick = function(){
    if(isSwitchOn === false){
        isSwitchOn = true;
        timeId = setInterval(startTimer,1000);
    }
    else isSwitchOn = false;
}


function startTimer(){
    if(isSwitchOn) passedTime.textContent = Number(passedTime.textContent) + oneSecond;
    else clearInterval(timeId);
}
