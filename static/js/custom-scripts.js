
$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});




$(document).ready(function() {

    $('#dataTable').dataTable({
        paging: false,
        searching: false
    });

    $('select').formSelect();

    $('.sidenav').sidenav();

    $('.modal').modal();

    $('.fixed-action-btn').floatingActionButton();



});


