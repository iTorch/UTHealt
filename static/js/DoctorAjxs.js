$(function(){
    $('.btnVer').on('click',function(evt){
        evt.preventDefault();
        let id_persona =$(this).attr('persona');
        //console.log(id_persona);

        $.ajax({
            URL: '{%url "doctor:index"%}',
            type: 'POST',
            data:{id:id_persona},
            dataType:'json' 

        }).done(function(data){
            console.log(data)
            

        })
    });
})