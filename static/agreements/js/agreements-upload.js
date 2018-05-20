



$( document ).ready(function() {
     $('.upload-file').change(function() {
        form_id = $(this).attr('data-form');
        console.log(form_id);
        $("#"+form_id).submit();
    });
});