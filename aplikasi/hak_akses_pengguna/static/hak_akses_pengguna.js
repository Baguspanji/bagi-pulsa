'use strict';
const btnTambah = document.querySelector('.btn-tambah');
let kode_role;
let kode;
let link;

$(document).ready(function() {
  $('#main-table').DataTable({ });
} );

$(".btn-edit").click(function() {
kode = $(this).attr('title');
link = `/hak_akses_pengguna_edit/?kode=${kode}`;
window.location.href = link;
  // swal({
  //   title: "Edit Nama Hak Akses :",
  //   type: "input",
  //   inputValue: nama,
  //   showCloseButton: true,
  //   showCancelButton: true,
  //   confirmButtonText: 'Simpan',
  //   cancelButtonText: 'Batal',
  //   closeOnConfirm: false,
  // },function() {
  //   nama_role = $("input[tabindex='3']").val();
  //   $.ajax({
  //       type: "put",
  //       url: "/hak_akses_pengguna/put",
  //       data: {kode_role, nama_role},
  //       success: function(data) {
  //         swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
  //         $(".confirm").click(function() {
  //           window.location.href = "/hak_akses_pengguna";
  //         });  
  //       }
  //     })
  // });  
});

$(".btn-hapus").click(function() {
  kode_role = $(this).attr('name');
  // console.log(typeof kode_role);
    swal({
      title: "Apakah Yakin Ingin Menghapus",
      type: "warning",
      showCloseButton: true,
      showCancelButton: true,
      confirmButtonText: 'Hapus',
      cancelButtonText: 'Batal',
      closeOnConfirm: false,
    },function() {
      $.ajax({
          type: "delete",
          url: "/hak_akses_pengguna/delete",
          data: {kode_role},
          success: function(data) {
            // console.log(data, typeof data);
            swal("Dihapus!", "Data Berhasil Dihapus!", "success"); 
            $(".confirm").click(function() {
              window.location.href = "/hak_akses_pengguna";
            });  
          }
        })
    });  
  });

  $(".btn-ganti").click(function() {
  var id = $(this).attr('name');
    $.ajax({
        type: "post",
        url: "/hak_akses_pengguna/show",
        data: {id},
        success: function(data) {
            $(".user").val(data.data[0].username);
            $(".kode").val(data.data[0].id);
            $('#exampleModalCenter').modal('show');

            $(".save_rate").on("click", function() {
                var id = $(".kode").val();
                var password = $(".password").val();
                var username = $(".user").val();
                if (password == '' || password == null){
                  $.ajax({
                    type: "post",
                    url: "/hak_akses_pengguna/req_user",
                    data: {username, id},
                    success: function(data) {
                      window.location.href = "/hak_akses_pengguna";
                    }
                  }) 
                }else{
                  $.ajax({
                    type: "post",
                    url: "/hak_akses_pengguna/req",
                    data: {username, password, id},
                    success: function(data) {
                      window.location.href = "/hak_akses_pengguna";
                    }
                  }) 
                }
            });
        }
    }) 
});

btnTambah.addEventListener('click', function () {
    window.location.href = "/hak_akses_pengguna_tambah";
});