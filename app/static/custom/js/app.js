function start_add_minus(selector) {
    // $("#actual_result").html('');
    $("#expected_result").html("")
    $('#user_result').val("")
    $('#user_result').focus();
    var digits = $("#digits").val()
    var rule = $("#rule").val()
    var count_of_numbers = $("#count_of_numbers").val()
    var rule_id = rule.split(":")[0]
    console.log(count_of_numbers)
    $("#rule_desc").html(rule)
    $("#btnSetup").attr({
        "href": "#setup-modal"
    })
    if (selector.indexOf("add")) {
        $("#operation_title").text("速算：加法")
        calc_type = "add"
    }
    if (selector.indexOf("minus") != -1) {
        $("#operation_title").text("速算：减法")
        calc_type = "minus"
    }
    var url = "/" + calc_type + "/rule/" + rule_id + "/count_of_numbers/" + count_of_numbers + "/digits/" + digits
    console.log("url is: ", url)
    $.ajax({
        url: url, //'/add/rule/1/count_of_numbers/2',
        type: "POST",
        dataType: 'json'
    }).done(function (data) {
        on_finish(data, selector)
    })
}

function start_multiply(selector) {
    // $("#actual_result").html('');
    $("#expected_result").html("")
    $('#user_result').val("")
    $('#user_result').focus();
    var rule = $("#multiply_rule").val()
    var count_of_numbers = $("#multiply_count_of_numbers").val()
    var rule_id = rule.split(":")[0]
    console.log("rule id is: " + rule_id)
    $("#rule_desc").html(rule)
    $("#btnSetup").attr({
        "href": "#setup-multiply-modal"
    })
    if (selector.indexOf("multiply") != -1) {
        $("#operation_title").text("速算：乘法")
        calc_type = "multiply"
    }
    if (selector.indexOf("divide") != -1) {
        $("#operation_title").text("速算：除法")
        calc_type = "divide"
    }

    var url = "/" + calc_type + "/rule/" + rule_id
    console.log("url is: ", url)
    $.ajax({
        url: url, //'/add/rule/1/count_of_numbers/2',
        type: "POST",
        dataType: 'json'
    }).done(function (data) {
        on_finish(data, selector)
    })
}


function on_finish(data, selector) {
    $("#actual_result").html("")
    var start_time = new Date().getTime();
    if (data.success == true) { //if your response have 'status' key
        $('#formula').text(data.formula + " = ")
        $('#user_result').unbind() // otherwise keypress will be invoked multiple times
        $('#user_result').bind("keydown", function (e) {
            if (e.which == 13) {
                 var end_time = new Date().getTime();
                 var duration = (end_time - start_time) / 1000;
                //  $('#add').click(function(e){
                actual_result = $('#user_result').val()
                e.preventDefault()
                var number = 1 + Math.floor(Math.random() * 6);
                if (actual_result == data.expected_result) {

                    //   $("#actual_result").html('<i class="glyphicon glyphicon-ok text-success"></i>');
                    showAlert("#actual_result", "success", '<i class="glyphicon glyphicon-ok text-success">用时：' + duration + '</i>')

                    //  $("#btnSuccessMessage").click()
                    //  window.setTimeout(function (){
                    //    alert("congratuations").close()
                    //  }, 1000)
                    //   $('#success_dialog').html("congratulations")


                    history_tag_to_insert = '<pre><font color="Green">' + data.formula + " = " + actual_result + '              <span class="glyphicon glyphicon-ok text-success"></span> <span> 用时：' + duration + 's</span></font></pre>'
                    $("<div id=" + actual_result + "_" + number + ">" + history_tag_to_insert + "</div>").insertBefore(history_tag)
                    history_tag = "#" + actual_result + "_" + number
                    console.log("selector is: " + selector)
                    $(selector).click()
                }
                else {
                    $("#actual_result").html('<br><font color="Red"><i class="glyphicon glyphicon-remove text-fail"></i></font');
                    history_tag_to_insert = '<pre><font color="Red">' + data.formula + " = " + actual_result + '              <span class="glyphicon glyphicon-remove text-fail"></span></font></pre>'
                    $("<div id=" + actual_result + "_" + number + ">" + history_tag_to_insert + "</div>").insertBefore(history_tag)
                    history_tag = "#" + actual_result + "_" + number
                    $("#expected_result").html('<h4><a id="hint">查看正确答案</a></h4>')

                    $("#hint").click(function (e) {
                        e.preventDefault()
                        $("#expected_result").html('<h4><p> 正确答案是: ' + data.expected_result + '</h4>');
                    })
                }
            }
        })
    } else {
        message = ""
        if (data.message instanceof Object) {
            $.each(data.message, function (index, element) {
                message += element + "<br>"
            });
        }
        else {
            message = data.message
        }
        $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> ' + message + '</i></label>');

    }
}

function setup(calc_type, start_selector) {
    $.ajax({
        url: "/" + calc_type + "/setup",
        type: "POST",
        dataType: 'json',
        data: $("#setup_form").serialize()
    }).done(function (data) {
        $(".result").html('<label class="result col-sm-10"><i class="glyphicon glyphicon-ok text-success"> ' + data.message + '</i></label>');

        $("#rule_desc").html(data.rule_summary + "<br>" + data.rule_desc)
        $("#setup_close").click(function (e) {
            e.preventDefault()
            $("#rule_desc").html(data.rule_summary + "<br>" + data.rule_desc)
            $(start_selector).click()
        })

        // $('#setup-modal').on('hidden', function (e) {
        //     alert("run")
        //     e.preventDefault()
        //     console.log(data.url);
        //     console.log($("#digits").val())
        //     $("#rule_desc").html(data.rule_desc)
        //    // $(start_selector).click()//'/minus/rule/1/count_of_numbers/2'),
        //     })
    });
}

function setup_multiply(calc_type, start_selector) {
    $.ajax({
        url: "/" + calc_type + "/setup",
        type: "POST",
        dataType: 'json',
        data: $("#setup_multiply_form").serialize()
    }).done(function (data) {
        $("#rule_desc").text(data.rule_desc)
        $(".result").html('<label class="result col-sm-10"><i class="glyphicon glyphicon-ok text-success"> ' + data.message + '</i></label>');
        $("#setup_multiply_close").click(function (e) {
            e.preventDefault()
            console.log(data.rule_summary + "<br>" + data.rule_desc)
            $("#rule_desc").html(data.rule_summary + "<br>" + data.rule_desc)
            start_multiply(start_selector)
        })
        // $('#setup-multiply-modal').on('hidden', function (e) {
        //     e.preventDefault()
        //     console.log(data.url);
        //     console.log($("#digits").val())
        //     $("#rule_desc").html(data.rule_desc)
        //     $(start_selector).click()//'/minus/rule/1/count_of_numbers/2'),
        //
        // });
    })
}

function login() {
    $.ajax({
        url: '/login',
        type: "POST",
        dataType: 'json',
        data: $("#login_form").serialize()
    }).done(function (data) {
        console.log(data)
        if (data.success == true) { //if your response have 'status' key
            $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-ok text-success">登录成功</i></label>');
            $("#login_close").click(function (e) {
                e.preventDefault()
                Cookies.set("username", data.username)
                window.location.href = "/"
            })
            // $('#login-modal').on('hidden', function (e) {
            //     e.preventDefault()
            //     $(function () {
            //         // $.session.set("username", data.username);
            //         Cookies.set("username", data.username)
            //     });
            //     window.location.href = "/"
            // })
        } else {
            message = ""
            if (data.message instanceof Object) {
                $.each(data.message, function (index, element) {
                    message += element + "<br>"
                });
            }
            else {
                message = data.message
            }
            $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> ' + message + '</i></label>');

        }
    })
}

function register() {
    $.ajax({
        url: '/register',
        type: "POST",
        dataType: 'json',
        data: $("#register_form").serialize()
    }).done(function (data) {
        if (data.success == true) { //if your response have 'status' key
            console.log("Registered Successfully, Please login", 2)
            $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-ok text-success"> ' + data.message + '</i></label>');

            $('#register-modal').on('hidden', function (e) {
                e.preventDefault()
                $(function () {
                    $("#login-modal").dialog({modal: true});
                });
            })
        } else {
            message = ""
            if (data.message instanceof Object) {
                $.each(data.message, function (index, element) {
                    message += element + "<br>"
                });
            }
            else {
                message = data.message
            }
            $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> ' + message + '</i></label>');

        }
    })
}

function showAlert(containerId, alertType, message) {
    $(containerId).append('<p><div id="temp" class="alert alert-' + alertType + '" id="alert' + containerId + '">' + message + '</div>');
    $("#alert" + containerId).alert();
    // window.setTimeout(function () { $("#alert" + containerId).alert('close'); }, 1000);
    window.setTimeout(function () {
        $("#temp").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 3000);
}

function countdowntimer() {
        $("#ms_timer").countdowntimer({
            minutes: 20,
            seconds: 10,
            size: "lg"
        });
}