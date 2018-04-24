$.ajax({
  url: '/bangalore',
  data: {page: 4},
  dataType: "json",
  success: function(t) {
    console.log(t);
  }
})
