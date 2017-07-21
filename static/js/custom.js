var token = 'a7fa56bf3402eced502c7a50158da8c97efecdd3';

$(function() {
    $("#section-1").show();
    $('#main-table').DataTable( {
      "ajax": {
          url: "/api/ticket_list/",
          headers: {
              Authorization:"Token "+token
          },
          type: "POST",
          data: function ( d ) {
              return $.extend( {}, d, {
                  // date: $("select[id='flt-date']").val(),
              } );
          },
          dataSrc: function ( json ) {
              for ( var i=0, ien=json.length ; i<ien ; i++ ) {
                  json[i].links = "<a href=\"javascript:void(0)\" onclick=\"get_ticket('" + json[i].id + "' )\"><i style=\"margin-left:5px\" class=\"fa fa-edit link-icons\"></i> Edit</a>";
              }
              return json;
          }
      },
      columns: [
          { "data": "links"},
          { "data": "order"},
          { "data": "created"},
          { "data": "priority"},
          { "data": "problem"},
          { "data": "status"},
          { "data": "agent"},
      ],
      paging:false,
      "ordering": false,
      columnDefs: [
          { targets: [0], "searchable": false, width: "60px", className: "cell-centered"},
      ],
      buttons: {
        buttons: [
          {extend:'pdf', className: 'btn btn-default btn-sm'}, 
        ],
      },
      dom: 'lftiBp',
    } );

    $.ajax({
        type: "GET",
        url: "http://localhost:8000/api/ticket_priorities/",
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
        $.each(data, function (i, item) {
            $('#id_priority').append($('<option>', { 
                value: item.id,
                text : item.name 
            }));
        });
    }).fail(function() {
         alert("Error");
    });

    $.ajax({
        type: "GET",
        url: "http://localhost:8000/api/ticket_problems/",
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
        $.each(data, function (i, item) {
            $('#id_problem').append($('<option>', { 
                value: item.id,
                text : item.name 
            }));
        });
    }).fail(function() {
         alert("Error");
    });
});

function show_section(section) {
    $("[id^=section]").hide();
    $("#section-"+section).show();
    if (section==1) {
        $('#main-table').DataTable().ajax.reload();
    }
}

function create_ticket(){
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/ticket_create/",
        data:{
          order_number:$('#id_order_number').val(),
          priority:$('#id_priority').val(),
          problem:$('#id_problem').val(),
          description:$('#id_description').val()
        },
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
        show_section(1);
    }).fail(function() {
         alert("Error");
    });
}

function get_ticket(id){

}

function answer_ticket() {
    // body...
}

function close_ticket() {
    // body...
}