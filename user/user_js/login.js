$(document).ready(function()
{
	$('#submit').click(function(event)
	{
		var u_name = $('#u_name_input').val();
		var u_pwd = $('#u_pwd_input').val();
		/*字符串长度验证*/
		if(u_name.length < 1 || u_pwd.length < 1)
		{
			$('#error').text('用户名和密码都不能为空');
			event.preventDefault();
		}
		/*用户名和密码字符串的合法性验证*/
		else
		{
			if(!is_valid(u_name) || !is_valid(u_pwd))
			{
				$('#error').text('用户名或者密码包含不合法字符（只能由字母、数字、下划线组成）');
				event.preventDefault();
			}
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
	});
});
