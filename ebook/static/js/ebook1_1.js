/* Created by sunjiahui on 3/10/16.
 */
//回到顶部箭头变化
function toTop1(){
    var goToTop=document.getElementById('jiantou');
    var imgw=parseInt(jiantou.style.width);
    var imgh=parseInt(jiantou.style.height);
    goToTop.style.width=imgw+30+'px';
    goToTop.style.height=imgh+30+'px';
}
function toTop2(){
    var goToTop=document.getElementById('jiantou');
    var imgw=parseInt(jiantou.style.width);
    var imgh=parseInt(jiantou.style.height);
    goToTop.style.width=imgw-30+'px';
    goToTop.style.height=imgh-30+'px';
}
//主页图片
$.ajax({
    url:"",
    method:"get",
    success:function(data) {
        var template = "";
        for (var i = 0; i < data.length; i++) {
            template +="<a href='"+data[i]['url']+"'><div class='picture' id='picture"+i+1+"'><img class='aaa' src='"+data[i]['imgsrc']+"'/><p hidden> <h class='zi5'>"+data[i]['intro']+"</h><br><h class='zi6'>"+data[i]['qqq']+"</h></p></div></a>";
        }
    }
});
//畅游背景
$.ajax({
    url:"",
    method:"get",
    success:function(data){
        var template="";
            template+="<i style='position: absolute;margin:50px;font-size: 25px'>"+data['intro']+"</i>";
        }
});

$(function(){
    $("#picture1").mouseover(function(){
        $("#picture1 img").hide();
        $("#picture1 p").show()
    });
    $("#picture1").mouseout(function(){
        $("#picture1 img").show();
        $("#picture1 p").hide()
    });
});
$(function(){
    $("#picture2").mouseover(function(){
        $("#picture2 img").hide();
        $("#picture2 p").show()
    });
    $("#picture2").mouseout(function(){
        $("#picture2 img").show();
        $("#picture2 p").hide()
    });
});
$(function(){
    $("#picture3").mouseover(function(){
        $("#picture3 img").hide();
        $("#picture3 p").show()
    });
    $("#picture3").mouseout(function(){
        $("#picture3 img").show();
        $("#picture3 p").hide()
    });
});

$(function(){
    $("#picture4").mouseover(function(){
        $("#picture4 img").hide();
        $("#picture4 p").show()
    });
    $("#picture4").mouseout(function(){
        $("#picture4 img").show();
        $("#picture4 p").hide()
    });
});
$(function(){
    $("#picture5").mouseover(function(){
        $("#picture5 img").hide();
        $("#picture5 p").show()
    });
    $("#picture5").mouseout(function(){
        $("#picture5 img").show();
        $("#picture5 p").hide()
    });
});
$(function(){
    $("#picture6").mouseover(function(){
        $("#picture6 img").hide();
        $("#picture6 p").show()
    });
    $("#picture6").mouseout(function(){
        $("#picture6 img").show();
        $("#picture6 p").hide()
    });
});
$(function(){
    $("#picture7").mouseover(function(){
        $("#picture7 img").hide();
        $("#picture7 p").show()
    });
    $("#picture7").mouseout(function(){
        $("#picture7 img").show();
        $("#picture7 p").hide()
    });
});
$(function(){
    $("#picture8").mouseover(function(){
        $("#picture8 img").hide();
        $("#picture8 p").show()
    });
    $("#picture8").mouseout(function(){
        $("#picture8 img").show();
        $("#picture8 p").hide()
    });
});
$(function(){
    $("#picture9").mouseover(function(){
        $("#picture9 img").hide();
        $("#picture9 p").show()
    });
    $("#picture9").mouseout(function(){
        $("#picture9 img").show();
        $("#picture9 p").hide()
    });
});
$("#image").mouseover(function(){
    $(this).css({
        "-moz-opacity":"1",
        "opacity":"1"
    })
}).mouseout(function(){
    $(this).css({
        "-moz-opacity":"0.5",
        "opacity":"0.5"
    });
});



/*document.addEventListener('mouseover',function(e){
    if(e.target.classList.contains('_body_picture')){
        e.target.style.display='none';
        e.target.previousSibling.style.display="show";
    }
});

document.addEventListener('mouseout',function(e){
    if(e.target.classList.contains('picture')){
        $("._body_picture").show();
        $(".picture> p").hide();
    }
});*/
//轮播图片




