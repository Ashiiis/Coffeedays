// function incrementValue(e) {
//     e.preventDefault();
//     var fieldName = $(e.target).data('field');
//     var parent = $(e.target).closest('div');
//     var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
  
//     if (!isNaN(currentVal)) {
//       parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
//     } else {
//       parent.find('input[name=' + fieldName + ']').val(0);
//     }
//   }
  
//   function decrementValue(e) {
//     e.preventDefault();
//     var fieldName = $(e.target).data('field');
//     var parent = $(e.target).closest('div');
//     var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
  
//     if (!isNaN(currentVal) && currentVal > 0) {
//       parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
//     } else {
//       parent.find('input[name=' + fieldName + ']').val(0);
//     }
//   }
  
//   $('.input-group').on('click', '.button-plus', function(e) {
//     incrementValue(e);
//   });
  
//   $('.input-group').on('click', '.button-minus', function(e) {
//     decrementValue(e);
//   });
let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
};

window.onscroll = () => {
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
};

document.querySelectorAll('.image-slider img').forEach(images => {
    images.onclick = () => {
        var src = images.getAttribute('src');
        document.querySelector('.main-home-image').src = src;
    };
});

var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    grabCursor: true,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1
        },
        768: {
            slidesPerView: 2
        }
    },
});