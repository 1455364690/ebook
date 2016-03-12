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

function ch3(){
    var bor=document.getElementById('image');
    var borWidth=parseInt(bor.style.borderWidth);
    bor.style.borderWidth=borWidth+5+'px';
}
function ch4(){
    var bor=document.getElementById('image');
    var borWidth=parseInt(bor.style.borderWidth);
    bor.style.borderWidth=borWidth-5+'px';
}


var arr=new Array();
arr[0]="/static/img/g5.jpg";//��ͼƬ��ַ
arr[1]="/static/img/g4.jpg";
arr[2]="/static/img/g3.jpg";
arr[3]="/static/img/g2.jpg";
arr[4]="/static/img/g1.jpg";

var num=0;
setInterval(turnpic,4000); //ÿ��4��ת��ͼƬ
function turnpic(){
    idsrc=document.getElementById("image");
    if(num==arr.length-1)
        num=0;
    else
        num+=1;
    idsrc.src=arr[num];
}
