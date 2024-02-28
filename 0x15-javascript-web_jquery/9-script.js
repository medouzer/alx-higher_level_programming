$(document).ready(function () {
  const word = $('DIV#hello');
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      word.text(data.hello);
    },
  });
});
