function load(){
    $("#section-1").show();
    $('#main-table').DataTable( {
      "ajax": {
          url: "/api/pending_ticket_list/",
          type: "POST",
          headers: {
              Authorization:"Token "+token
          },
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
      destroy:true,
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

    $('#closed-table').DataTable( {
      "ajax": {
          url: "/api/closed_ticket_list/",
          type: "POST",
          headers: {
              Authorization:"Token "+token
          },
          data: function ( d ) {
              return $.extend( {}, d, {
                  // date: $("select[id='flt-date']").val(),
              } );
          },
          dataSrc: function ( json ) {
              for ( var i=0, ien=json.length ; i<ien ; i++ ) {
                  json[i].links = "<a href=\"javascript:void(0)\" onclick=\"get_ticket('" + json[i].id + "' )\"><i style=\"margin-left:5px\" class=\"fa fa-edit link-icons\"></i> View</a>";
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
      destroy:true,
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
        url: "/api/ticket_priorities/",
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
        url: "/api/ticket_problems/",
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

}

function get_ticket(id){
   $.ajax({
        type: "POST",
        url: "/api/get_ticket/",
        data:{
          id:id
        },
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
        $("#ticket_id").val(data.id);
        $("#ticket_answer").val('');
        $("#ticket_created_date").html(data.created);
        $("#ticket_closed_date").html(data.closed);
        $("#ticket_order_number").html(data.order);
        $("#ticket_created_by").html(data.created_by);
        $("#ticket_priority").html(data.priority);
        $("#ticket_problem").html(data.problem);
        $("#ticket_description").html(data.description);
        $("#ticket_status").html(data.status);
        $("#ticket_assigned_to").html(data.agent);
        if ((data.status=="Open") || (data.status=="Client-Reply")) {
          $("#answer-box").show();
        } else {
          $("#answer-box").hide();
        }
        show_section(4);
    }).fail(function() {
         alert("Error");
    });
}

function answer_ticket() {
   $.ajax({
        type: "POST",
        url: "/api/answer_ticket/",
        data:{
          id:$('#ticket_id').val(),
          answer:$('#ticket_answer').val()
        },
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
      get_ticket($('#ticket_id').val());
    }).fail(function() {
         alert("Error");
    });
}

function close_ticket() {
   $.ajax({
        type: "POST",
        url: "/api/close_ticket/",
        data:{
          id:$('#ticket_id').val(),
          answer:$('#ticket_answer').val()
        },
        headers: {
            Authorization: 'Token '+token
        }
    }).done(function( data ) {
      get_ticket($('#ticket_id').val());
    }).fail(function() {
         alert("Error");
    });
}