$(document).ready(function () {
    var repeatable =  $("#repeatable").clone();
    $("#numTickets").on("change", function () {
        $("#repeatablesContainer").empty();
        for(var i = 0; i < $("#numTickets").val(); i++) {
            repeatable.clone().appendTo("#repeatablesContainer");
            console.log($("#repeatable"));
        }
    })
    
})