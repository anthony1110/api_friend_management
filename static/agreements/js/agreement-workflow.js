$( document ).ready(function() {
    $('.task-button').click(function (e) {
        var url = $( this ).attr('data-url');
        $("#task-form").attr('action', url);
        $("#task-form").submit();
    });
});