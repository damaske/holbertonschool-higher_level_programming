/*JavaScript-скрипт, который работает из
 <head> и выводит перевод "Hello" по-французски с API
*/
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching greeting:', error);
    });
});
