let lineItems = document.getElementsByTagName("li");
let counter = 0;
let visitedIndexes = []
let lastPlaceIndex = undefined;
for(let itemIndex = 0;itemIndex <lineItems.length;itemIndex++){
    lineItems[itemIndex].onclick = function(){
        visitedIndexes.push(itemIndex);
        if(counter > 0){
            lastPlaceIndex = visitedIndexes.shift();
            lineItems[lastPlaceIndex].style.backgroundColor = "unset";
        }
        lineItems[itemIndex].style.backgroundColor = "orange";
        counter ++;
    }
}