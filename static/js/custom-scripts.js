
$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});
var nyTime = new Date().toLocaleString("en-US", {timeZone: "America/New_York"});
var today = new Date(nyTime);

var clock = $('.us-clock').FlipClock(today, {
    clockFace: 'TwelveHourClock'
});



$(document).ready(function() {


    $('select').formSelect();

    $('.sidenav').sidenav();

    $('.modal').modal();

    $('.fixed-action-btn').floatingActionButton();



});


