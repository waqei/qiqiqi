/* 首页幻灯片 */
$(function(){
     var len  = $(".slide-triggers > li").length;
	 var index = 0;
	 var adTimer;
	 $(".slide-triggers li").mouseover(function(){
		index  =   $(".slide-triggers li").index(this);
		showImg(index);
	 }).eq(0).mouseover();	
	 $('.slide').hover(function(){
			 clearInterval(adTimer);
		 },function(){
			 adTimer = setInterval(function(){
			    showImg(index)
				index++;
				if(index==len){index=0;}
			  } , 5000);
	 }).trigger("mouseleave");
});
function showImg(index){
        var adHeight = $(".slide").height();
		$(".slide-list").stop(true,false).animate({top : -adHeight*index},500);
		$(".slide-triggers li").removeClass("on").eq(index).addClass("on");
}

/* 自动缩放图片 */
jQuery.fn.LoadImage=function(scaling,width,height){
	return this.each(function(){
		var t=$(this);
		var src=$(this).attr("src")
		var img=new Image();
		img.src=src;
		//自动缩放
		var autoScaling=function(){
			if(scaling){
				if(img.width>0 && img.height>0){ 
			        if(img.width/img.height>=width/height){ 
			            if(img.width>width){ 
			                t.width(width); 
			                t.height((img.height*width)/img.width); 
			            }else{ 
			                t.width(img.width); 
			                t.height(img.height); 
			            } 
			        } 
			        else{ 
			            if(img.height>height){ 
			                t.height(height); 
			                t.width((img.width*height)/img.height); 
			            }else{ 
			                t.width(img.width); 
			                t.height(img.height); 
			            } 
			        } 
			    } 
			}	
		}
		//处理FF下会自动读取缓存图片
		if(img.complete){
		    //alert("获取缓存图片");
			autoScaling();
		    return;
		}
		$(this).attr("src","");
		t.hide();
		$(img).load(function(){
			autoScaling();
			t.attr("src",this.src);
			t.show();
			//alert("完成")
		});	
	});
}
//首页企业动态图片
$(function(){
	$("#gw_b_i img").LoadImage(true,160,135);
});
//产品详细页面图片
$(function(){
	$("#gw_b img").LoadImage(true,500,400);
});

/* 产品详细幻灯片 */
$(function(){
	var defaultOpts = { interval: 5000, fadeInTime: 200, fadeOutTime: 200 };
	var _titles = $(".num_loop li");
	var _bodies = $(".pic_loop li");
	var _count = _titles.length;
	var _current = 0;
	var _intervalID = null;
	var stop = function() { 
		window.clearInterval(_intervalID); 
	};
	var slide = function(opts) {
		if (opts) {
			_current = opts.current || 0;
		} else {
			_current = (_current >= (_count - 1)) ? 0 : (++_current);
		};
		_bodies.filter(":visible").fadeOut(defaultOpts.fadeOutTime, function() {
			_bodies.eq(_current).fadeIn(defaultOpts.fadeInTime);
			_bodies.removeClass("on").eq(_current).addClass("on");
		});
		_titles.removeClass("on").eq(_current).addClass("on");
	};
	var go = function() {
		stop();
		_intervalID = window.setInterval(function() { slide(); }, defaultOpts.interval);
	}; 
	var itemMouseOver = function(target, items) {
		stop();
		var i = $.inArray(target, items);
		slide({ current: i });
	}; 
	_titles.hover(function() { if($(this).attr('class')!='on'){itemMouseOver(this, _titles); }else{stop();}}, go);
	_bodies.hover(stop, go);
	go();
});

/* 导航效果（兼容IE6） */
$(function(){
		$("#navigation ul li:has(ul)").hover(function(){
			$(this).children("ul").stop(true,true).show();
        },function(){
		    $(this).children("ul").stop(true,true).hide();
		});
		$('li', this).hover(
			function() { $(this).addClass('hover'); $('> a', this).addClass('hover'); },
			function() { $(this).removeClass('hover'); $('> a', this).removeClass('hover'); }
		);
})