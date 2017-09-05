
function pop( fileIndex ) {
    document.getElementById( 'TheModalContent' ).innerHTML = '<object width=100% height=100% type="text/html" data="' + fileIndex + '" ></object>';
    
    $("body").css("overflow", "hidden");
    document.getElementById( 'TheModal' ).style.display = 'block';
    document.getElementById( 'TheModal' ).style.overflow = 'scroll';
}

function hide() {
    document.getElementById( 'TheModal' ).style.display = 'none';
    $("body").css("overflow", "scroll");
}
