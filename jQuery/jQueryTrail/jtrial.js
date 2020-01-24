$('#main h1').css('background-color', 'red');
// $('.special').addClass('background');
$('p[class]').addClass('background');

$(document).ready(function(){
    $('a[href="#"]').addClass('link');
    $('a[href!="#"]').addClass('font-size');
    $('a[href^=http]').addClass('external');
    $('a[href$=org]').addClass('org');

    $('.first li:first').css('font-size', '30px')
    $('.first li:last').html('I am the last')

    $('.second li:even').addClass('even')
    $('.second li:odd').addClass('odd')

    $('.third li:eq(2)').hide()
    $('.second li:lt(2)').css('font-size', '40px')
    $('.second li:gt(2)').css('background-color', 'green')

    $('div .chain').hide(2000).html('I am a code Addict').addClass('border').show(2000)
})