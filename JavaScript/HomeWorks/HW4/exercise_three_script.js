let registerItems = document.getElementsByClassName('regi-input');
let loginItems = document.getElementsByClassName('log-input');
let regForm = document.getElementById('registration');
let logForm = document.getElementById('entrance');

for(item of registerItems){
    item.onclick = function(){
        regForm.style.backgroundColor = 'cadetblue';
        logForm.style.backgroundColor = 'unset';
    }
}

for(item of loginItems){
    item.onclick = function(){
        regForm.style.backgroundColor = 'unset';
        logForm.style.backgroundColor = 'cornflowerblue'; 
    }
}