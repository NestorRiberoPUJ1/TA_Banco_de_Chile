


function suma(n1, n2) {
    return n1 + n2;
}

const add = (n1, n2) => n1 + n2;

console.log(suma(1, 5));
console.log(add(5, 8));

const average = (numlist) => {
    let sum = 0;
    for (let index = 0; index < numlist.length; index++) {
        sum += numlist[index];
    }
    console.log(sum);
    let sumy = numlist.reduce((previous, current) => previous + current, 20);
    let double = numlist.map((value) => value * 2);

    numlist.forEach(element => {
        console.log(element);
    });

    console.log("SUMATORIA", sumy);
    console.log("Double", double);
    return sum / numlist.length
}

let lista = [2, 0, 2, 0, 2, 0];

console.log("Average", average(lista));