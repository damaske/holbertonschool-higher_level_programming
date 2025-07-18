/*
 JavaScript-скрипт, который получает имя персонажа с указанного URL и 
 отображает его в HTML-элементе с id="character" с использованием Fetch API
 */
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
