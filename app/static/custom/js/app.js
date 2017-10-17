function start()
{
  $('#start').click(function(e){
    e.preventDefault()
      $('#actual_result_add').val("")
      $.ajax({
          url: '/add/rule/1/count_of_numbers/2',
          type: "POST",
          dataType: 'json'
        }).done( function(data) {
          console.log(data)
                if (data.success == true) { //if your response have 'status' key
                 console.log(data.formula)
                 $('#formula_add').text(data.formula + "=")

                 $('#add').click(function(e){
                   actual_result = $('#actual_result_add').val()
                   console.log(actual_result)
                   console.log(data.expected_result)
                   e.preventDefault()
                   if (actual_result == data.expected_result){
                     $("#results_add").html('<font color="Green"> Well Done！</font>');
                     start();
                   }
                   else{
                     $("#results_add").html('<font color="Red"> Sorry, Incorrect, please retry!</font>');
                   }
                  }
                )
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
