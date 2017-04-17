/* Add your Application JavaScript */
var url='/url'
var urll=[]
var thumbs
var imgs
$(document).ready(function(){
    $('#submit').click(function(e){
        e.preventDefault();
        console.log("\""+$('#search').val()+"\"");
        urls="\""+$('#search').val()+"\""
        $.ajax({
            url,
            data:{
                urls:$('#search').val()
            },
            method:"POST"
        }).done(function(status){
            console.log(status);
            console.log("B4");
            urll=status.split(',')
            console.log(urll[1])
            imgs=urll.splice(0,1)
            console.log(imgs[0])
        });
    });
});