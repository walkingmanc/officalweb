$(function(){
   var urlstr = location.href;
    urlstatus = false;
    fullAdress='';
    $('#nav ul li a').each(function () {
        fullAdress=$(this).attr('href');
      //alert("f="+fullAdress);
        lastChar=fullAdress.substr(fullAdress.length-1,1)
        //alert("lastChar="+lastChar);
        if(!isNaN(lastChar))mainAdress=fullAdress.substring(0,fullAdress.lastIndexOf('-'));
        else  mainAdress=fullAdress;

        if(mainAdress.indexOf('-') > -1)
        navMainAdress=mainAdress.substr(0,mainAdress.lastIndexOf('-'));
        else
        navMainAdress=mainAdress;

          //alert(" urlstr="+ urlstr+";mainAdress="+mainAdress+";navMainAdress="+navMainAdress);
        if (urlstr.indexOf(navMainAdress) > -1&&navMainAdress!=''&&navMainAdress!='.') {
            //alert(" add class");
        $(this).addClass('selected'); urlstatus = true;
    }

    else {
         //alert(" remove class");
        $(this).removeClass('selected');
         //alert("remove selected");
    }
});

    //alert("menuIndex="+menuIndex)
    if (!urlstatus) {$("#nav ul li a").eq(0).addClass('selected');}
    //导航栏目选中时背景色改变

    $('#nav ul li a').hover(function (ev) {
        //alert("r");

        //找到背景变色的a标签
         //var aTag=$(this).parent().siblings().find('a').css("selected);
         $(this).parent().siblings().find('a').removeClass('hovered');
        //.siblings().removeClass('selected');

            //将选择的菜单背景色改变

        $(this).addClass('hovered');

    });
     //alert("urlstr="+urlstr);
    //案例选择时背景变色
    $('#nav_cata ul li a').each(function () {
        cataNavFullAddr=$(this).attr('href');
      //alert("f="+fullAdress);

        //alert("lastChar="+lastChar);
       cataNavMainAddr=cataNavFullAddr.substring(0,cataNavFullAddr.lastIndexOf('-'));
        //alert("cataNavMainAddr="+cataNavMainAddr);
          //alert(" urlstr="+ urlstr+";mainAdress="+mainAdress+";navMainAdress="+navMainAdress);
        if (urlstr.indexOf(cataNavMainAddr) > -1&&cataNavMainAddr!=''&&cataNavMainAddr!='.') {
            //alert(" add class");
        $(this).addClass('selected');
    }
    else {
         //alert(" remove class");
        $(this).removeClass('selected');
         //alert("remove selected");
    }
});


    $("#guestCollectSub").on("click",function(){

        //alert("点击提交按钮");
    var name= $('#name').val();
    var tel= $('#tel').val();
    var txt= $('#txt').val();

   //输入验证
msgTips='请填写 "';
if(name=='') msgTips=msgTips+"您的姓名 ";
if(tel=='')  msgTips=msgTips+"您的联系方式 ";
if(txt=='')  msgTips=msgTips+"您的需求描述信息 ";
 msgTips=msgTips+'"';

if(msgTips!='请填写 ""') {$('#guestCollectOutput').html(msgTips);return false;}


  $('#guestCollectSub').ajaxSubmit( //ajax方式提交表单
            {
                url:"guest/collect",
                dataType: "json",
                type:"post",
                data:{
                    name:name,
                     tel:tel,
                     txt:txt
                },
                success:function(data){
                  //alert(data.code);
                if (data.code==100){
                   $('#guestCollectOutput').html('您的需求已成功提交，我们将会在1-2个工作日内进行审核，请耐心等待!');
                }else if(data.code == 101){
                    $('#guestCollectOutput').html('您的需求提交失败!');
                }
                },
                clearForm: false,//禁止清楚表单
                resetForm: false //禁止重置表单
            });
            return false;//禁止页面刷新
    });
});