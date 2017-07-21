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

function show_section(section) {
    $("[id^=section]").hide();
    $("#section-"+section).show();
    if (section==1) {
        $('#main-table').DataTable().ajax.reload();
    }
    if (section==2) {
        $('#closed-table').DataTable().ajax.reload();
    }
}
