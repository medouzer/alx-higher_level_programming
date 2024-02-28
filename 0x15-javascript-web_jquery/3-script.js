const red_header = $('DIV#red_header');
const header = $('header');

$(document).ready(function () {
  red_header.click(function () {
    header.addClass('red');
  });
});
