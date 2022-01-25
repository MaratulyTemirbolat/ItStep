var logo = document.getElementById('logo');
window.onscroll = function(){
    var scroll = window.pageYOffset;
    console.log(scroll/window.innerHeight);
    logo.style.transform = 'translate(-50%, -' + 200*scroll/window.innerHeight + '%)'
}