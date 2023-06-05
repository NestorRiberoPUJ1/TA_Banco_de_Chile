

const aumentar = (element) => {
    let num = parseInt(element.innerHTML);
    num++;
    element.innerHTML = num;
}

/*
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
*/

function solicitarImagen() {
    fetch("https://dog.ceo/api/breed/hound/images/random", {
        method: "GET",
    })
        .then((response) => response.json())
        .then((result) => {
            console.log(result);
            let imagenDog = document.getElementById("imagenDog");
            imagenDog.src = result.message;
            console.log(result.message);
        })
        .catch(error => console.log(error));
}

async function buscarPerrito() {
    try {
        const response = await fetch("https://dog.ceo/api/breed/akita/images/random", {
            method: "GET",
        });
        const result = await response.json();
        console.log(result);
        let imagenDog = document.getElementById("imagenDog");
        imagenDog.src = result.message;
        console.log(result.message);
    }
    catch (error) {
        console.log("AWAIT", error);
    }

}

var etiqueta = document.getElementById("imagenDog");
var arreglo = [1, 2, 3, 4, 5];

var doble = arreglo.map((gato,idx,lista) => {
    console.log(gato,idx,lista);
})