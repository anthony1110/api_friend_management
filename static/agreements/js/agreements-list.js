

$( document ).ready(function() {
    $('.filter').keypress(function (e) {
        if (e.which == 13) {
            console.log('plop');
            $('form#search').submit();
            return false;
        }
    });
});