/* Created by sunjiahui on 3/10/16.
 */
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

var arr=new Array();
arr[0]="../static/img/g5.jpg";
arr[1]="../static/img/g4.jpg";
arr[2]="../static/img/g3.jpg";
arr[3]="../static/img/g2.jpg";
arr[4]="../static/img/g1.jpg";

var num=0;
setInterval(turnpic,4000);
function turnpic(){
    idsrc=document.getElementById("image");
    if(num==arr.length-1)
        num=0;
    else
        num+=1;
    idsrc.src=arr[num];
}

//��ҳ��ͼƬЧ��
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