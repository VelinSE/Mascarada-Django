$(document).ready(function () {
    var minDate = new Date('01 Jan 1970 00:00:00 GMT');
    $('.datepicker').datepicker({'format': 'yyyy-mm-dd', 'minDate': minDate, 'yearRange' : [minDate.getFullYear(), new Date(Date.now()).getFullYear()] });
    $('#id_birth_date').on('click', function() {
        $('.datepicker-modal').css('display', 'table');
    });

})