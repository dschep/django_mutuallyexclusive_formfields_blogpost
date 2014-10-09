$(document).ready(function() {
    $('#id_test_field1,#id_test_field2').each(function(i, e) {
        $('<input name="test_field" type="radio" value="'+i+'">')
            .insertBefore(e)
            .click(function() {
                $('#id_test_field1,#id_test_field2').attr('disabled', 'disabled');
                $(e).removeAttr('disabled');
            })
            .next('#id_test_field1').prev().click();
    });
});
