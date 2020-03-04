$(function () {
    $('.message_title').click(function () {

        let id=$(this).attr('id');
         $.ajax({
            'url': '/blog/message',
            'type': 'get',
             'data':'id='+id,
             //data:'name='+name+'&user='+user,
             success:function (data) {
                $("#title_body").html(data.btn)
             }
         });
     });

});


$(function () {
    $('#btn_l').click(function () {

        //let id=$('input').attr('name');
        let title=$("input[name='message_title']").val();
        let body=$("textarea[name='message_body']").val();
         $.ajax({
            'url': '/blog/message_ajax',
            'type': 'get',
             data:{title:title,body:body},
             success:function (data) {
                alert(data.btn);

             }
         });
     });

});