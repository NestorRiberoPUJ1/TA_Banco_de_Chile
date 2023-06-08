

var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};


/* fetch("https://swapi.dev/api/people/1", requestOptions)
    .then(response => response.json())
    .then(result => {
        let nombre = document.getElementById("nombre");
        nombre.innerHTML = result.name;
    })
    .catch(error => console.log('error', error));
 */
async function buscarPersona() {
    let num = document.getElementById("inputPersona").value
    console.log(num);
    let response = await fetch("https://swapi.dev/api/people/" + num, requestOptions);

    let result = await response.json();

    let nombre = document.getElementById("nombre");
    nombre.innerHTML = result.name;
}
