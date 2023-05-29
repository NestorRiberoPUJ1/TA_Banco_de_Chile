

/*
var numerito = Math.random()
var max = 10;// máximo
var min = 2;

var aleatorio = numerito * (max - min);
aleatorio = Math.round(aleatorio) + min;
console.log(numerito, aleatorio);
*/

function rangoAleatorio(min, max) {
    let number = Math.random();
    number = number * (max - min);
    number = Math.round(number) + min;
    return number
}

console.log(rangoAleatorio(12, 16));