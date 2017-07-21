$(function() {
    $("[id^=section]").hide();
    $("#section-1").show();
    $.ajax({
        url: "http://localhost:8000/api/series/"
    }).then(function(data) {
        console.log(JSON.stringify(data));
        $('#result').html(data[0].name);
    }).fail(function() {
        $('#result').html("Error");
        alert(2);
    });
});
function show_section(section) {
    $("[id^=section]").hide();
    $("#section-"+section).show();
}
