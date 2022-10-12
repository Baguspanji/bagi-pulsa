'use strict';

$(document).ready(function() {
  var table = $('#main-table').DataTable({ });
} );

$(".rating").click(function() {
  var kode_provider = $(this).attr('name');
    $.ajax({
        type: "post",
        url: "/rate_operator/show",
        data: {kode_provider},
        success: function(data) {
            $(".kode").val(''+data.data[0].kode_provider+'');
            $(".nilai_min").val(''+data.data[0].nilai_minimal+'');
            $(".nilai_max").val(''+data.data[0].nilai_maksimal+'');
            $(".rate").val(''+data.data[0].rate * 100+'');
            $(".no_admin").val(''+data.data[0].no_admin+'');
            $('#exampleModalCenter').modal('show');

            $(".save_rate").on("click", function() {
                var nilai_minimal = $(".nilai_min").val();
                var nilai_maksimal = $(".nilai_max").val();
                var rating = $(".rate").val();
                var rate = parseInt(rating)/100;
                var no_admin = $(".no_admin").val();
                kode_provider = $(".kode").val();
                $.ajax({
                    type: "post",
                    url: "/rate_operator/req",
                    data: {nilai_minimal, nilai_maksimal, rate, no_admin, kode_provider},
                    success: function(data) {
                        window.location.href = "/rate_operator";
                    }
                }) 
            });
        }
    }) 
  });