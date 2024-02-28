const update_header = $('DIV#update_header');
const header = $('header');

$(document).ready(function () {
  update_header.click(function () {
    header.text('New Header!!!');
  });
});
