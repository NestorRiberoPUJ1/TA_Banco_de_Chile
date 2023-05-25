function nombreDeLaFuncion() {
    //cuerpo de la función
    console.log("TRAER AGUA");
}

nombreDeLaFuncion();
nombreDeLaFuncion();
nombreDeLaFuncion();

function conParametros(parametro) {
    //cuerpo de la función
    console.log("TRAER " + parametro);
}

conParametros("Billetera");
conParametros("Mouse");

let Salario = 200000;

function moneda(valor) {
    let currency = "$";
    currency += valor;
    return currency; //permiten retornar un valor
}

let sueldo = moneda(Salario);
console.log(sueldo);