let mainContainer = document.getElementById("main");
let url = "https://reqres.in/api/unknown";
let xhr = new XMLHttpRequest();

mainContainer.innerHTML = "";

xhr.open("GET",url);
xhr.send()

xhr.onreadystatechange = function(){
    if(xhr.readyState == 4 && xhr.status == 200){
        let data = JSON.parse(xhr.response);
        console.log(data);
        for(let color of data.data){
            let blockColor = document.createElement("div");
            blockColor.style.width = "150px";
            blockColor.style.height = "70px";
            blockColor.style.margin = "10px";
            blockColor.style.backgroundColor = `${color.color}`;
            let colorBlockName = document.createElement("p");
            colorBlockName.textContent = color.name;
            colorBlockName.style.fontSize = "20px";
            colorBlockName.style.color = "white";
            colorBlockName.style.textTransform = "capitalize";
            blockColor.append(colorBlockName);
            colorBlockName.style.textAlign = "center";
            mainContainer.append(blockColor);
        }
    }
}


