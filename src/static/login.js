$(document).ready(function(){
    $("#addcard").click(function() {
        $.ajax({
            url: "/oauth",
            type: "GET",
            success: function(data) {
                if(data == "true") {
                    setButton();
                }
            }
        });
    });
});
