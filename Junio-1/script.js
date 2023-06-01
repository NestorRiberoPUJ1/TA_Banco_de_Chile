

const aumentar = (element) => {
    let num = parseInt(element.innerHTML);
    num++;
    element.innerHTML = num;
}


setTimeout(() => {
    let numeroRojo = document.getElementById("redTeam");
    let numeroAzul = document.getElementById("blueTeam");
    numeroRojo = parseInt(numeroRojo.innerHTML);
    numeroAzul = parseInt(numeroAzul.innerHTML);
    if (numeroAzul > numeroRojo) {
        alert("Ganaron los azules");
    }
    else if (numeroAzul < numeroRojo) {
        alert("Ganaron los rojos");
    }
    else {
        alert("Empate");
    }
}, 10000)


function solicitarImagen() {
    //fetch()
}

