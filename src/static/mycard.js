$(document).ready(function(){
    var card;
    var uid = $("#uid").text();
    var setCardInfo = function() {
        window.descContent = card.name+"的微名片，您可以存入名片夹、回赠名片或分享给朋友";
        window.shareTitle = card.name+"的微名片";
        window.lineLink = window.location.href;
    }

    var getCardInfo = function() {
        $.ajax({
            url: "/get/"+uid,
            type: "GET",
            success: function (data) {
                card = JSON.parse(data);
                setCardInfo();
            }
        });
    };

    $("#editcard").click(function() {
        $("#card").hide();
        $("#editform").show();
    });

    $("#submit").click(function () {
        $.ajax({
            url: "/set",
            type: "POST",
            dataType: "text",
            data: $("form").serialize(),
            success: function (data) {
                window.location.reload();
            }
        });
        return false;
    });

    $("#sharecard").click(function() {
        mask = $("#mask").show();
        mask.click(function() {
            mask.hide();
        });
    });


    getCardInfo();
});

