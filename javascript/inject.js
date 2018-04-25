function initAjax(p) {
  $.ajax({
    url: '/bangalore',
    data: {
      page: p
    },
    dataType: "json",
    success: function(t) {
      $('div.results_holder').html(t.html);
    }
  })
}
