const list_movies = $('UL#list_movies');

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      const results = data.results;
      results.forEach(function (movie) {
        list_movies.append('<li>' + movie.title + '</li>');
      });
    },
  });
});
