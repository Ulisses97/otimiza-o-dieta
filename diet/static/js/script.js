const formulario = document.querySelector(".formulario");
const minCaloria = document.querySelector('input[name="minCaloria"]');
const maxCaloria = document.querySelector('input[name="maxCaloria"]');
const minColesterol = document.querySelector('input[name="minColesterol"]');
const maxColesterol = document.querySelector('input[name="maxColesterol"]');
const minGordura = document.querySelector('input[name="minGordura"]');
const maxGordura = document.querySelector('input[name="maxGordura"]');
const minSodio = document.querySelector('input[name="minSodio"]');
const maxSodio = document.querySelector('input[name="maxSodio"]');
const minCarboidrato = document.querySelector('input[name="minCarboidrato"]');
const maxCarboidrato = document.querySelector('input[name="maxCarboidrato"]');
const minFibras = document.querySelector('input[name="minFibras"]');
const maxFibras = document.querySelector('input[name="maxFibras"]');
const minProteina = document.querySelector('input[name="minProteina"]');
const maxProteina = document.querySelector('input[name="maxProteina"]');
const minVitA = document.querySelector('input[name="minVitA"]');
const maxVitA = document.querySelector('input[name="maxVitA"]');
const minVitC = document.querySelector('input[name="minVitC"]');
const maxVitC = document.querySelector('input[name="maxVitC"]');
const minCalcio = document.querySelector('input[name="minCalcio"]');
const maxCalcio = document.querySelector('input[name="maxCalcio"]');
const minFerro = document.querySelector('input[name="minFerro"]');
const maxFerro = document.querySelector('input[name="maxFerro"]');
const results = document.querySelector("#results");

function onSubmit(event) {
  event.preventDefault();
  const obj = {
    minCaloria: minCaloria.value,
    maxCaloria: maxCaloria.value,
    minColesterol: minColesterol.value,
    maxColesterol: maxColesterol.value,
    minGordura: minGordura.value,
    maxGordura: maxGordura.value,
    minSodio: minSodio.value,
    maxSodio: maxSodio.value,
    minCarboidrato: minCarboidrato.value,
    maxCarboidrato: maxCarboidrato.value,
    minFibras: minFibras.value,
    maxFibras: maxFibras.value,
    minProteina: minProteina.value,
    maxProteina: maxProteina.value,
    minVitA: minVitA.value,
    maxVitA: maxVitA.value,
    minVitC: minVitC.value,
    maxVitC: maxVitC.value,
    minCalcio: minCalcio.value,
    maxCalcio: maxCalcio.value,
    minFerro: minFerro.value,
    maxFerro: maxFerro.value,
  };

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  let csrftoken = getCookie("csrftoken");

  fetch("/diet/criarDieta", {
    method: "POST",
    body: JSON.stringify(obj),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => response.json())
    .then((json) => {
      let str = "";
      for (chave in json) {
        str += `${chave}:${json[chave]}\n`;
      }
      results.innerHTML = str;
    })
    .catch((err) => console.log(err));
}

formulario.addEventListener("submit", onSubmit);
