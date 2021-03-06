function readMore(){
    var dots = document.getElementById("dots");
    var more = document.getElementById("more");
    var btndrop = document.getElementById("btndrop");
    var icon = document.getElementsByClassName("fa fa-plus-circle");

    if(more.style.display === 'inline') {
        more.style.display = 'none';
        icon.classList.remove("fa fa-plus-circle");
        icon.classList.add("fa fa-minus-circle");
    } else {
        more.style.display = 'inline';
    }
}

function readMore2(){
    var dots2 = document.getElementById("dots2");
    var more2 = document.getElementById("more2");
    var btndrop2 = document.getElementById("btndrop2");

    if(more2.style.display === 'inline') {
        more2.style.display = 'none';
    } else {
        more2.style.display = 'inline';
    }
}

function readMore3(){
    var dots3 = document.getElementById("dots3");
    var more3 = document.getElementById("more3");
    var btndrop3 = document.getElementById("btndrop3");

    if(more3.style.display === 'inline') {
        more3.style.display = 'none';
    } else {
        more3.style.display = 'inline';
    }
}