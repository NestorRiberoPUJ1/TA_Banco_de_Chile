const avogadro = 6.02 * 10 ^ 23; //Declaración con asignación Obligatoria const
var atomos = 20; //Declaración con asignación opcional para las var es global
atomos = 0;  //Asignación
let masa = 24;  //Declaración con asignación opcional para las let //let es local


if (atomos > 10) {
    console.log("ES MAYOR");
}
else if (atomos > 5) {
    console.log("No es tan pequeño");
}
else if (atomos > 2) {
    console.log("No es tan pequeñito");
}
else if (atomos > 0) {
    console.log("Al menos es positivo");
}
else {
    console.log("SI es pequeño");
}

// == igualdad
// === estrictamente igual 
// > mayor 
//< menor
// >= mayor igual
// <= menor igual

if (masa >= 10 && masa <= 15) {

}

if (masa < 8 || masa < 16) {

}

// && implica que las dos condiciones sean ciertas
// || implica que al menos una de las condiciones sea cierta


if (masa != 13) {

}

// != diferente 