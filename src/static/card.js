$(document).ready(function(){
    var card;
    var uid = $("#uid").text();
    var setCardInfo = function() {
        window.descContent = card.name+"的微名片，您可以存入名片夹、回赠名片或分享给朋友";
        window.shareTitle = card.name+"的微名片";
        if(window.location.href.indexOf("set") != -1) {
            window.lineLink = "http://tjuthelper.duapp.com/card/"+uid;
        }
        else
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

    var setButton = function() {
        $.ajax({
            url: "/hascard/"+uid,
            type: "GET",
            success: function (data) {
                if(data == "true") {
                    $("#addcard").hide();
                    $("#delcard").show();
                }
                else if(data == "false") {
                    $("#addcard").show();
                    $("#delcard").hide();
                }
            }
        });
    };


    $("#addcard").click(function() {
        $.ajax({
            url: "/add/"+uid,
            type: "GET",
            success: function (data) {
                if(data == "true") {
                    setButton();
                }
            }
        });
    });
    $("#delcard").click(function() {
        $.ajax({
            url: "/del/"+uid,
            type: "GET",
            success: function (data) {
                if(data == "true") {
                    setButton();
                }
            }
        });

    });
    setButton();
    getCardInfo();
});

