

document.getElementById("search_btn").addEventListener("click", displayDate);

function displayDate() {
  document.getElementById("demo").innerHTML = Date();

  console.log(output)
}

$(function() {
  $('#search_btn').bind('click', function() {
    $.post('/', {  
      story: $('textarea[name="story"]').val(),
    }, function(data) {
      $('#demo').text(data.result);
    });
    return false;
  });
});

