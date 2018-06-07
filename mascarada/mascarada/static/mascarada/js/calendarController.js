$(document).ready(function () {
    $('#dob').each(function () {
        $(this).datepicker();
    })

    $('.gj-icon').on('click', function () {
        if ($(this).css('color') == 'rgb(66, 133, 244)') {
            $(this).css('color', 'rgba(0, 0, 0, 0.87)');
        } else {
            $(this).css('color', 'rgb(66, 133, 244)');
        }

    })
})

