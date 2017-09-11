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
            url: "",
            type: "POST",
            data: {"username": username, "email": email, "password": password, "yzm": yzm},
            cache: false,
            dataType: "html",
            success: function(data) {
                alert(data);
            },
            error: function() {
                alert("请求失败");
            }
        })
    });
});