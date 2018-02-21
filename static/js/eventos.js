
var BASE_URL = "http://"+window.location.hostname+":8000/juegosmundial/";

function eventoingresar(tipo){

	valnombre = $("#nombreUsuario").text()    
    var nomUsu = valnombre.split(":");
    console.log("abajo lo q hay")
    console.log(nomUsu[1])
    console.log(tipo)

        var valiUsu = {
            usuario: "pepito",
            contra: "123"
        };
        $.ajax({
            type: "POST",
            url: BASE_URL + "validar/",
            data: "data=" + JSON.stringify(valiUsu),
            async: false,
            success: function (data) {
                if(data==="true"){
                    alert("Usuario Ingresado Correctamente");
                    //window.location.assign(BASE_URL+'HojaCalculo?nom='+$("#usuario").val());
                }else{                    
                    alert("Ha introducido mal los datos requeridos");
                }
            }
        });



}