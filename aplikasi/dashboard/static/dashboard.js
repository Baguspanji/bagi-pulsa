'use strict';

$(".provider").click(function(event) {
    var kode_provider = $(this).attr('name');
    var status_provider = $(this).val();
    event.preventDefault();
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
            url: "/layanan_operator/req",
            data: {status_provider, kode_provider},
            success: function(data) {
                swal("Sukses!", "Data Berhasil Terganti!", "success"); 
                $(".confirm").click(function() {
                window.location.href = "/layanan_operator";
                });  
            }
        })
    });
});