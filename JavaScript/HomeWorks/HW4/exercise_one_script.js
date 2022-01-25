let dateWindow = document.getElementById('date-window');
let btn = document.getElementById('date-button');
let dateInformation = document.getElementsByClassName('info');
let givenData = [];
let todayDate = []
const oneStepYear = 1;
btn.onclick = function(){
    if((dateWindow.value).length == 0){
        alert('Вы не заполнили дату!')
    }
    else{
        givenData = (dateWindow.value).split('.');
        let dateBirth = new Date(Number(givenData[2]),Number(givenData[1]) - oneStepYear,Number(givenData[0]));
        if((dateBirth - new Date()) < 0){
            dateBirth.setFullYear(new Date().getFullYear() + oneStepYear);
        }
        dateInformation[3].textContent = Math.floor((dateBirth - (new Date()))/1000);
        dateInformation[2].textContent = Math.floor(Number(dateInformation[3].textContent) / 60);
        dateInformation[1].textContent = Math.floor(Number(dateInformation[2].textContent) / 60);
        dateInformation[0].textContent = Math.floor(Number(dateInformation[1].textContent) / 24);

        dateInformation[3].textContent %= 60;
        dateInformation[2].textContent %= 60;
        dateInformation[1].textContent %= 24;
    }
}
