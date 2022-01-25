// Задание 1
/*
let userAge = parseInt(prompt("Укажите ваш возраст"));

const childAgeMinimum = 0;const childAgeMaximum = 12;
const teenagerAgeMaximum = 18;
const adultAgeMaximum = 60;

if(userAge >= childAgeMinimum){
    if(userAge >= childAgeMinimum && userAge < childAgeMaximum) console.log("Вы являетесь ребенком")
    else if(userAge >= childAgeMaximum && userAge < teenagerAgeMaximum) console.log("Вы являетесь подростком")
    else if(userAge >=teenagerAgeMaximum && userAge < adultAgeMaximum) console.log("Вы являетесь взрослым")
    else console.log("Вы являетесь пенсионером")
}
else alert("Такого возраста не бывает")
*/

//Задание 2
/*
let userNumber = parseInt(prompt("Укажите цифру(0-9), чтобы вывести соответствующий спец.символ"))

const maxFigure = 9; const minFigure = 0;


switch(userNumber){
    case 0: console.log("Символ цифре 0 соответствует: ) "); break;
    case 1: console.log("Символ цифре 1 соответствует: ! "); break;
    case 2: console.log("Символ цифре 2 соответствует: @ "); break;
    case 3: console.log("Символ цифре 3 соответствует: # "); break;
    case 4: console.log("Символ цифре 4 соответствует: $ "); break;
    case 5: console.log("Символ цифре 5 соответствует: % "); break;
    case 6: console.log("Символ цифре 6 соответствует: ^ "); break;
    case 7: console.log("Символ цифре 7 соответствует: & "); break;
    case 8: console.log("Символ цифре 8 соответствует: * "); break;
    case 9: console.log("Символ цифре 9 соответствует: ( "); break;
    default: alert("Ваше число не является цифрой, оно вне диапазона от 0 до 9."); break;
}
*/



//Задание 4

// Используя Конструкцию If

/*
let year = parseInt(prompt("Укажите год для проверки на високосность"));

if (year % 4 != 0) console.log(String(year) + " год " + "Не является Високосным")
else if(year % 100 == 0){
    if (year % 400 == 0){
        console.log(String(year) + " год " + "является Високосным годом")
    }
    else console.log(String(year) + " год " + "Не является Високосным")
}
else console.log(String(year) + " год " + "Является Високосным годом")
*/

// Используя Тернарный оператор

/*
let year = parseInt(prompt("Укажите год для проверки на високосность"));

let yearDescription = (year % 100 == 0) ? ((year % 400 == 0) ? "Високосный" : "Не високосный") : ((year % 4 == 0) ? "Високосный" : "Не високосный" );

console.log("Ваш год:",yearDescription);
*/

//Задание 7

// Используя If
/*
let purchaseSum = parseInt(prompt("Укажите сумму вашей покупки"));

if(purchaseSum >= 200){
    let discountSum = undefined;
    if(purchaseSum >=200 && purchaseSum < 300) discountSum = (purchaseSum * 3) / 100;
    else if(purchaseSum >= 300 && purchaseSum < 500) discountSum = (purchaseSum * 5)/100;
    else discountSum = (purchaseSum * 7)/100;
    alert("Ваша финальная сумма вместе со скидкой составит: " + String(parseInt(purchaseSum - discountSum)) + " тенге")
}
else if (purchaseSum >= 0 && purchaseSum < 200) alert("Конечная сумма останеться Неизменной: " + String(purchaseSum) + " тенге")
else alert("Сумма не может быть отрицательной!")
*/

//Использую Тернарный оператор
/*
let purchaseSum = parseInt(prompt("Укажите сумму вашей покупки"));

if(purchaseSum >= 200){
    let discountSum = purchaseSum >= 500 ? ((purchaseSum * 7)/100) : ((purchaseSum >= 200 && purchaseSum < 300) ? (purchaseSum * 3) / 100 :(purchaseSum * 5)/100);
    alert("Ваша финальная сумма вместе со скидкой составит: " + String(parseInt(purchaseSum - discountSum)) + " тенге")
}
else if (purchaseSum >= 0 && purchaseSum < 200) alert("Конечная сумма останеться Неизменной: " + String(purchaseSum) + " тенге");
else alert("Сумма не может быть отрицательной!");
*/