jQuery(function($) {
    $('div.inline-group').sortable({
        /*containment: 'parent',
        zindex: 10, */
        items: 'div.inline-related',
        handle: 'h3:first'
    });
    $('div.inline-related h3').css('cursor', 'move');
    // $('div.inline-related').find('input[id$=order]').parent('div').hide();
    $('#menu_form').submit(function() {
        $('div.inline-group > div.inline-related').each(function(i) {
            if ($(this).find('input[id$=name]').val()) {
                $(this).find('input[id$=order]').val(i+1);
            }
        });
    });
});