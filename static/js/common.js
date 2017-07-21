var token = '';

$(function() {
  $('#loginModal').modal();
});

function login() {
    $.ajax({
        type: "POST",
        url: "/api/get_auth_token/",
        data: {
          username:$("#id_username").val(),
          password:$("#id_password").val()
        }
    }).done(function( data ) {
        if (data.token != '') {
          token = data.token;
          $('#loginModal').modal('hide');
          load();
        }
    }).fail(function() {
         alert("Error");
    });
}

function logout() {
  token = '';
  $("[id^=section]").hide();
  $('#loginModal').modal();
}

function load_user(){
    $.ajax({
        type: "POST",
        url: "/api/load_user/",
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
        $("#id_first_name").val(data.first_name);
        $("#id_last_name").val(data.last_name);
        $("#id_email").val(data.email);
    }).fail(function() {
         alert("Error");
    });
}

function save_user(){
    $.ajax({
        type: "POST",
        url: "/api/save_user/",
        headers: {
            Authorization: 'Token '+token
        },
        data: {
          first_name: $("#id_first_name").val(),
          last_name: $("#id_last_name").val(),
          email: $("#id_email").val()
        }
    }).done(function( data ) {
      show_section('1');
    }).fail(function() {
         alert("Error");
    });
}

