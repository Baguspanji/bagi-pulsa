
    $(function()
    {

        //do stuff
        console.log('required plugins loaded...');

        //jQuery Captcha Validation

        WEBAPP = {

            settings: {},
            cache: {},

            init: function() {

                //DOM cache
                this.cache.$form = $('#captcha-form');
                this.cache.$refreshCaptcha = $('#refresh-captcha');
                this.cache.$captchaImg = $('img#captcha');
                this.cache.$captchaInput = $(':input[name="captcha"]');

                this.eventHandlers();
                // this.setupValidation();

            },

            eventHandlers: function() {

                //generate new captcha
                WEBAPP.cache.$refreshCaptcha.on('click', function(e)
                {
                    // console.log("terklik");
                    // WEBAPP.cache.$captchaImg.attr("src","Captcha/new_captcha?rnd=" + Math.random());
                    getCaptcha();
                });
            }
            // ,

            // setupValidation: function()
            // {

            //     WEBAPP.cache.$form.validate({
            //        onkeyup: false,
            //        rules: {
            //             "username": {
            //                 "required": true
            //             },
            //             "password": {
            //                 "required": true
            //             },
            //             "captcha": {
            //                 "required": true,
            //                 "remote" :
            //                 {
            //                   url: 'Captcha/check_captcha',
            //                   type: "post",
            //                   data:
            //                   {
            //                       code: function()
            //                       {
            //                         console.log(WEBAPP.cache.$captchaInput.val());
            //                           return WEBAPP.cache.$captchaInput.val();
            //                       }
            //                   }
            //                 }
            //             }
            //         },
            //         messages: {
            //             "captcha": {
            //                 "required": "Please enter the verifcation code.",
            //                 "remote": "Verication code incorrect, please try again."
            //             }
            //         },
            //         submitHandler: function(form)
            //         {
            //             /* -------- AJAX SUBMIT ----------------------------------------------------- */
            //             console.log("submitHandler");
            //             var submitRequest = $.ajax({
            //                  type: "POST",
            //                  url: "Login/aksi_login",
            //                  data: {
            //                     "data": WEBAPP.cache.$form.serialize()
            //                 }
            //             });

            //             submitRequest.done(function(msg,y,z)
            //             {
            //                 console.log(msg);
            //                 //redirect
            //                 //success
            //                 // console.log("submitReques Done");
            //                 // console.log('success');
            //                 // $.post("Login/aksi_login",function($data){

            //                 // });
            //                 // ajax login

            //             });

            //             submitRequest.fail(function(jqXHR, textStatus)
            //             {
            //                 //fail
                            
            //                 console.log( "fail - an error occurred: (" + textStatus + ")." );
            //                 captcha_gagal();
            //             });

            //         }

            //     });

            // }

        }

        WEBAPP.init();

    });

    function captcha_gagal(){

    }