$(function() {

  console.log("whee!")

  // event handler
  $("#btn-click").click(function() {
    if ($('input').val() !== '') {
      // grab the value from the input box after the button click
      var input = $("input").val()
      // display value within the browser's JS console
      console.log(input)
      // add the value to the DOM
      $('ol').append('<li><a href="">x</a> - ' + input + '</li>');
    }
    $('input').val('');
  });

});

$(document).on('click', 'a', function (e) {
    e.preventDefault();
    $(this).parent().remove();
});
