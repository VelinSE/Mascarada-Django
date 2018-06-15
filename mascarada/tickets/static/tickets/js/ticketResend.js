$(document).ready(function(){
    $('.ticket-resend').on('click' ,function(event){
        $(event.target).prop('disabled', true);
        $(event.target).html('EMAIL SENT!');
        resendTicket(event.target.id)
    })
    
    function resendTicket(visitorId){
        console.log(visitorId)
        $.ajax({
            type: "POST",
            url: '/tickets/resend-ticket/',
            data: { 'visitorId' : visitorId },
            success: function(data){
                button = $('#' + visitorId) 
                button.prop('disabled', false);
                button.html('SEND TO EMAIL');
            }
          });
    }
})

