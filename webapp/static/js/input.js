/**
 * Created by liu on 2017/9/8.
 */
$(document).ready(function() {
    $("#signupbn").click(function () {
        var username = $("#signup_name").val();
        var email = $("#signup_email").val();
        var password = $("#signup_password").val();
        var yzm = $("#signup_yzm").val();
        $.ajax({
            url: "/login/",
            type: "POST",
            data: {"username": username, "email": email, "password": password, "yzm": yzm},
            headers: {"X-CSRFtoken": $.cookie("csrftoken")},
            success: function (data) {
                alert("ok")
            },
            error: function (data) {
                alert("ok");
            }
        })
    })
})