let monthInfo = document.getElementById('month-info');
let yearInfo = document.getElementById('year-info');
let btn = document.getElementById('btn');
let months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const minDayIndex = 0;
const maxDayIndex = 6;
const oneIndexStep = 1;
let newDateInitial = undefined;
let lastDay = undefined;
let dateTimeInfo = document.getElementById('date-time-info');
const daysPerWeek = 7;
let lastWeekDay = undefined;
let tableBody = document.querySelector("tbody");
let tableFoot = document.querySelector("tfoot");
const minMonth = 1;
const maxMonth = 12;
const minYear = 1970;


function deleteCells(){
    let weekLines = document.getElementsByClassName('daysLine');
    for(let week of weekLines){
        week.remove();
    }
    return weekLines.length
}

btn.onclick = function(event){

    if(monthInfo.value != '' && yearInfo.value != ''){
        if(Number(monthInfo.value) >= minMonth && Number(monthInfo.value) <= maxMonth && Number(yearInfo.value) >= minYear){
            while(deleteCells() != 0) deleteCells();
            let givenYear = Number(yearInfo.value);
            let givenMonth = Number(monthInfo.value);

            dateTimeInfo.textContent = months[givenMonth - oneIndexStep] + ', ' + givenYear;

            newDateInitial = new Date(givenYear,givenMonth - oneIndexStep,1);
            lastWeekDay = (new Date(givenYear,givenMonth,0)).getDay();
            lastDay = (new Date(givenYear,givenMonth,0)).getDate();

            let initialDayWeekIndex = newDateInitial.getDay();
            if(initialDayWeekIndex == minDayIndex) initialDayWeekIndex = maxDayIndex;
            else initialDayWeekIndex -= oneIndexStep;

            if(lastWeekDay == minDayIndex) lastWeekDay = maxDayIndex;
            else lastWeekDay -= oneIndexStep;
            let remaindedDaysToEndWeek = daysPerWeek - (lastWeekDay + 1);
            let totalDaysWithEmptyCells = lastDay + initialDayWeekIndex + remaindedDaysToEndWeek;
            
            let totalWeeks = parseInt(totalDaysWithEmptyCells / daysPerWeek);
            let currentDay = 1;
            let newLine = document.createElement('tr');
            newLine.className = 'daysLine';
            let currentWeekDay = 0;
            while(currentWeekDay <= maxDayIndex){
                let newCell = document.createElement('td');
                newCell.className = 'days';
                if(currentWeekDay >= initialDayWeekIndex){
                    newCell.textContent = currentDay;
                    currentDay++;
                }
                else{
                    newCell.textContent = '';
                }
                newLine.append(newCell);
                currentWeekDay++;
            }
            tableBody.append(newLine);
            currentWeekDay = 0;
            for(let curWeek = 0; curWeek < totalWeeks - 2;curWeek++){
                let newLineWeek = document.createElement('tr');
                newLineWeek.className = 'daysLine';
                while(currentWeekDay <= maxDayIndex){
                    let newCell = document.createElement('td');
                    newCell.className = 'days';
                    newCell.textContent = currentDay;
                    currentDay++;
                    newLineWeek.append(newCell);
                    currentWeekDay++;
                }
                tableBody.append(newLineWeek)
                currentWeekDay = 0;
            }
            currentWeekDay = 0;
            let lastLineWeek = document.createElement('tr');
            lastLineWeek.className = 'daysLine';
            while(currentWeekDay <= maxDayIndex){
                let newCell = document.createElement('td');
                newCell.className = 'days';
                if(currentWeekDay<=lastWeekDay){
                    newCell.textContent = currentDay;
                    currentDay++;
                }
                else{
                    newCell.textContent = '';
                }
                lastLineWeek.append(newCell);
                currentWeekDay++;
            }
            tableFoot.append(lastLineWeek);
        }
        else{
            alert('Вы вышли за границы диапазона!')
        }
    }
    else{
        alert('Вы не ввели данные полностью!')
    }
    event.preventDefault();
}
