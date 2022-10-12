"use strict";
const btnTambah = document.querySelector(".btn-tambah");
const btnSimpan = document.querySelector(".btn-save-form");
const btnBatal = document.querySelector(".btn-batal");

let kode_role = null;
let nama_role = "";
let role = [];
let temp_kd = "";
let child_id = "None";
let parent_id = "None";
let roleBody = {};
let data;
let kode;
let url;
let urlEdit;
let url_string;
let checkbox;
let checkbox2;
let checkbox3;
let checkbox4;
let p_id;
let arr = [];
let index;
let iChild;
let arrChild = [];
let childLog = [];
let roleChild = {};
let logParent;
let arrLog = [];
let arrTiket = [];
let arrMaster = [];
var g = [];
var parent_cek = [];
var child_cek = [];

roleBody = {
  child_id: child_id,
  parent_id: parent_id,
};

var count = $('.count_parent').val();

$(document).ready(function () {
  
  // get param kode
  url_string = window.location.href;
  url = new URL(url_string);
  kode = url.searchParams.get("kode");
  $("[name=kode_role]").attr("disabled", "").val(kode);

  // get data by url
  // urlEdit = `/hak_akses_pengguna_edit/req2?kode=${kode}`;

  // get data by url
  urlEdit = `/hak_akses_pengguna_edit/req?kode=${kode}`;
  $.get(urlEdit, function (res) {
    // console.log(res);
    let {roles: [first]} = res;
    let roleObj = JSON.parse(first.role);
    // console.log(JSON.parse(first.role));
    $("[name=nama_user]").val(first.username);
    $("[name=password]").val(first.password);

    // looping parent
    for (let x = 1; x <= count; x++) {
      // centang box parent
      $(`input[name="parent_id${x}"]`).each(function () {
        for (let y = 0; y < roleObj.length; y++) {
          if ($(this).val() == roleObj[y].parent_id) {
            // console.log(roleObj[y].parent_id);
            // centang box child aktivitas
            // console.log(x);
            if (roleObj[y].child_id != "None") {
              if (roleObj[y].parent_id == ''+x+'' || roleObj[y].parent_id == x) {
                for (let i = 0; i < roleObj[y].child_id.length; i++) {
                  childLog.push(Number(roleObj[y].child_id[i].id));
                }
              }
            }
            $(this).attr("checked", "checked");
          }
          for (let z = 0; z <= 100; z++) {
            $('.child'+x+'')
              .find(`.child_id${z}`)
              .each(function () {
                for (let i = 0; i < childLog.length; i++) {
                  if ($(this).val() == childLog[i]) {
                    $(this).attr("checked", "checked");
                  }
                }
              });
          }
          childLog = [];
        }
      });
    }
  })
    .fail(function () {})
    .always(function () {});

  $('[name="parent_id1"]').prop('disabled', true);
  
});

btnSimpan.addEventListener("click", function (e) {
  for (let x = 1; x <= count; x++) {
    $(`input[name="parent_id${x}"]`).each(function () {
        checkbox3 = $(this);
        if(child_cek[0] == 1 || child_cek[0] == undefined){
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
        }
      });
  }

  if (child_cek[0] == 0){
    swal("Gagal!", "Pilih Menu Utama dan Sub Menu", "warning");
    child_cek = [];
    e.preventDefault();
  }else{
    $(this).attr("disabled", true);
    // uppercaseKodeRole();
    nama_role = $("[name=nama_role]").val();

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
      id: kode,
      role: JSON.stringify(role)
    };
    
    url = "/hak_akses_pengguna_edit/put";
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
        swal("Gagal!", "Data Gagal Dikirim", "warning");
        $(".confirm").click(function() {
          $('.btn-save-form').prop("disabled", false);
        }); 
      }
    }).fail(function () {
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