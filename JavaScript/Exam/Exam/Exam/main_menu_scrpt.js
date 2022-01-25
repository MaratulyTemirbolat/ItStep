let editUserPancels = document.getElementsByClassName("edit-user");
let userTable = document.getElementById("user-table");
let userEditPage = document.getElementById("edit-user");
let userTableLines = document.querySelectorAll(".user-line");
let btnEditSave = document.getElementById("btn-edit");
let userSelectedLineIndex = undefined;
let editPicturePencil = document.createElement("img");
editPicturePencil.className = "edit-user";
editPicturePencil.src = "pencil_two.png";
editPicturePencil.width = "30";
let namePart = document.getElementById("edit-name");
let phonePart = document.getElementById("edit-phone"),
order = undefined,
bestBooksMap = new Map(), bestVisitorsMap = new Map();

// localStorage.clear()
let regexPhoneNumber = /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/;

let editedUserId = undefined,userName = undefined,
userPhone = undefined

function deleteTableInfoPart(rowName){
    while(document.getElementsByClassName(rowName).length != 0){
        document.getElementsByClassName(rowName)[0].remove();
    }
}

function loadCustomerPartWindow(){
    deleteTableInfoPart("user-line");
    let systemUsers = localStorage.getItem("users");
    if(systemUsers != null){
        systemUsers = JSON.parse(systemUsers);
        for(let k = 0; k < systemUsers.length; k++){
            let newUserLine = document.createElement("tr");
            newUserLine.className = "user-line";
            let userIDCell = document.createElement("td");
            let userNameCell = document.createElement("td");
            let userPhoneCell = document.createElement("td");
            let userEditPictureCell = document.createElement("td");
            let editPicturePencil = document.createElement("img");
            editPicturePencil.className = "edit-user";
            editPicturePencil.src = "pencil_two.png";
            editPicturePencil.width = "30";
            editPicturePencil.onclick = function(){
                editedUserId = systemUsers[k].id;
                userEditPage.style.display = "flex";
                namePart.value = systemUsers[k].name;
                phonePart.value = systemUsers[k].phone;
                userEditedRow = newUserLine;
                console.log(namePart.value);
                console.log(phonePart.value);
            }
            userIDCell.textContent = systemUsers[k].id;
            userNameCell.textContent = systemUsers[k].name;
            userPhoneCell.textContent = systemUsers[k].phone;
            userEditPictureCell.append(editPicturePencil);
            newUserLine.append(userIDCell,userNameCell,userPhoneCell,userEditPictureCell);
            userTable.append(newUserLine);
        }
    }
}
function isCorrectPhone(phoneNumber){
    let result = regexPhoneNumber.test(phoneNumber);
    return result;
}
let userEditedRow = undefined;
btnEditSave.onclick = function(){
    console.log(phonePart.value,isCorrectPhone(phonePart.value));
    console.log(namePart.value,namePart.value.length);
    if(isCorrectPhone(phonePart.value) && namePart.value.length != 0){
        let userRowCells = userEditedRow.children;
        userRowCells[1].textContent = namePart.value;
        userRowCells[2].textContent = phonePart.value;
        userEditPage.style.display = "none";
        
        let currentUserId = userRowCells[0].textContent;
        allTheUsers = localStorage.getItem("users");
        if(allTheUsers != null){
            allTheUsers = JSON.parse(allTheUsers);
            for(let curUser of allTheUsers){
                if(curUser.id == currentUserId){
                    curUser.name = userRowCells[1].textContent;
                    curUser.phone = userRowCells[2].textContent;
                }
            }
            allTheUsers = JSON.stringify(allTheUsers);
            localStorage.setItem("users",allTheUsers);
            console.log(localStorage.getItem("users"));
        }
    }
    else alert("Номер телефона или имя введены неверно!")
}

let btnAddNewUserConfirmation = document.getElementById("btn-add"),
btnAddNewVisitor = document.getElementById("btn-new-visitor"),
addUserDataWindow = document.getElementById("add-user"),
addedUserName = document.getElementById("add-name"),
addedUserPhone = document.getElementById("add-phone"),
addBookDataWindow = document.getElementById("add-book"),
btnAddNewBookConfirmation = document.getElementById("btn-add-book"),
inputAddedBookName = document.getElementById("add-name-book"),
addCardDataWindow = document.getElementById("add-card"),
inputAddedCardVisitorName = document.getElementById("add-card-visitor-name"),
inputAddedCardBookName = document.getElementById("add-card-book-name"),
btnAddedNewCardConfirmation = document.getElementById("btn-add-new-card");

btnAddNewVisitor.onclick = function(){
    if(order == 1){
        addUserDataWindow.style.display = "flex";
        addedUserName.value = "";
        addedUserPhone.value = "";
        console.log(localStorage.getItem("users"));
    }
    else if(order == 0){
        addBookDataWindow.style.display = "flex";
        inputAddedBookName.value = "";
        console.log(localStorage.getItem("books"));
    }
    else if(order == 2){
        addCardDataWindow.style.display = "flex";
        inputAddedCardVisitorName.value = "";
        inputAddedCardBookName.value = "";
        console.log(localStorage.getItem("cards"));
    }
}

function isUserReturnSameBook(newCard){
    let allCards = localStorage.getItem("cards");
    if(allCards != null){
        allCards = JSON.parse(allCards);
        for(let curCard of allCards){
            if(curCard.visitorName == newCard.visitorName && curCard.bookName == newCard.bookName){
                if(curCard.returnDate == '') return false;
            }
        }
        return true;
    }
    return true;
}

function isBookOrVisitorInSystem(bookVisitorName,key){
    let allTheInfo = localStorage.getItem(key);
    if(allTheInfo == null) return false;

    allTheInfo = JSON.parse(allTheInfo);
    for(let k = 0;k < allTheInfo.length;k++){
        if(allTheInfo[k].name == bookVisitorName) return true;
    }
    return false;
}
// localStorage.clear();
btnAddedNewCardConfirmation.onclick = function(){
    if(inputAddedCardVisitorName.value.length != 0 && inputAddedCardBookName.value.length != 0){
        let isBookInSystem = isBookOrVisitorInSystem(inputAddedCardBookName.value,"books"),
        isVisitorInSystem = isBookOrVisitorInSystem(inputAddedCardVisitorName.value,"users");
        if(isBookInSystem && isVisitorInSystem){
            let borrowDate = new Date(), 
            date = String(borrowDate.getDate()),
            month = String(borrowDate.getMonth() + 1),
            fullYear =  String(borrowDate.getFullYear());
            if(date.length < 2) date = '0'+ date;
            if(month.length < 2) month = '0' + month;

            let newCard = {
                id:getNewBookId("card-line"),
                visitorName:inputAddedCardVisitorName.value,
                bookName:inputAddedCardBookName.value,
                borrowDate:(date + '.' + month + '.' + fullYear),
                returnDate:''
            }

            if(isUserReturnSameBook(newCard) == false){
                alert("Вы еще пользуетесь этой книгой! Сначала верните её")
                return
            }


            if(bestVisitorsMap.has(newCard.visitorName)){
                let quantity = bestVisitorsMap.get(newCard.visitorName) + 1;
                bestVisitorsMap.set(newCard.visitorName,quantity);
            }
            else bestVisitorsMap.set(newCard.visitorName,1);

            if(bestBooksMap.has(newCard.bookName)){
                let quantity = bestBooksMap.get(newCard.bookName) + 1;
                bestBooksMap.set(newCard.bookName,quantity);
            }
            else bestBooksMap.set(newCard.bookName,1);

            let newCardLine = document.createElement("tr");
            newCardLine.className = "card-line";
            let newCardId = document.createElement("td"),
            newCardVisitorCell = document.createElement("td"),
            newCardBookCell = document.createElement("td"),
            newCardBorrowCell = document.createElement("td"),
            newCardReturnCell = document.createElement("td");

            newCardId.textContent = newCard.id;
            newCardVisitorCell.textContent = newCard.visitorName;
            newCardBookCell.textContent = newCard.bookName;
            newCardBorrowCell.textContent = newCard.borrowDate;

            newCardReturnImg = document.createElement("img");

            newCardReturnImg.className = "return-book";
            newCardReturnImg.src = "return_icon.png";
            newCardReturnImg.width = "30";

            newCardReturnImg.onclick = function(){
                let returnDate = new Date(),dateReturn = String(returnDate.getDate()),
                monthReturn = String(returnDate.getMonth() + 1),
                fullYearReturn = String(returnDate.getFullYear());
                if(dateReturn.length < 2) dateReturn = '0' + dateReturn;
                if(monthReturn.length < 2) monthReturn = '0' + monthReturn;

                newCard.returnDate = (dateReturn + '.' + monthReturn + '.' + fullYearReturn);
                console.log('IdCard',newCard.id);
                let systemCardsNew = localStorage.getItem("cards");
                systemCardsNew = JSON.parse(systemCardsNew);
                for(let card of systemCardsNew){
                    if(card.id == newCard.id) card.returnDate = newCard.returnDate;
                }
                systemCardsNew = JSON.stringify(systemCardsNew);
                localStorage.setItem("cards",systemCardsNew);
                console.log(newCardReturnCell);
                newCardReturnCell.innerHTML = ""
                newCardReturnCell.textContent = (dateReturn + '.' + monthReturn + '.' + fullYearReturn);
                newCardReturnImg.remove(); 
            }

            newCardReturnCell.append(newCardReturnImg);
            newCardLine.append(newCardId,newCardVisitorCell,newCardBookCell,newCardBorrowCell,newCardReturnCell);
            cardTbody.append(newCardLine);

            let systemCards = localStorage.getItem("cards");
            if(systemCards != null){
                systemCards = JSON.parse(systemCards);
                systemCards.push(newCard);
            }
            else systemCards = [newCard];

            systemCards = JSON.stringify(systemCards);
            localStorage.setItem("cards",systemCards);
            console.log(localStorage.getItem("cards"));
            addCardDataWindow.style.display = "none";
        }
        else{
            if(!isBookInSystem) alert("Вашей книги нет в системе!");
            if(!isVisitorInSystem) alert("Такого Посетителя нет в системе!")
        }
    }
    else alert("Вы ввели данные не полностью!") // Вверх Объем + 77(Обхват), наверное А , 77А. S Джинсы 36
}

function getNewBookId(rowNames){
    let lastLine = document.getElementsByClassName(rowNames);
    if(lastLine.length != 0){
        lastLine = lastLine[lastLine.length - 1];
        let newId = parseInt(lastLine.children[0].textContent);
        return newId + 1;
    } 
    return document.getElementsByClassName(rowNames).length + 1;
}

function isUserBookInSystem(name,storageKey){
    let dataInfo = localStorage.getItem(storageKey);
    if(dataInfo != null){
        dataInfo = JSON.parse(dataInfo);
        for(let curData of dataInfo){
            if(curData.name == name) return true;
        }
    }
    return false;
}

btnAddNewBookConfirmation.onclick = function(){
    if(inputAddedBookName.value.length != 0){
        if(isUserBookInSystem(inputAddedBookName.value,"books")){
            alert("Такая книга уже есть в системе!")
            return
        }
        let newBook = {
            id:getNewBookId("book-line"),
            name:inputAddedBookName.value
        };

        let newBookLine = document.createElement("tr");
        newBookLine.className = "book-line";
        let newBookIdCell = document.createElement("td");
        let newBookNameCell = document.createElement("td");
        let newBookEditCell = document.createElement("td");
        let newBookBasketCell = document.createElement("td");

        newBookIdCell.textContent = newBook.id;
        newBookNameCell.textContent = newBook.name;

        let pencilEdit = document.createElement("img");
        let basketEdit = document.createElement("img");

        pencilEdit.className = "edit-book";
        pencilEdit.src = "pencil_two.png";
        pencilEdit.width = "30";
        pencilEdit.onclick = function(){
            editBookPanel.style.display = "flex";
            editBookPanelName.value = newBook.name;
            choosenBook = newBookLine; 
            choosenBookId = newBook.id;
            console.log('Created',choosenBook);
            console.log('Created',choosenBookId);
        }

        basketEdit.className = "delete-book";
        basketEdit.src = "delete_icon.png";
        basketEdit.width = "30";
        basketEdit.onclick = function(){
            choosenBook = newBookLine;
            newBookLine.remove();
            console.log(choosenBook)
            let allTheBooks = localStorage.getItem("books");
            console.log(localStorage.getItem("books"));
            if(allTheBooks != null){
                allTheBooks = JSON.parse(allTheBooks);
                for(let bookIndex = 0;bookIndex < allTheBooks.length;bookIndex++){
                    if(allTheBooks[bookIndex].id == newBook.id) allTheBooks.splice(bookIndex,1);
                }
                allTheBooks = JSON.stringify(allTheBooks);
            }
            localStorage.setItem("books",allTheBooks);
            console.log(localStorage.getItem("books"));
        }

        newBookEditCell.append(pencilEdit);
        newBookBasketCell.append(basketEdit);
        newBookLine.append(newBookIdCell,newBookNameCell,newBookEditCell,newBookBasketCell);
        bookTbody.append(newBookLine);
        let allTheBooks = localStorage.getItem("books");
        if(allTheBooks != null){
            allTheBooks = JSON.parse(allTheBooks);
            allTheBooks.push(newBook);
        }
        else{
            allTheBooks = [newBook];
        }
        allTheBooks = JSON.stringify(allTheBooks);
        localStorage.setItem("books",allTheBooks);
        console.log(localStorage.getItem("books"));
        addBookDataWindow.style.display = "none";
    }
    else alert("Вы не заполнели поле названия книги!");
}

function isUserNameCorrect(userName){
    if(userName.length == 0) return false;
    return true;
}

function getNewUserID(){
    let numberUserLines = document.getElementsByClassName("user-line");
    return numberUserLines.length + 1;
}

btnAddNewUserConfirmation.onclick = function(){
    console.log("Зашел")
    console.log(addedUserName.value,isUserNameCorrect(addedUserName.value))
    console.log(addedUserPhone.value,isCorrectPhone(addedUserPhone.value))
    if(!isUserNameCorrect(addedUserName.value) || !isCorrectPhone(addedUserPhone.value)){
        if(!isUserNameCorrect(addedUserName.value)) alert("Вы не заполнили Полное Имя!")
        if(!isCorrectPhone(addedUserPhone.value)) alert("Номер телефона не соответствует требованиям")
    }
    else{
        if(isUserBookInSystem(addedUserName.value,"users")){
            alert("Пользователь с таким именем уже существует!")
            return
        }
        console.log("WHAT?")
        let newUser = {
            id:getNewUserID(),
            name:addedUserName.value,
            phone:addedUserPhone.value
        };
        let userNewLine = document.createElement("tr");
        userNewLine.className = "user-line";
        let userCellID = document.createElement("td");
        let userCellName = document.createElement("td");
        let userCellPhone = document.createElement("td");
        let userCellEditPencil = document.createElement("td");
        let editPicturePencil = document.createElement("img");
        editPicturePencil.className = "edit-user";
        editPicturePencil.src = "pencil_two.png";
        editPicturePencil.width = "30";
        editPicturePencil.onclick = function(){
            editedUserId = newUser.id;
            userEditPage.style.display = "flex";
            namePart.value = newUser.name;
            phonePart.value = newUser.phone;
            userEditedRow = userNewLine;
        }

        userCellID.textContent = newUser.id;
        userCellName.textContent = newUser.name;
        userCellPhone.textContent = newUser.phone;
        userCellEditPencil.append(editPicturePencil);

        userNewLine.append(userCellID,userCellName,userCellPhone,userCellEditPencil);
        userTable.append(userNewLine);

        systemUsers = localStorage.getItem("users");
        if(systemUsers != null){
            systemUsers = JSON.parse(systemUsers);
            systemUsers.push(newUser);
        }
        else{
            systemUsers = [newUser]
        }
        systemUsers = JSON.stringify(systemUsers);
        localStorage.setItem("users",systemUsers);
        console.log(localStorage.getItem("users"));
        addUserDataWindow.style.display = "none";
    }
}

let searchInfoText = document.getElementsByClassName("interraction")[2],
searchBtn = document.getElementsByClassName("interraction")[3];

function isFoundRow(rowText,targetText){
    if(targetText.length == 0) return false
    return rowText.includes(targetText)
}

searchBtn.onclick = function(){
    console.log(order)
    if(order == 1){
        let foundUserLines = document.getElementsByClassName("user-line");
        for(let currentLine = 0;currentLine < foundUserLines.length;currentLine++){
            let lineChildren = foundUserLines[currentLine].children;
            userName = lineChildren[1].textContent;
            userPhoneNumber = lineChildren[2].textContent;
            if(isFoundRow(userName.toLowerCase(),searchInfoText.value.toLowerCase()) || isFoundRow(userPhoneNumber.toLowerCase(),searchInfoText.value.toLowerCase())){
                foundUserLines[currentLine].style.backgroundColor = "yellow";
                // console.log(isFoundRow(userName,searchInfoText.value),userName,searchInfoText.value)
                // console.log(isFoundRow(userPhoneNumber,searchInfoText.value),userPhoneNumber,searchInfoText.value)
            }
            else foundUserLines[currentLine].style.backgroundColor = "unset";
        }
    }
    else if(order == 0){
        let foundedBooksLines = document.getElementsByClassName("book-line");
        for(let curentLine = 0;curentLine < foundedBooksLines.length ; curentLine ++){
            let rowElements = foundedBooksLines[curentLine].children;
            let bookName = rowElements[1].textContent;
            if(isFoundRow(bookName.toLowerCase(),searchInfoText.value.toLowerCase())){
                foundedBooksLines[curentLine].style.backgroundColor = "orange";
            }
            else foundedBooksLines[curentLine].style.backgroundColor = "unset";
        }
    }
    else if(order == 2){
        let foundedCardsLines = document.getElementsByClassName("card-line");
        for(let currentLine = 0;currentLine < foundedCardsLines.length;currentLine++){
            let rowElements = foundedCardsLines[currentLine].children;
            let cardVisitorName = rowElements[1].textContent,
            cardBookName = rowElements[2].textContent,
            cardBorrowDate = rowElements[3].textContent;
            if(isFoundRow(cardVisitorName.toLowerCase(),searchInfoText.value.toLowerCase()) || isFoundRow(cardBookName.toLowerCase(),searchInfoText.value.toLowerCase()) || isFoundRow(cardBorrowDate.toLowerCase(),searchInfoText.value.toLowerCase())){
                foundedCardsLines[currentLine].style.backgroundColor = "green";
            }
            else foundedCardsLines[currentLine].style.backgroundColor = "unset";
        }
    }
    else if(order == 3){
        let foundedCardsLines = document.getElementsByClassName("best-books-line");
        for(let currentLine = 0;currentLine < foundedCardsLines.length ; currentLine++){
            let rowElements = foundedCardsLines[currentLine].children;
            let bookName = rowElements[1].textContent,
            bookNumberOfAppearance = rowElements[2].textContent;
            if(isFoundRow(bookName.toLowerCase(),searchInfoText.value.toLowerCase()) || isFoundRow(bookNumberOfAppearance,searchInfoText.value.toLowerCase())){
                foundedCardsLines[currentLine].style.backgroundColor = "pink";
            }
            else foundedCardsLines[currentLine].style.backgroundColor = "unset";
        } 
        foundedCardsLines = document.getElementsByClassName("best-visitors-line");
        for(let currentLine = 0;currentLine < foundedCardsLines.length ; currentLine++){
            let rowElements = foundedCardsLines[currentLine].children;
            let visitorName = rowElements[1].textContent,
            visitorNumberOfAppearance = rowElements[2].textContent;
            if(isFoundRow(visitorName.toLowerCase(),searchInfoText.value.toLowerCase()) || isFoundRow(visitorNumberOfAppearance,searchInfoText.value.toLowerCase())){
                foundedCardsLines[currentLine].style.backgroundColor = "coral";
            }
            else foundedCardsLines[currentLine].style.backgroundColor = "unset";
        } 
        
    }
}

let sortBtn = document.getElementsByClassName("interraction")[1];
function sortTable(table,tableLines,selectedOption){
    let tableRows = Array.from(document.getElementsByClassName(tableLines));
    let sortedRows = undefined;
    // console.log(tableRows);
    if(selectedOption.value == 'ID'){
        sortedRows = tableRows.sort((a,b) => {
            const aColText = (a.children)[0].textContent.trim();
            const bColText = (b.children)[0].textContent.trim();
            // console.log(aColText)
            // console.log(bColText)
            return aColText > bColText ? 1:-1;
        })
    }
    else if(selectedOption.value == 'Name' || selectedOption.value == 'Visitor name' || selectedOption.value == 'Book name' || selectedOption.value == 'Borrow date'){
        let columntIndex = undefined;
        if(selectedOption.value == 'Name' || selectedOption.value == 'Visitor name') columntIndex = 1;
        else if(selectedOption.value == 'Book name') columntIndex = 2;
        else if(selectedOption.value == 'Borrow date') columntIndex = 3;
        sortedRows = tableRows.sort((a,b) => {
            const aColText = (a.children)[columntIndex].textContent.trim();
            const bColText = (b.children)[columntIndex].textContent.trim();
            // console.log(aColText)
            // console.log(bColText)
            return aColText > bColText ? 1:-1;
        })
    }
    else if(selectedOption.value == 'Phone'){
        sortedRows = tableRows.sort((a,b) => {
            const aColText = (a.children)[2].textContent.trim();
            const bColText = (b.children)[2].textContent.trim();
            // console.log(aColText)
            // console.log(bColText)
            return aColText > bColText ? 1:-1;
        })
    }
    else if(selectedOption.value == 'Number of purchases'){
        sortedRows = tableRows.sort((a,b) => {
            const aColText = parseInt((a.children)[2].textContent.trim());
            const bColText = parseInt((b.children)[2].textContent.trim());
            return aColText > bColText ? 1:-1;
        })
    }
    while(document.getElementsByClassName("user-line").length != 0){
        document.getElementsByClassName("user-line")[0].remove();
    }
    document.getElementById(table).append(...sortedRows);
}
sortBtn.onclick = function(){
    if(order == 1) sortTable("user-table","user-line",document.getElementsByClassName("interraction")[0]);
    else if(order == 0) sortTable("book-table","book-line",document.getElementsByClassName("interraction")[0]);
    else if(order == 2) sortTable("card-table","card-line",document.getElementsByClassName("interraction")[0]);
    else if(order == 3){
        sortTable("best-books","best-books-line",document.getElementsByClassName("interraction")[0]);
        sortTable("best-visitors","best-visitors-line",document.getElementsByClassName("interraction")[0]);
    }
}
let navigatorItems = document.getElementsByClassName("nav-item"),
visitorBlock = document.querySelector(".main-info");

navigatorItems[1].onclick = function(){
    visitorBlock.style.display = "block";
    bookTable.style.display = "none";
    cardTable.style.display = "none";
    bestBooksTable.style.display = "none";
    bestVisitorTable.style.display = "none";
    userTable.style.display = "table";
    order = 1;
    infoHeader.children[0].textContent = "ALL VISITORS";
    infoHeader.children[1].style.display = "inline";
    infoHeader.children[1].textContent = "New visitor";
    selectionSortType.children[2].style.display = "block";
    selectionSortType.children[3].style.display = "none";
    selectionSortType.children[4].style.display = "none";
    selectionSortType.children[5].style.display = "none";
    selectionSortType.children[6].style.display = "none";
    bestVisitorTitle.style.display = "none";
    bestBooksTitle.style.display = "none";
    console.log(bestVisitorTitle)
    loadCustomerPartWindow();
}

let infoHeader = document.getElementById("info-header"),
bookTable = document.getElementById("book-table"),
selectionSortType = document.getElementsByClassName("interraction")[0],
bookTbody = document.getElementById("book-tbody"),
editBookPanel = document.getElementById("edit-book"),
addBookPanel = document.getElementById("add-book"),
choosenBook = undefined,
editBookPanelName = document.getElementById("edit-book-name"),
editBookPanelButtonSave = document.getElementById("btn-edit-book"),
choosenBookId = undefined;

editBookPanelButtonSave.onclick = function(){
    if(editBookPanelName.value.length != 0){
        console.log(choosenBook);
        console.log(choosenBookId);
        let choosenBookCells = choosenBook.children;
        choosenBookCells[1].textContent = editBookPanelName.value;
        let allTheUsers = localStorage.getItem("books");
        if(allTheUsers != null){
            allTheUsers = JSON.parse(allTheUsers);
            for(let curBook of allTheUsers){
                if(curBook.id == choosenBookId) curBook.name = editBookPanelName.value;
            }
            allTheUsers = JSON.stringify(allTheUsers);
            localStorage.setItem("books",allTheUsers);
        }
        editBookPanel.style.display = "none";
        console.log(localStorage.getItem("books"));
    }
    else alert("Заполните название книги!")
}

// // Delete

// book = {
//     id:'1',
//     name:"Assassin's creed"
// }
// bookTwo = {
//     id:'2',
//     name:"Art of love"
// }
// localStorage.setItem("books",JSON.stringify([book,bookTwo]));
// localStorage.clear()
// //

function loadBookPartWindow(){
    deleteTableInfoPart("book-line");

    let systemBooks = localStorage.getItem("books");
    if(systemBooks != null){
        systemBooks = JSON.parse(systemBooks);
        for(let bookIndex = 0; bookIndex < systemBooks.length; bookIndex++){
            let bookRow = document.createElement("tr");
            bookRow.className = "book-line";
            let bookIdCell = document.createElement("td");
            let bookNameCell = document.createElement("td");
            let bookEditCell = document.createElement("td");
            let bookDeleteCell = document.createElement("td");

            let editPencil = document.createElement("img");
            let deleteBasket = document.createElement("img");

            editPencil.className = "edit-book";
            editPencil.src = "pencil_two.png";
            editPencil.width = "30";

            deleteBasket.className = "delete-book";
            deleteBasket.src = "delete_icon.png";
            deleteBasket.width = "30";

            editPencil.onclick = function(){
                editBookPanel.style.display = "flex";
                choosenBook = bookRow;
                editBookPanelName.value = systemBooks[bookIndex].name;
                choosenBookId = systemBooks[bookIndex].id;
                console.log(choosenBook);
                console.log(editBookPanelName.value);
                console.log(choosenBookId);
            }

            deleteBasket.onclick = function(){
                console.log(bookRow);
                choosenBook = bookRow;
                console.log(choosenBook)
                choosenBookId = systemBooks[bookIndex].id;
                bookRow.remove();  
                systemBooks.splice(bookIndex,1);
                console.log(choosenBookId);
                systemBooks = JSON.stringify(systemBooks);
                localStorage.setItem("books",systemBooks);
                console.log(localStorage.getItem("books"));
            }

            bookEditCell.append(editPencil);
            bookDeleteCell.append(deleteBasket);
            bookIdCell.textContent = systemBooks[bookIndex].id;
            bookNameCell.textContent = systemBooks[bookIndex].name;
            bookRow.append(bookIdCell,bookNameCell,bookEditCell,bookDeleteCell);
            bookTbody.append(bookRow);
        }
    }
}

navigatorItems[0].onclick = function(){
    userTable.style.display = "none";
    cardTable.style.display = "none";
    visitorBlock.style.display = "block";
    bestBooksTable.style.display = "none";
    bestVisitorTable.style.display = "none";
    bookTable.style.display = "table";
    order = 0;
    infoHeader.children[0].textContent = "ALL BOOKS";
    infoHeader.children[1].textContent = "New book";
    infoHeader.children[1].style.display = "inline";
    selectionSortType.children[2].style.display = "none";
    selectionSortType.children[3].style.display = "none";
    selectionSortType.children[4].style.display = "none";
    selectionSortType.children[5].style.display = "none";
    selectionSortType.children[6].style.display = "none";
    selectionSortType.value = "ID";
    bestVisitorTitle.style.display = "none";
    bestBooksTitle.style.display = "none";
    loadBookPartWindow();
}

// Card Part
//Delete
// let trialBookOne = {
//     id:'1',
//     visitorName:'Maratuly Temirbolat',
//     bookName:'JS Part 1',
//     borrowDate:'12.01.2019'
// }

// let trialBookTwo = {
//     id:'2',
//     visitorName:'Assanali Moldash',
//     bookName:'JS Part 2',
//     borrowDate:'20.03.2020'
// }

// localStorage.setItem("cards",JSON.stringify([trialBookOne,trialBookTwo]))
// localStorage.clear()
//
function loadCardPartWindow(){
    deleteTableInfoPart("card-line");

    let systemCards = localStorage.getItem("cards");
    if(systemCards != null){
        systemCards = JSON.parse(systemCards);
        for(let cardIndex = 0; cardIndex < systemCards.length; cardIndex++){
            let cardRow = document.createElement("tr");
            cardRow.className = "card-line";
            let cardId = document.createElement("td");
            let cardVisitorName = document.createElement("td");
            let cardBookName = document.createElement("td");
            let cardBorrowDate = document.createElement("td");
            let cardReturnDate = document.createElement("td");
            
            
            let returnImage = document.createElement("img");
            returnImage.className = "return-book";
            returnImage.src = "return_icon.png";
            returnImage.width = "30";
            returnImage.onclick = function(){
                let returnDate = new Date(),dateReturn = String(returnDate.getDate()),
                monthReturn = String(returnDate.getMonth() + 1),
                fullYearReturn = String(returnDate.getFullYear());
                if(dateReturn.length < 2) dateReturn = '0' + dateReturn;
                if(monthReturn.length < 2) monthReturn = '0' + monthReturn;
                systemCards[cardIndex].returnDate = dateReturn + '.' +monthReturn + '.' + fullYearReturn;
                
                systemCards = JSON.stringify(systemCards);
                localStorage.setItem("cards",systemCards);

                cardReturnDate.innerHTML = "";
                cardReturnDate.textContent = dateReturn + '.' +monthReturn + '.' + fullYearReturn;
                returnImage.remove();
            }
            console.log(systemCards[cardIndex].returnDate)
            cardId.textContent = systemCards[cardIndex].id;
            cardVisitorName.textContent = systemCards[cardIndex].visitorName;
            cardBookName.textContent = systemCards[cardIndex].bookName;
            cardBorrowDate.textContent = systemCards[cardIndex].borrowDate;
            if(systemCards[cardIndex].returnDate == '') cardReturnDate.append(returnImage);
            else cardReturnDate.textContent = systemCards[cardIndex].returnDate;
            // cardReturnDate.append(returnImage);
            cardRow.append(cardId,cardVisitorName,cardBookName,cardBorrowDate,cardReturnDate);
            cardTbody.append(cardRow);
        }
    }
    console.log("Cards Loaded Finished");
}

let cardTable = document.getElementById("card-table"),
cardTbody = document.getElementById("card-tbody"),
bestVisitorTitle = document.getElementById("top-visitors-title"),
bestBooksTitle = document.getElementById("top-books-title");

navigatorItems[2].onclick = function(){
    userTable.style.display = "none";
    visitorBlock.style.display = "block";
    bookTable.style.display = "none";
    bestBooksTable.style.display = "none";
    bestVisitorTable.style.display = "none";
    cardTable.style.display = "table";
    order = 2;
    infoHeader.children[0].textContent = "ALL CARDS";
    infoHeader.children[1].style.display = "inline";
    infoHeader.children[1].textContent = "New card";
    selectionSortType.children[1].style.display = "none";
    selectionSortType.children[2].style.display = "none";
    selectionSortType.children[3].style.display = "block";
    selectionSortType.children[4].style.display = "block";
    selectionSortType.children[5].style.display = "block";
    selectionSortType.children[6].style.display = "none";
    selectionSortType.value = "ID";
    bestVisitorTitle.style.display = "none";
    bestBooksTitle.style.display = "none";

    loadCardPartWindow()
}

// Statistics Part

function getIdByFullName(name,key){
    let allTheInfo = localStorage.getItem(key);
    if(allTheInfo != null){
        allTheInfo = JSON.parse(allTheInfo);
        for(let curInfo of allTheInfo){
            if(curInfo.name == name) return curInfo.id;
        }
    }
    return null;
}

function loadStatisticsPartWindow(){
    deleteTableInfoPart("best-books-line");
    deleteTableInfoPart("best-visitors-line");
    let cardsInfo = localStorage.getItem("cards");
    if(cardsInfo != null){
        cardsInfo = JSON.parse(cardsInfo);
        bestVisitorsMap = new Map([...bestVisitorsMap.entries()].sort((a,b) => b[1] - a[1]));
        bestBooksMap = new Map([...bestBooksMap.entries()].sort((a,b) => b[1] - a[1]));
        console.log(bestVisitorsMap)
        console.log(bestBooksMap)

        let maxTableRows = undefined;
        if(bestVisitorsMap.length > 5) maxTableRows = 5;
        else maxTableRows = bestVisitorsMap.length;

        let currentNumber = 1;
        for(let [mapKey,mapValue] of bestVisitorsMap.entries()){
            if(currentNumber <= 5){
                let bestVisitorsRow = document.createElement("tr"),
                bestVisitorsIdCell = document.createElement("td"),
                bestVisitorsNameCell = document.createElement("td"),
                bestVisitorAppearanceCell = document.createElement("td");

                bestVisitorsIdCell.textContent = getIdByFullName(mapKey,"users");
                bestVisitorsNameCell.textContent = mapKey;
                bestVisitorAppearanceCell.textContent = mapValue;

                bestVisitorsRow.className = "best-visitors-line";
                bestVisitorsRow.append(bestVisitorsIdCell,bestVisitorsNameCell,bestVisitorAppearanceCell);
                bestVisitorTbody.append(bestVisitorsRow);
            }
            currentNumber++;
        }

        if(bestBooksMap.length > 5) maxTableRows = 5;
        else maxTableRows = bestBooksMap.length;
        currentNumber = 1;
        for(let [mapKey,mapValue] of bestBooksMap.entries()){
            if(currentNumber <= 5){
                let bestBookRow = document.createElement("tr"),
                bestBookIdCell = document.createElement("td"),
                bestBookNameCell = document.createElement("td"),
                bestBookAppearanceCell = document.createElement("td");

                bestBookRow.className = "best-books-line";
                bestBookIdCell.textContent = getIdByFullName(mapKey,"books");
                bestBookNameCell.textContent = mapKey;
                bestBookAppearanceCell.textContent = mapValue;

                bestBookRow.append(bestBookIdCell,bestBookNameCell,bestBookAppearanceCell);
                bestBookTbody.append(bestBookRow);
            }
            currentNumber++;
        }
        
    }
    console.log("Statistics is loaded successfully")
}

let bestBooksTable = document.getElementById("best-books"),
bestVisitorTable = document.getElementById("best-visitors"),
bestVisitorTbody = document.getElementById("best-visitors-tbody"),
bestBookTbody = document.getElementById("best-books-tbody");

navigatorItems[3].onclick = function(){
    userTable.style.display = "none";
    visitorBlock.style.display = "block";
    bookTable.style.display = "none";
    cardTable.style.display = "none";
    bestBooksTable.style.display = "table";
    bestVisitorTable.style.display = "table";
    order = 3;
    infoHeader.children[0].textContent = "ALL STATISTICS";
    infoHeader.children[1].style.display = "none";
    selectionSortType.children[1].style.display = "block";
    selectionSortType.children[2].style.display = "none";
    selectionSortType.children[3].style.display = "none";
    selectionSortType.children[4].style.display = "none";
    selectionSortType.children[5].style.display = "none";
    selectionSortType.children[6].style.display = "block";
    bestVisitorTitle.style.display = "block";
    bestBooksTitle.style.display = "block";
    selectionSortType.value = "ID";
    loadStatisticsPartWindow()

}
