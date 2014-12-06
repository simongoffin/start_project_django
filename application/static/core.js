
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
});