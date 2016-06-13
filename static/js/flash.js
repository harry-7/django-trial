
function showAlert(){
	var d = document.getElementsByClassName("flash-message");
	if (d.length == 0)return;
	d[0].className += " fadein";
}

window.setTimeout(function () {
    showAlert();
}, 3000);

