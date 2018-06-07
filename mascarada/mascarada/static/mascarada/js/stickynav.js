$(document).ready(function() {
    $('#stickypoint').waypoint(function(direction) {
        if(direction == 'down') {
            $('#home-nav').fadeOut(300);
            $('#main-nav').slideDown(200);
            $('#main-nav').removeClass('no-display');
        } else if(direction == 'up') {
           // $('#home-nav').removeClass('no-display');
            $('#home-nav').fadeIn(300);
            $('#main-nav').slideUp(100);
            
        }
        console.log("asda");
    }, {
        offset: '120px'
    })

    
})