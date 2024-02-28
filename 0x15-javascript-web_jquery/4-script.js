const toggle_header = $('DIV#toggle_header');
const header = $('header');

$(document).ready(function () {
  toggle_header.click(function () {
    var currentClass = header.attr('class');
    if (currentClass === 'green') {
      header.removeClass('green').addClass('red');
    } else {
      header.removeClass('red').addClass('green');
    }
  });
});
