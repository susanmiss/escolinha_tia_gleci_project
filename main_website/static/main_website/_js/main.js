/* -------------------Carousel Divs----------------------*/

function moveToSelected(element) {

  if (element == "next") {
    var selected = $(".selected").next();
  } else if (element == "prev") {
    var selected = $(".selected").prev();
  } else {
    var selected = element;
  }

  var next = $(selected).next();
  var prev = $(selected).prev();
  var prevSecond = $(prev).prev();
  var nextSecond = $(next).next();

  $(selected).removeClass().addClass("selected");

  $(prev).removeClass().addClass("prev");
  $(next).removeClass().addClass("next");

  $(nextSecond).removeClass().addClass("nextRightSecond");
  $(prevSecond).removeClass().addClass("prevLeftSecond");

  $(nextSecond).nextAll().removeClass().addClass('hideRight');
  $(prevSecond).prevAll().removeClass().addClass('hideLeft');

}



$('#carousel div').click(function() {
  moveToSelected($(this));
});

$('.btn_right').click(function() {
  moveToSelected('next');
});

$('.btn_left').click(function() {
  moveToSelected('prev');
});

/* ---------------Menu Buttons---------------------*/

function openMenu(){
    document.getElementById("myDropdown").style.display = "block";
  }

function closeMenu(){
   document.getElementById("myDropdown").style.display = "none";
}

/*----------------Form Button---------------------*/
function sendForm(){
  alert("Sua solicitação de mantrícula foi enviada. Em breve entraremos em contato! :)")
}

/*---------------Making IMG big, School page------*/
