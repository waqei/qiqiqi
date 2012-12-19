/*
Copyright 2010, Yimai Inc
MIT Licensed
build: 2011-1-23
by: liu <roccoliu@gmail.com>
*/

/* 图片轮换 */
$(function () {
    var len = $(".num > li").length;
    var index = 0;
    var adTimer;
    $(".num li").mouseover(function () {
        index = $(".num li").index(this);
        showImg(index);
    }).eq(0).mouseover();
    $('.slider').hover(function () {
        clearInterval(adTimer);
    }, function () {
        adTimer = setInterval(function () {
            showImg(index)
            index++;
            if (index == len) {
                index = 0;
            }
        }, 4000);
    }).trigger("mouseleave");
})

function showImg(index) {
    var adHeight = $(".slider").height();
    $(".picture").stop(true, false).animate({
        top: -adHeight * index
    }, 500);
    $(".num li").removeClass("on").eq(index).addClass("on");
}

/* 标签切换 */
$(function () {
    var $div_li = $("ul.tab-t li");
    $div_li.mouseover(function () {
        $(this).addClass("selected").siblings().removeClass("selected");
        var index = $div_li.index(this);
        $("#tabCnt .tab-c").eq(index).show().siblings().hide();
    })
})

/* 搜索切换 */
$(function () {
    var $div_li = $("ul.indser li");
    $div_li.click(function () {
        $(this).addClass("current").siblings().removeClass("current");
		//alert($(this).attr('tit'));
		$("#mSearch").attr("value",$(this).attr('tit'));
		$("#searchPanel").attr("action",$(this).attr('ac'));
		//$("ul.indser li b").show().siblings().hide();
    })
})

/* 搜索框 */
$(function () {
    $("#mSearch").click(function () {
		$(this).attr("value",'');
    })
});

/* 搜索切换 */
$(function () {
    var $div_li = $("div.category-main > div");
    $div_li.mouseover(function () {
        $(this).addClass("category-item-hover").siblings().removeClass("category-item-hover");
    })
	$div_li.mouseout(function () {
        $(this).removeClass("category-item-hover");
    })
});

/* 信息翻屏 */
(function($){
	$.fn.extend({
	Scroll:function(opt,callback){
	if(!opt) var opt={};
	var _btnUp = $("#"+ opt.up);//Shawphy:向上按钮
	var _btnDown = $("#"+ opt.down);//Shawphy:向下按钮
	var _this=this.eq(0).find("ul:first");
	var lineH=_this.find("li:first").height(), //获取行高
	line=opt.line?parseInt(opt.line,10):parseInt(this.height()/lineH,10), //每次滚动的行数，默认为一屏，即父容器高度
	speed=opt.speed?parseInt(opt.speed,10):500; //卷动速度，数值越大，速度越慢（毫秒）
	if(line==0) line=1;
	var upHeight=0-line*lineH;
	//滚动函数
	var scrollUp=function(){
	_btnUp.unbind("click",scrollUp); //Shawphy:取消向上按钮的函数绑定
	_this.animate({
	marginTop:upHeight
	},speed,function(){
	for(i=1;i<=line;i++){
	_this.find("li:first").appendTo(_this);
	}
	_this.css({marginTop:0});
	_btnUp.bind("click",scrollUp); //Shawphy:绑定向上按钮的点击事件
	});
	}
	//Shawphy:向下翻页函数
	var scrollDown=function(){
	_btnDown.unbind("click",scrollDown);
	for(i=1;i<=line;i++){
	_this.find("li:last").show().prependTo(_this);
	}
	_this.css({marginTop:upHeight});
	_this.animate({
	marginTop:0
	},speed,function(){
	_btnDown.bind("click",scrollDown);
	});
	}
	_btnUp.css("cursor","pointer").click( scrollUp ).mouseover(function(){$(this).addClass("list-up-h")}).mouseout(function(){$(this).removeClass("list-up-h")});//Shawphy:向上向下鼠标事件绑定
	_btnDown.css("cursor","pointer").click( scrollDown ).mouseover(function(){$(this).addClass("list-down-h")}).mouseout(function(){$(this).removeClass("list-down-h")});
	}      
	})
	})(jQuery);
	$(document).ready(function(){
	$("#supply .bd").Scroll({line:5,speed:500,up:"btn1",down:"btn2"});
	$("#buy .bd").Scroll({line:5,speed:500,up:"btn3",down:"btn4"});
	$("#supplier .bd").Scroll({line:5,speed:500,up:"btn5",down:"btn6"});
});