let divStorage = document.getElementById("main-part");
let url = "https://jsonplaceholder.typicode.com/users";
let xhr = new XMLHttpRequest();

divStorage.innerHTML = '';
xhr.open("GET",url);
xhr.send()

xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        let data = JSON.parse(xhr.response);
        for(let item of data){
            let personalContainer = document.createElement("div");
            let idPart = document.createElement("h3");
            idPart.textContent = "ID: " + item.id;
            let namePart = document.createElement("p");
            namePart.textContent = "Full Name: " + item.name;
            let emailPart = document.createElement("p");
            emailPart.textContent = "Email: " + item.email;
            let addressPart = document.createElement("p");
            addressPart.textContent = "Address: " + item.address.street + ' ' + item.address.suite + ' ' + item.address.city + ' ' + item.address.zipcode;
            let phoneNumber = document.createElement("p");
            phoneNumber.textContent = "Phone: " + item.phone;
            let additionalInfo = document.createElement("p");
            additionalInfo.textContent = "Website: " + item.website;
            let workPart = document.createElement("p");
            workPart.textContent = "Company: " + item.company.name + ' ' + item.company.catchPhrase + ' ' + item.company.bs;
            personalContainer.append(idPart,namePart,emailPart,addressPart,phoneNumber,additionalInfo,workPart);
            divStorage.append(personalContainer);
        }
    }
}