'use strict';

$(document).ready(function() {
  var table = $('#main-table').DataTable({ });
} );

$(".status").click(function() {
  var status_bank = $(this).attr('title');
  var kode_bank = $(this).attr('name');
    swal({
      title: "Apakah Yakin Ingin Merubah?",
      type: "warning",
      showCloseButton: true,
      showCancelButton: true,
      confirmButtonText: 'Ubah',
      cancelButtonText: 'Batal',
      closeOnConfirm: false,
    },function() {
      $.ajax({
          type: "post",
          url: "/layanan_bank/req",
          data: {status_bank, kode_bank},
          success: function(data) {
            swal("Sukses!", "Data Berhasil Terganti!", "success"); 
            $(".confirm").click(function() {
              window.location.href = "/layanan_bank";
            });  
          }
        })
    });  
});

$(".layanan_bank").click(function() {
  var kode_bank = $(this).attr('name');
    $.ajax({
        type: "post",
        url: "/layanan_bank/show",
        data: {kode_bank},
        success: function(data) {
            $(".kode").val(''+data.data[0].kode_bank+'');
            $(".b_admin").val(''+data.data[0].biaya_bank+'');
            $('#exampleModalCenter').modal('show');

            $(".save_bank").on("click", function() {
                var biaya_bank = $(".b_admin").val();
                kode_bank = $(".kode").val();
                $.ajax({
                    type: "post",
                    url: "/layanan_bank/send",
                    data: {biaya_bank, kode_bank},
                    success: function(data) {
                        window.location.href = "/layanan_bank";
                    }
                }) 
            });
        }
    })   
});