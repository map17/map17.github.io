
function pop( fileIndex ) {
    document.getElementById( 'TheModalContent' ).innerHTML = '<object width=100% height=100% type="text/html" data="' + fileIndex + '" ></object>';
    
    document.getElementById( 'TheModal' ).style.display = 'block';
    $("body").css("overflow", "hidden");
}

function hide() {
    document.getElementById( 'TheModal' ).style.display = 'none';
    $("body").css("overflow", "scroll");
}
