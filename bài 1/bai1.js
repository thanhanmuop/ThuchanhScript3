const url = 'https://jsonplaceholder.typicode.com/users';

let data = {
  name: 'Thanh'
}

let request = new Request(url, {
  method: 'POST',
  body: JSON.stringify(data),
  headers: {
    'Content-Type': 'application/json; charset=UTF-8'
  }
});

fetch(request)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));