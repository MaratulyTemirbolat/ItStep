let selectedMoney = document.getElementById("money-range");
let money = document.getElementById("money-info");
let durationCredit = document.querySelector("select");
const sixMonthPercent = 1.03, twelveMonthPercent = 1.06, twentyFourMonthPercent = 1.1; 
let monthPayment = document.querySelector('#final-money');
money.textContent = selectedMoney.value;
let sumPayment = 0;
let percentInfo = document.getElementById('percent-info');
let purchaseBlock = document.getElementById('purchase-block');
let btnClose = document.querySelector('button');
let extraWindow = document.getElementById('confirmation-window');
calculateCredit();

purchaseBlock.onclick = function(){
    extraWindow.style.display = "block";
}
btnClose.onclick = function(){
    extraWindow.style.display = "none";
}

function calculateCredit(){
    money.textContent = selectedMoney.value;

    if(durationCredit.value == '6'){
        sumPayment = Number(money.textContent) * sixMonthPercent;
        percentInfo.textContent = parseInt((sixMonthPercent - 1) * 100);
    }
    else if(durationCredit.value == '12'){
        sumPayment = Number(money.textContent) * twelveMonthPercent;
        percentInfo.textContent = parseInt((twelveMonthPercent - 1) * 100);
    }
    else if(durationCredit.value == '24'){
        sumPayment = Number(money.textContent) * twentyFourMonthPercent;
        percentInfo.textContent = parseInt((twentyFourMonthPercent - 1) * 100);
    }
    monthPayment.textContent = Math.round(sumPayment / durationCredit.value);
    console.log(durationCredit.value)
}

selectedMoney.oninput = calculateCredit;

durationCredit.onchange = calculateCredit;

