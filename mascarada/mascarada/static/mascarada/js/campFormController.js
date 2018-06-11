$(document).ready(function () {
    
    $('select').formSelect()

    

    $('#single').on('change', function() {
        $('#multiple').prop('selectedIndex', 0);
        $('#multiple').formSelect();

        var select = M.FormSelect.getInstance($('#single'));
        var multiple = M.FormSelect.getInstance($('#multiple'));

        for(elem in multiple.dropdownOptions.children) {
            if(!isNaN(parseInt(multiple.dropdownOptions.children[elem].textContent))) {
                
                var spot = multiple.dropdownOptions.children[elem].textContent.trim();
                var spotJSON = ($('#camp_' + spot).val());
                spotJSON = JSON.parse(spotJSON.replace(/'/g, '"'));

                if(($(select.input).val() != parseInt(spotJSON.free_beds, 10)) && (spotJSON != undefined))
                {
                    $(multiple.dropdownOptions.children[elem]).hide();
                }
                else {
                    $(multiple.dropdownOptions.children[elem]).show();
                }
            }
        }
    })
})