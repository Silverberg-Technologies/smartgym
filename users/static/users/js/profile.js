
$(document).ready(function() {
    $("p").click(function() {
        $(this).hide();
    });
    $("button#modeswitch").click(function() {
        $("div.viewmode").hide();
        $("div.editmode").show();
    });
});
