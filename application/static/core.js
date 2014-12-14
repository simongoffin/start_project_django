
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$( document ).ready(function() {
    $( ".run_js" ).on( "click", function() {
        var xx = parseInt($('.x_val').val());
        var yy = parseInt($('.y_val').val());
        if(xx && yy){
            var zz = xx+yy;
            $('.solution').text(xx+'+'+yy+'='+zz);
        }
        else{
            $('.solution').text('Bad value');
        }
    });
    $( ".clear_js" ).on( "click", function() {
        $('.x_val').val('');
        $('.y_val').val('');
        $('.solution').text('');
    });
    $( ".ajax" ).on( "click", function() {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type: "POST",
            url: "/application/hello/",
            data: { name: $('.name').val(), csrfmiddlewaretoken: csrftoken},
        })
        .done(function( data ) {
            window.location.href ='/application/confirmation/';
            console.log(data['message']);
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            console.log('Finish');
        });
    });
    $('#Test').modal('show');
    $( ".ok" ).on( "click", function() {
        window.location.href ='/application/home/';
    });
});