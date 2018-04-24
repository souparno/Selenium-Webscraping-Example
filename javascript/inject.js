$.ajax({
  url: '/bangalore',
  data: {page: 4},
  dataType: "json",
  success: function(t) {
    $('div.results_holder').html(t.html);
  }
})
