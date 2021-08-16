$(function(){
    /*$(document).ready(function(){
        $('.table').DataTable({
            responsive:true,
            autowith:false
        });
    });*/
    $(document).on('click','#btnAll',function(evt){
        //evita que re recargue la pagia
        evt.preventDefault();
        $.ajax({
            url:'{% url "doctor:index"%}',
            type:'POST',
            success:(res)=>{
                console.log(res.data)
            }
        })
    });

/*
    $('.#getAll').on('click', function(){
        $.ajax({
            url:'{% url "doctor:index"%}',
            type:"POST",
            data:{id:1},
            dataType:'json'
        }).done(function(data){
            let tbody=$('tbody');
            tbody.html('');
            data.forEach(p=>{
                ` <tr>
                <td></td>
                <td><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                  <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>${p.nombre}</td>
                <td>${p.apellido_paterno}</td> 
                <td>${p.apellido_materno}</td>
                <td>${p.fecha_nacimiento}</td>
                <td>${p.genero}</td>
                <td><form method="GET" >
                
                  <input type="text" name="id_persona" value="${e.id} "hidden>
                  <a href="#"><input class="btn btn-primary btnSearch" type="submit">Ver</a>
                </form>
              </td>
            </tr>
          {%else%}
              <center><h3 class="text alert-danger">No hay registros de pacientes</h3></center>
          {%endif%}`
            })

        })
    });
*/
/*
    $('#getPacientes').on('click',function(){
        $.ajax({
           url:'doctors/doctor/',
           type:'GET',
           data:{id_persona:1},
           dataType:'json'

        }).done(function(data){
           let tbody =$('tbody');
           tbody.html('');
           object_list.forEach(e => {
               tbody.append(`
               
               
                 <tr>
                     <td></td>
                     <td><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                       <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                       <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                     </svg>${e.nombre}</td>
                     <td>${e.apellido_paterno}</td> 
                     <td>${e.apellido_materno}</td>
                     <td>${e.fecha_nacimiento}</td>
                     <td>${e.genero}</td>
                     <td><form method="GET" >
                     
                       <input type="text" name="id_persona" value="${e.id} "hidden>
                       <a href="#"><input class="btn btn-primary btnSearch" type="submit">Ver</a>
                     </form>
                   </td>
                 </tr>
               {%else%}
                   <center><h3 class="text alert-danger">No hay registros de pacientes</h3></center>
               {%endif%}

               `)
           });
        }).fail(function (){
            alert('Algo ha salido mal')
        })
    });*/
})