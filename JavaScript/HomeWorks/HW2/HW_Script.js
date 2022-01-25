// Exercise 1
/*
let userString = prompt("Введите вашу строку для выявления статистики")

function isSpecialSymbol(userLetter){
    let specialLetters = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','/',',','.','{','}','[',']']
    if(specialLetters.includes(userLetter)) return true;
    return false;
}

function isLetter(userLetter){
    const firstLetter = 'a';
    const lastLetter = 'z';
    const firstRussianLetter = 'а';
    const lastRussianLetter = 'я';
    if((userLetter.toLowerCase() >= firstLetter && userLetter.toLowerCase() <= lastLetter) || (userLetter.toLowerCase() >= firstRussianLetter && userLetter.toLowerCase() <= lastRussianLetter)) return true;
    return false;
}

function isFigure(userFigure){
    const minFigure = '0';
    const maxFigure = '9';
    if(userFigure >= minFigure && userFigure <= maxFigure) return true;
    return false;
}

function viewStringStatistics(myString){
    let letterCounter = 0;
    let figureCounter = 0;
    let specialSymbolCounter = 0;
    for(let strIndex = 0; strIndex < myString.length; strIndex++){
        if(isSpecialSymbol(myString[strIndex])){
            specialSymbolCounter++;
        }
        if(isLetter(myString[strIndex])){
            letterCounter++;
        }
        if(isFigure(myString[strIndex])){
            figureCounter++;
        }
    }
    console.log(`Количество букв в слове ${myString} составляет: ${letterCounter}, цифр: ${figureCounter}, специальных символов: ${specialSymbolCounter}`)

}

viewStringStatistics(userString)
*/

//Exercise 4
/*
let userStyle = prompt('Введите пожалуйста название CSS стиля с дефисом')

function getCamelStyle(userString){
    const hyphen = '-';
    let camelString = "";
    userString = userString.split(hyphen);
    camelString+=userString[0]
    if(userString.length >= 2){
        for(let strIndex = 1; strIndex < userString.length; strIndex++){
            camelString += userString[strIndex][0].toUpperCase() + userString[strIndex].slice(1);
        }
    }
    return camelString;
}

console.log('Ваш CSS стиль в CamelCase:',getCamelStyle(userStyle))
*/

//Exercise 6
/*
function getCombinedString(oldString,newString){
    return oldString + newString;
}

let isRunning = true;
const exitOptionFigure = '0';
const exitOptionWord = 'exit';
let combinedString = '';
do{
    let newString = prompt("Пожалуйста, введите вашу строку. Чтобы выйти из программы, введите 0 или 'exit'");
    if(newString == exitOptionFigure || newString == exitOptionWord) isRunning = false;
    else combinedString = getCombinedString(combinedString,newString);
}while(isRunning)

console.log("Ваша объединённая строка:",combinedString);
*/