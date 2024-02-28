const add_item = $('DIV#add_item');
const my_list = $('UL.my_list');

$(document).ready(function () {
  add_item.click(function () {
    $('<li>Item</li>').appendTo(my_list);
  });
});
