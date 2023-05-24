const ID = "123456";

console.log("ID:", ID);

//ID = 24; esto es un error a las const no se les puede reasignar valor
var salario;
console.log("Salario", salario);
salario = 3500;
console.log("Salario", salario);

let horas = 40;


for (let index = 0; index < 5; index++) {
    var numerito = 12;
    console.log(index);
    if (index == 4) {
        console.log("Salario", salario);
    }
    else if (index == 2) {
        console.log("Horas", horas);
    }
    else if (index == 1) {
        console.log("Num", numerito);
    }
}
console.log(numerito);

let nombre = "Nestor"; //string texto
let edad = 25; //numerica entera int
let altura = 1.85; //numerica decimal float 
let graduado = true; // boolean binarias

let arreglos = [];//
let objectos = {};//