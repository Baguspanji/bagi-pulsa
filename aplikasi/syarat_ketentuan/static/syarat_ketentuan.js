$(document).ready(function() {
  var deskripsi = $('#deskripsi').val();
    // $('#table-kk').DataTable();
    $('#summernote').summernote({
        placeholder: 'Masukkan Keterangan',
        tabsize: 2,
        height: 180,
        toolbar: [
          ['style', ['style']],
          ['font', ['bold', 'underline', 'clear']],
          ['color', ['color']],
          ['para', ['ul', 'ol', 'paragraph']],
          ['table', ['table']],
          ['insert', ['link', 'picture', 'video']],
          ['view', ['fullscreen', 'codeview', 'help']]
        ]
    });
    $('#summernote').summernote('code', deskripsi);
} );

$(".btn-simpan").click(function() {  
    var deskripsi = $('#summernote').summernote('code');
    var text = $($("#summernote").summernote("code")).text();
    var judul = $("input[name='judul']").val();
    var kode = $("input[name='kode']").val();

    if (text == '' || judul == ''){
      swal("Data Harus Diisi!", "Pilih Ok untuk mengisi", "warning", {
        button: "OK",
      });
    }
    if (text != '' && judul != ''){
    $.ajax({
        type: "post",
        url: "/syarat_ketentuan/req",
        data: {deskripsi, kode},
        success: function(data) {
          swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
          $(".confirm").click(function() {
            window.location.href = "/syarat_ketentuan";
          });  
        }
      })
    }
});