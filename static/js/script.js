function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

// const forms = document.querySelector('form[name=filter]');
//
// forms.addEventListener('submit', function (e) {
//     // Получаем данные из формы
//     e.preventDefault();
//     let url = this.action;
//     let params = new URLSearchParams(new FormData(this)).toString();
//     ajaxSend(url, params);
// });

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output;
}

let html = '\
{{#movies}}\
    <div class="col-md-4 product-men">\
        <div class="product-shoe-info editContent text-center mt-lg-4">\
            <div class="men-thumb-item">\
                <img src="media/{{ poster }}" class="img-fluid" alt="">\
            </div>\
            <div class="item-info-product">\
                <h4 class="">\
                    <a href="/{{ url }}" class="editContent">{{ title }}</a>\
                </h4>\
                <div class="product_price">\
                    <div class="grid-price">\
                        <span class="money editContent">{{ tagline }}</span>\
                    </div>\
                </div>\
                <ul class="stars">\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
                    <li><a href="#"><span class="fa fa-star-o" aria-hidden="true"></span></a></li>\
                </ul>\
            </div>\
        </div>\
    </div>\
{{/movies}}'

//button
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

//add rating
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e){
    //получение данных из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен")
        .catch(error => alert("При попытке установить рейтинг произошла ошибка")))
});

function xd(){
    // let a = document.getElementsByName("language")[0].children;
    // for (let i = 0; i < a.length; i++) {
    //     if (location.pathname === "/" + a[i].value + "/"){
    //         document.getElementsByClassName("editContent")[0].click();
    //     }
    // }
}