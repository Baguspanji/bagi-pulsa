'use strict';

$(".provider").click(function(event) {
    var kode_service = $(this).attr('name');
    var status_service = $(this).val();
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
            url: "/service/req",
            data: {status_service, kode_service},
            success: function(data) {
                swal("Sukses!", "Data Berhasil Terganti!", "success"); 
                $(".confirm").click(function() {
                window.location.href = "/service";
                });  
            }
        })
    });
});