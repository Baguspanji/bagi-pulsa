'use strict';

$("#add_file1").click(function() {
    var form = $('#fileform1')[0];
    var file = new FormData(form);
    var c = form[0].files[0];
    if (c == undefined){
        $('#file1').addClass('invalid');
    }

    if (c.size > 1000000){
        swal("Data Besar!", "Data Max 1MB !", "warning");
    }

    if (c.size <= 1000000){
        // file.append("file", c);
        $.ajax({
        type: "post",
        url: "/banner/req1",
        data: file,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#file1').removeClass('invalid');
            swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
                $(".confirm").click(function() {
                    window.location.href = "/banner";
                });
            }
        });
    }
});

$("#add_file2").click(function() {
    var form = $('#fileform2')[0];
    var file = new FormData(form);
    var c = form[0].files[0];
    if (c == undefined){
        $('#file2').addClass('invalid');
    }

    if (c.size > 1000000){
        swal("Data Besar!", "Data Max 1MB !", "warning");
    }

    if (c.size <= 1000000){
        // file.append("file", c);
        $.ajax({
        type: "post",
        url: "/banner/req2",
        data: file,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#file1').removeClass('invalid');
            swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
                $(".confirm").click(function() {
                    window.location.href = "/banner";
                });
            }
        });
    }
});

$("#add_file3").click(function() {
    var form = $('#fileform3')[0];
    var file = new FormData(form);
    var c = form[0].files[0];
    if (c == undefined){
        $('#file3').addClass('invalid');
    }

    if (c.size > 1000000){
        swal("Data Besar!", "Data Max 1MB !", "warning");
    }

    if (c.size <= 1000000){
        // file.append("file", c);
        $.ajax({
        type: "post",
        url: "/banner/req3",
        data: file,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#file1').removeClass('invalid');
            swal("Terkirim!", "Data Berhasil Dikirim!", "success"); 
                $(".confirm").click(function() {
                    window.location.href = "/banner";
                });
            }
        });
    }
});