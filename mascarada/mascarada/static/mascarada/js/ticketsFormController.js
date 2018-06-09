$(document).ready(function () {
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd'});
    $('#id_birth_date').on('click', function() {
        $('.datepicker-modal').css('display', 'table');
    });

   
})