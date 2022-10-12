$(document).ready(function() {
} );

$(".btn-simpan").click(function() {
    var no_telp = $("input[name='judul']").val();
    var kode_kontak = $("input[name='kode']").val();

    if (no_telp == ''){
      swal("Data Harus Diisi!", "Pilih Ok untuk mengisi", "warning", {
        button: "OK",
      });
    }
    else{
    $.ajax({
        type: "post",
        url: "/kontak_cs/req",
        data: {no_telp, kode_kontak},
        success: function(data) {
          swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
          $(".confirm").click(function() {
            window.location.href = "/kontak_cs";
          });  
        }
      })
    }
});