"use strict";
const btnTambah = document.querySelector(".btn-tambah");
const btnSimpan = document.querySelector(".btn-save-form");
const btnBatal = document.querySelector(".btn-batal");

let password = $("[name=password]").val();
let nama_role = "";
let role = [];
let temp_kd = "";
let child_id = "None";
let parent_id = "None";
let roleBody = {};
let data = {};
let url;
let checkbox;
let checkbox2;
let checkbox3;
let checkbox4;
let roleChild = {};
let arr = [];
let index;
let iChild;
let arrChild= [];
var g = [];
var parent_cek = [];
var child_cek = [];

roleBody = {
  child_id: child_id,
  parent_id: parent_id,
};

var count = $('.count_parent').val();

$(document).ready(function () {
  $('.parent_id1').prop('disabled', true);
  $('.parent_id1').prop('checked', true);
});

btnSimpan.addEventListener("click", function (e) {

  for (let x = 1; x <= count; x++) {
    $(`input[name="parent_id${x}"]`).each(function () {
        checkbox3 = $(this);
        if (checkbox3.is(":checked")) {
          parent_cek.splice(0, 1, 1);
          
          $('.child'+x+'').find('input').each(function(){
            checkbox4 = $(this);           
    
            if (checkbox4.is(":checked")) {
              child_cek.splice(0, 1, 1);
            }
          }); 

        }else{
          parent_cek.splice(0, 1, 0);

          $('.child'+x+'').find('input').each(function(){
            checkbox4 = $(this);           
    
            if (checkbox4.is(":checked")) {
              child_cek.splice(0, 1, 0);
            }
          }); 
        }
      });
  }
  
  if ( $("input[name='password']").val() == "" && $("input[name='nama_user']").val() == "" && $('.form-checkbox input[type=checkbox]').is(":checked") == false )  {
    swal("Gagal!", "Ada data yang kosong!!!", "warning");
    $(".btn-save-form").removeAttr("disabled");
    e.preventDefault();
  } else if($("input[name='password']").val() == "" ){
    swal("Gagal!", "Data Kode Masih Kosong!!!", "warning");
    e.preventDefault();
  } else if($("input[name='nama_user']").val() == "" ){
    swal("Gagal!", "Data Nama Masih Kosong!!!", "warning");
    e.preventDefault();
  } else if($('.form-checkbox input[type=checkbox]').is(":checked") == false ){
    swal("Gagal!", "Data Centang Masih Kosong!!!", "warning");
    e.preventDefault();
  } else if (child_cek[0] == 0){
    swal("Gagal!", "Pilih Menu Utama dan Sub Menu", "warning");
    e.preventDefault();
  }else {
    $(this).attr("disabled", true);
    // uppercaseKodeRole();
    nama_role = $("[name=nama_user]").val();

    for (let x = 1; x <= count; x++) {
      $(`input[name="parent_id${x}"]`).each(function () {
          checkbox = $(this);
          parent_id = $(this).val();
          if (checkbox.is(":checked")) {
            roleBody = {
              child_id: child_id,
              parent_id: parent_id
            };
            role.push(roleBody);
            
            $('.child'+x+'').find('input').each(function(){
              checkbox2 = $(this);
              child_id = $(this).val();              
      
              if ( checkbox2.is(":checked")) {
                  role.pop();
                  roleChild = {
                    id: child_id,
                  };
                  g.push(roleChild);

                  roleBody = {
                    child_id: g,
                    parent_id: parent_id,
                  };
                  role.push(roleBody);
                }
            }); 
            g = [];
            child_id = "None";     

          }
        });
    }

    data = {
      pw: password,
      user: nama_role,
      role: JSON.stringify(role)
    };
    // data={};
    url = "/hak_akses_pengguna_tambah/req";
    $.post(url, data, function (data) {
      // console.log(data);
      if (data.rc == "00" || data.rc == '00') {
        swal("Terkirim!", "Data Berhasil Dikirim!", "success");
        $(".confirm").click(function() {
          window.location.href = "/hak_akses_pengguna";
        });
      } else if(data.rc == "08" || data.rc == '08') {        
        swal("Gagal!", "Kode Hak Akses Sudah Ada", "warning");
        $(".confirm").click(function() {
          $('.btn-save-form').prop("disabled", false);
        }); 
      }else{
        swal("Gagal!", "Kode Hak Akses Terlalu Pendek", "warning");
        $(".confirm").click(function() {
          $('.btn-save-form').prop("disabled", false);
        }); 
      }
      // $(this).attr("disabled", false);
    }).fail(function () {
      $(this).attr("disabled", false);
      swal("Gagal!", "Data Gagal Dikirim!", "warning");
    });
  }  
});

btnBatal.addEventListener("click", function () {
  window.location.href = "/hak_akses_pengguna";
});

// const uppercaseKodeRole = function () {
//   temp_kd = $("input[name=kode_role]").val();
//   temp_kd = temp_kd.replace(/\s+/g, "");
//   temp_kd = temp_kd.toUpperCase();
//   $("input[name=kode_role]").val(temp_kd);
//   kode_role = temp_kd;
// };