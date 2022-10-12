'use strict';

$(document).ready(function() {
  $('#main-table').DataTable({ 
    scrollX: true,
    scrollY: true
  });
});

  $(".aksi_sukses").click(function() {
    var kode_transaksi = $(this).attr('title');
    var status = $(this).attr('name');
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
            url: "/transaksi/req",
            data: {status, kode_transaksi},
            success: function(data) {
              swal("Sukses!", "Data Berhasil Terganti!", "success"); 
              $(".confirm").click(function() {
                window.location.href = "/transaksi";
              });  
            }
          })
      });  
  });

  $(".aksi_gagal").click(function() {
    var kode_transaksi = $(this).attr('title');
    var status = $(this).attr('name');
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
            url: "/transaksi/req",
            data: {status, kode_transaksi},
            success: function(data) {
              swal("Sukses!", "Data Berhasil Terganti!", "success"); 
              $(".confirm").click(function() {
                window.location.href = "/transaksi";
              });  
            }
          })
      });  
  });