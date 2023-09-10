console.log("This is Hello World!");

var url = 'https://newsapi.org/v2/top-headlines?' +
          'country=us&' +
          'from=2023-08-02&' +
          'sortBy=popularity&' +
          'apiKey=9ccce2d7b2aa49f6855a919ea653ce48';

var req = new Request(url);

fetch(req)
    .then(function(response) {
        console.log(response.json());
    })