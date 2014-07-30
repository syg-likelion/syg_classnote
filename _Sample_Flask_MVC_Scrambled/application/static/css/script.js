
	$("[name='email']").change(function(){
		if ($(this).val().match(/[\w\d._]+@[\w\d-]+\.(\w{2,3}|\w{2}\.\w{2})/)) $('#email').hide()
		else $('#email').show()
	});
	$("[name=password]").change(function(){
		if ($(this).val().match(/(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!#\$%&\?])/)) $('#password').hide();
		else $('#password').show();
	});
	$("[name=password_check]").change(function(){
		if ($(this).val()!=$("[name=password]").val()) $('#password_check').show();
		else $('#password_check').hide();
	});

	$("[name=email]").change(function(){
		var email = $("[name=email]").val();
		$.ajax({
			url:'/check_email',
			type:'POST',
			data:{"email":email},
			success:function(response){
			},
			error:function(){
			},
			complete:function(){
				console.log(response)
				var result = $.parseJSON(response);
				console.log(result['message']);

				if(result['message'] == 'ok'){
					$('#check_email').hide();
				}else{
					$('#check_email').show();
				}
			} 
		});
	});
});