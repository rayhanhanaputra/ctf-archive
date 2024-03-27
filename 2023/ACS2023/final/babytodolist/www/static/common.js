window.onload = function() {
  const clock = document.querySelector("#clock")
  function getClock() {
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth()).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      const hours = String(date.getHours()).padStart(2, "0");
      const min = String(date.getMinutes()).padStart(2, "0");
      const sec = String(date.getSeconds()).padStart(2, "0");
      clock.innerText = `${year}-${month}-${day} ${hours}:${min}:${sec}`;
  }
  setInterval(getClock, 1000);
  const quotes = [
    "Life is what happens when you're busy making other plans.",
    "The way to get started is to quit talking and begin doing.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "The only impossible journey is the one you never begin.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "To see what is right and not do it is the want of courage.",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty."
  ];

  const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
  document.getElementById('quote').textContent = randomQuote;

  fetchLocation();
};
function getWeather(lat, lon) {
  const apiKey = 'c8a76b177e8ec37639c6856d37c90dd1';

  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;

  fetch(url)
      .then(response => response.json())
      .then(data => {
          const temp = data.main.temp;
          const desc = data.weather[0].description;
          document.getElementById('weatherInfo').textContent = `Temperature: ${temp}°C, Description: ${desc}`;
      })
      .catch(error => {
          document.getElementById('weatherInfo').textContent = "Error fetching weather information.";
      });
}
function fetchLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            getWeather(lat, lon);
        }, () => {
            document.getElementById('weatherInfo').textContent = "Unable to retrieve your location.";
        });
    } else {
        document.getElementById('weatherInfo').textContent = "Geolocation is not supported by this browser.";
    }
}
function removeTodo(e, task){
  $(e).parents(".Todo").remove();
  if (task) {
    fetch('/todo_process.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'mode=remove&task=' + encodeURIComponent(task)
    }).then();
  }
}
function addTodo(){
  var addText = $("#addText").val();
  if (addText.trim().length > 0){
    var addList = $("#addList");
    var newTodo = $("#newTodo").clone();
    newTodo.attr("id", "");
    newTodo.removeClass("hidden");
    newTodo.find("label").find("span").text(addText);
    addList.append(newTodo);
    $('#addModal').hide();
    fetch('/todo_process.php', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'mode=add&task=' + encodeURIComponent(addText)
    }).then();
  }else{
    alert("No inputs.");
  }
}
function showTodo(){
  $('#addModal').show();
  $("#addText").val("");
}
function closeTodo(){
  $('#addModal').hide();
}
function todoDone(task){
  if (task){
    fetch('/todo_process.php', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'mode=done&task=' + encodeURIComponent(task)
    }).then();
  }
}
function changeTheme(color){
  fetch('/todo_process.php', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: 'mode=changeTheme&theme=' + encodeURIComponent(color)
  }).then(function(){
    location.reload();
  });
}