$(function(){
    //se selecciona el boton por su evento onclick 
    $('.btnVer').on('click',function(evt){
        evt.preventDefault();
        //se recupera el id del boton 
        let id_persona =$(this).attr('persona');
        //console.log(id_persona);

        //metodo ajax por post
        $.ajax({
            URL: '{%url "doctor:index"%}',
            type: 'POST',
            data:{id:id_persona},
            dataType:'json' 

        }).done(function(data){
            console.log(data)
            location.href=(`/doctors/doctor-detalle/`+id_persona)
            

        })
    });
    //se selecciona el boton 
    $('.cerrar').on('click',function(){
        //se manda a la ruta logout
        location.href=(`/logout/`)
    })
})