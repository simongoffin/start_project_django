
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
    var progressBar;
    var percent = 0;
    progressBar = new ProgressBar("results", {'width':'250px', 'height':'25px'});
    progressBar.setPercent(percent);
    $( ".ajax" ).on( "click", function() {
            var csrftoken = getCookie('csrftoken');
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/load/progress/",
                data: { state: percent, csrfmiddlewaretoken: csrftoken},
            })
            .done(function( data ) {
                percent = data['state'];
                progressBar.setPercent(percent);
            })
            .fail(function() {
                alert( "error" );
            })
            .always(function() {
                if(percent == 100){
                    percent = 0;
                    progressBar.setPercent(percent);
                    console.log('Finish');
                }
            });
    });
});