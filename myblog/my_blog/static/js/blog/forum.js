var post_id=null;
$(function () {
    //绑定Ajax事件
    $('.title').click(function () {
        post_id=$(this).attr('id');
        let id=post_id;
        $.ajax({
          'url':'/blog/forum_ajax' ,                    //btn_ajax请求的路径
          'type':'get',                       //请求方式，默认get
            'data':'id='+id,
          //'datetype':'json' ,
          success:function (data) {
                //console.log(data.body)
              $('#body').html(data.body);
              $('#comment').html(data.pls);

              //console.log(data.pls);
              $('#comments_on').show();
            
          }

        });
    });
});

//展开，收回评论区信息
$(function () {
    $('#li_pl').click(function () {
        $('.ment').toggle();

    });

});


$(function () {
    $('#submitComment').click(function () {
        //console.log("$('.pl textarea').text()",$('.pl textarea').val());
        let id=post_id;
        //console.log(id);
         $.ajax({
            'url': '/blog/sflogin',
            'type': 'post',
             'data':{'id':id,'comment_body':$('.pl textarea').val(),
             'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()},
             success:function (data) {
                //console.log(data);
                 alert(data.bk);
             }
         });
     });

});




