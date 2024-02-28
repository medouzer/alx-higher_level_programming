const name = $('DIV#character');

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      name.text(data.name);
    },
  });
});
