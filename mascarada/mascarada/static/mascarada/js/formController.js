$(document).ready(function () {
    $(':text, :password, [type="email"]').on('ready', function () {
        console.log("asdf");
        if($(this).val() == "" && $(this).attr('id') != 'dob') {
            $("label[for='" + $(this).attr('id') + "']").removeClass('active');
        }
    })

    $(':text, :password, [type="email"]').on('focus', function () {
        if ($(this).attr('id') != 'dob') {
            $("label[for='" + $(this).attr('id') + "']").addClass('active');
        }
    })

    $(':text, :password, [type="email"]').on('focusout', function () {
        if ($(this).val() == "" && $(this).attr('id') != 'dob') {
            $("label[for='" + $(this).attr('id') + "']").removeClass('active');
        }
    })

    
})
