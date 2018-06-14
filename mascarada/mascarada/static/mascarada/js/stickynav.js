$(document).ready(function() {
    $('#stickypoint').waypoint(function(direction) {
        if(direction == 'down') {
            $('#home-nav').fadeOut(300);
            $('#main-nav').slideDown({'duration': 200, 'start' : function() {
                    $('#main-nav').css('display', 'flex');
                    $('#main-nav').removeClass('no-display');
                }
            });
            
        } else if(direction == 'up') {
            $('#home-nav').fadeIn(300);
            $('#main-nav').slideUp(100);
        }
    }, {
        offset: '120px'
    })

    
})