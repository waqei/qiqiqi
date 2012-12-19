// JavaScript Document
function GetUname(){
	var oBao = new ActiveXObject("Microsoft.XMLHTTP");
	var my_url="/User/GetUname.asp";
	oBao.open("POST",my_url,false);
	oBao.send(null);
	var strResult = unescape(oBao.responseText);
	return strResult;
}