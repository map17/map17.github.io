var iPad=false;
if (navigator.appVersion.indexOf("iPad")!=-1) iPad=true;


function pop( fileIndex ) {
    if ( iPad ) {

	document.write( '<object width=100% height=100% type="text/html" data="' + fileIndex + '" ></object>' );
	
    }
    else {
	document.getElementById( 'TheModalContent' ).innerHTML = '<object width=100% height=100% type="text/html" data="' + fileIndex + '" ></object>';
    
	$("body").css("overflow", "hidden");
	document.getElementById( 'TheModal' ).style.display = 'block';
	document.getElementById( 'TheModal' ).style.overflow = 'scroll';
    }
}

function hide() {
    if ( iPad ) {

	location.replace( "../../index.html" );
	//window.location.href = "../../index.html";
	//window.history.back();
	
    }
    else {
	document.getElementById( 'TheModal' ).style.display = 'none';
	$("body").css("overflow", "scroll");
    }
}
