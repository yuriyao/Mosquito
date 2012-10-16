$(document).ready(function()
{
	$('#submit').click(function(event)
	{
		var u_name = $('#u_name_input').val();
		var u_pwd = $('#u_pwd_input').val();
		var u_confirm = $('#u_confirm_input').val();
		var u_email = $('#u_email_input').val();

		var result = true;
		/*检测用户名是否合法*/
		if(u_name.length < 5 || u_name.length > 15)
		{
			result = false;
			$('.error:eq(0)').text('用户名应该由5到15个字符组成');
		}
		else if(!is_valid(u_name))
		{
			result = false;
			$('.error:eq(0)').text('用户名包含不合法字符（只能由字母、数字、下划线组成）');
		}
		else
			$('.error:eq(0)').text('');
		/*检测密码是否合法*/
		if(u_pwd.length < 5 || u_pwd.length > 30)
		{
			result = false;
			$('.error:eq(1)').text('密码应该由5到30个字符组成');
		}
		else if(!is_valid(u_pwd))
		{
			result = false;
			$('.error:eq(1)').text('密码包含不合法字符（只能由字母、数字、下划线组成）');
		}
		else
			$('.error:eq(1)').text('');
		/*检测确认密码是否合法*/
		if(u_confirm != u_pwd)
		{
			result = false;
			$('.error:eq(2)').text('两次密码不相同');
		}
		else
			$('.error:eq(2)').text('');
		/*检测e-mail是否合法*/
		if(!is_valid_emial(u_email))
		{
			result = false;
			$('.error:eq(3)').text('e-mail不符合规范');
		}
		else
			$('.error:eq(3)').text('');
		if(!result)
		{
			event.preventDefault();
		}

		function is_valid(str)
		{
			len = str.length;
			for(i = 0; i < len; i ++)
			{
				if(!is_valid_ch(str[i]))
				{
					return false;
				}		
			}
			return true;
		}

		function is_valid_ch(ch)
		{
			if((ch >= '0' && ch <= '9') || (ch >= 'a' && ch <= 'z')
					|| (ch >= 'A' && ch <= 'Z') || ch == '_')
				return true;
			return false;
		}

		function is_valid_emial(email)
		{
			var reg = new RegExp('^([a-zA-Z0-9_])+@([a-zA-Z0-9_])+((\.[a-zA-Z0-9_]{2,3}){1,2})$');
			return reg.test(email);
		}
	});
});
