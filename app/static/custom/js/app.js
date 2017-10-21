function start(operator_tag)
{
  $(operator_tag).click(function(e){
        $("#expected_result").html("")
        e.preventDefault()
          $('#user_result').val("")
          $('#user_result').focus();
          var digits = $("#digits").val()
          var rule = $("#rule").val()
          var count_of_numbers = $("#count_of_numbers").val()
          var rule_id = rule.split(":")[0]
          console.log(count_of_numbers)
          if (operator_tag.indexOf("add")) {
            $("#operation_title").text("速算 - 加法")
            calc_type = "add"
        }
          if (operator_tag.indexOf("minus") != -1) {
            $("#operation_title").text("速算 - 减法")
            calc_type = "minus"
          }
          if (operator_tag.indexOf("multiply") != -1) {
            $("#operation_title").text("速算 - 乘法")
            calc_type = "multiply"
          }
          if (operator_tag.indexOf("divide") != -1) {
            $("#operation_title").text("速算 - 除法")
            calc_type = "divide"
          }

          var url = "/" + calc_type + "/rule/" + rule_id + "/count_of_numbers/" + count_of_numbers + "/digits/" + digits
          console.log("url is: ",url)
        $.ajax({
            url: url, //'/add/rule/1/count_of_numbers/2',
            type: "POST",
            dataType: 'json'
          }).done( function(data) {
                  if (data.success == true) { //if your response have 'status' key
                   console.log(data.formula)
                   $('#formula').text(data.formula + " =")

                   $('#user_result').keypress(function (e) {
                     if (e.which == 13) {
                    //  $('#add').click(function(e){
                       actual_result = $('#user_result').val()
                       e.preventDefault()
                       var number = 1 + Math.floor(Math.random() * 6);
                       if (actual_result == data.expected_result){
                         $("#actual_result").html('<i class="glyphicon glyphicon-ok text-success"></i>');
                        history_tag_to_insert = '<font color="Green">' + data.formula + "=" + actual_result + '              <span class="glyphicon glyphicon-ok text-success"></span></font><br>'
                        $("<div id="+actual_result+"_"+number+">" + history_tag_to_insert +"</div>").insertBefore(history_tag)
                          history_tag = "#"+actual_result+"_"+number
                          console.log("susscess ---" + history_tag)
                           $(operator_tag).click()
                       }
                       else{
                         $("#actual_result").html('<font color="Red"><i class="glyphicon glyphicon-remove text-fail"></i></font');
                         history_tag_to_insert = '<font color="Red">' + data.formula + "=" + actual_result + '              <span class="glyphicon glyphicon-remove text-fail"></span></font><br>'
                        console.log(history_tag_to_insert)
                        console.log($(history_tag))
                          $("<div id="+actual_result+"_"+number+">" + history_tag_to_insert +"</div>").insertBefore(history_tag)
                          history_tag = "#"+actual_result+"_"+number
                          $("#expected_result").html('<a id="hint">check answer</a>')

                            $("#hint").click(function(e){
                              e.preventDefault()
                                $("#expected_result").html('<p> Correct answer is: ' + data.expected_result);
                            })

                    }

                }})
                } else {
                    message = ""
                    if (data.message instanceof Object){
                      $.each(data.message, function(index, element) {
                          message += element + "<br>"
                        });
                    }
                    else{
                      message = data.message
                    }
                    $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> '+message + '</i></label>');

                }
            })
        })
}


function setup(calc_type, setup_tag, url, start_tag){
  $(setup_tag).click(function(e){
    e.preventDefault()
    $.ajax({
        url: url,
        type: "POST",
        dataType: 'json',
        data: $("#setup_form").serialize()
      }).done( function(data) {
        $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-ok text-success"> '+data.message + '</i></label>');

        $('#setup-modal').on('hidden', function (e) {
          e.preventDefault()
          console.log(data.url);
          console.log($("#digits").val())
          $("#rule_desc").html(data.rule_desc)
          $(start_tag).click()//'/minus/rule/1/count_of_numbers/2'),

        });
      })
  })
}

function login(){
  $('#login').click(function(){
        $.ajax({
            url: '/login',
            type: "POST",
            dataType: 'json',
            data: $("#login_form").serialize()
          }).done( function(data) {
            console.log(data)
                  if (data.success == true) { //if your response have 'status' key
                   alert("Welcome" + data.username +", redicting you...", 2)
                   $(function() {
                          // $.session.set("username", data.username);
                        Cookies.set("username", data.username)
                        });
                   window.location.href = "/"
                } else {
                  message = ""
                  if (data.message instanceof Object){
                    $.each(data.message, function(index, element) {
                        message += element + "<br>"
                      });
                  }
                  else{
                    message = data.message
                  }
                  $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> '+message + '</i></label>');

              }
            })
        });
}

function register(){
  $('#register').click(function(){
        $.ajax({
            url: '/register',
            type: "POST",
            dataType: 'json',
            data: $("#register_form").serialize()
          }).done( function(data) {
                if (data.success == true) { //if your response have 'status' key
                   alert("Registered Successfully, Please login", 2)
                   $(function() {
                      $("#regsiter-modal").dialog({modal:false});
                        });
                   $(function() {
                      $("#login-modal").dialog({modal:true});
                        });
                } else {
                  message = ""
                  if (data.message instanceof Object){
                    $.each(data.message, function(index, element) {
                        message += element + "<br>"
                      });
                  }
                  else{
                    message = data.message
                  }
                  $(".result").html('<label class="text-danger"><i class="glyphicon glyphicon-exclamation-sign"> '+message + '</i></label>');

              }
            })
        });
}
