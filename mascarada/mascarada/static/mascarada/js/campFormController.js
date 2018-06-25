$(document).ready(function () {
    
    $('select').formSelect()
    var single = M.FormSelect.getInstance($('#single'));
    var multiple = M.FormSelect.getInstance($('#multiple'));

    $('#single').on('change', function() {
        $('#multiple').prop('selectedIndex', 0);
        $('#multiple').formSelect();

        single = M.FormSelect.getInstance($('#single'));
        multiple = M.FormSelect.getInstance($('#multiple'));

        for(elem in multiple.dropdownOptions.children) {
            if(!isNaN(parseInt(multiple.dropdownOptions.children[elem].textContent))) {
                
                var spot = multiple.dropdownOptions.children[elem].textContent.trim();
                var spotJSON = ($('#camp_' + spot).val());
                spotJSON = JSON.parse(spotJSON.replace(/'/g, '"'));

                if(($(single.input).val() != parseInt(spotJSON.free_beds, 10)) && (spotJSON != undefined))
                {
                    $(multiple.dropdownOptions.children[elem]).hide();
                }
                else {
                    $(multiple.dropdownOptions.children[elem]).show();
                }
            }
        }
    })

    $('select').on('change', function() {
        if($(single.input).val() != undefined && $(this)[0].id != 'id_visitor_email')
        {
            if($('#id_tent_size').val() == 0)
            {
                $('#price').text(($(single.input).val() * 30) + '€');
            }
            else {
                $('#price').text(($(single.input).val() * 30) + ($('#id_tent_size').val() * 7.5) + 10 + '€');
            }
            
        }
    })
})