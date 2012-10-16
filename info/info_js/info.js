$(document).ready(function() 
{
	

	/*初始化用户信息*/
	/*初始化性别信息*/
	var sex = $('#sex_default').text();
	if(sex == 'M')
	{
		$('#male').attr('checked', 'true');
	}
	else
	{
		$('#female').attr('checked', 'true');
	}
	/*初始化生日信息*/
	var birth_year = $('#year_default').text();
	if(birth_year != '' && birth_year != null)
	{
		$('#birth_year').attr('value', birth_year);
	}

	var birth_month = $('#month_default').text();
	if(birth_month != '' && birth_month != null)
	{
		$('#birth_month').attr('value', birth_month);
	}
	var birth_day = $('#day_default').text();
	if(birth_day != '' && birth_day != null)
	{
		$('#birth_day').attr('value', birth_day);
	}
	/*初始化学校信息*/
	var type = $('#type_default').text();
	var type_value = '3';
	if(type != '' && type != null && type.length < 2)
	{
		
		switch(type)
		{
		case 'P':
			tyep_value = '1';
			break;
		case 'S':
			tyep_value = '2';
			break;
		case 'H':
			tyep_value = '3';
			break;
		case 'T':
			tyep_value = '4';
			break;
		case 'J':
			tyep_value = '5';
			break;
		case 'O':
			tyep_value = '6';
			break;
		default:
			break;
		}
		
	}
	$('#school_type').attr('value', type_value);
	set_grade();
	var school_grade = $('#grade_default').text();
	//alert('hello');
	if(school_grade != null && school_grade != '')
	{
		$('#grade').attr('value', school_grade);
	}
	
	/*********************************************/

	

	$('#school_type').change(function()
	{
		set_grade();
	});

	$('#birth_year').change(function()
	{
		set_day();
	});

	$('#birth_month').change(function()
	{
		set_day();
	});

	/*使用ajax进行用户信息传输*/
	$('#submit').click(function()
	{
		return commit();
	});

	/********************************************/
	
	function set_day()
	{	
		var month = $('#birth_month option:selected').val();
		var year = $('#birth_year option:selected').val();
		var day = $('#birth_day option:selected').val();
		var day29 = $("#birth_day option:contains('29')");
		var day30 = $("#birth_day option:contains('30')");
		var day31 = $("#birth_day option:contains('31')");
		day29.show();
		day30.show();
		day31.show();
		if(month == 4 || month == 6 || month == 9 || month == 11)
		{
			day31.hide();
			if(day == 31)
			{
				//alert('hello');
				$('#birth_day').attr('value', '30');
			}
		}
		if(month == 2)
		{
			if(year == year / 4 * 4 && year != year / 100 * 100)
			{
				day31.hide();
				day30.hide();
				if(day >= 30)
					$('#birth_day').attr('value', '29');
			}
			else
			{
				day31.hide();
				day30.hide();
				day29.hide();
				if(day >= 29)
					$('#birth_day').attr('value', '28');
			}
		}
	}

	function set_grade()
	{
		/*设置显示Grade的内容*/
		var grade = $('#grade');
		var school_type = $('#school_type option:selected').text();
		//alert(school_type);
		/*清空年级选项*/
		grade.html('');
		//alert('ok1');
		grade.show();
		//alert('ok1');
		if(school_type == '小学')
		{
			var primary = ["1年级", "2年级", "3年级", "4年级", "5年级", "6年级", "老师"];
			var values = [1, 2, 3, 4, 5, 6, 7];
			$.each(primary, function(index, value)
			{
				grade.append('<option value='  + values[index] + '>' + value + '</option>');
			});
		}
		else if(school_type == '中学')
		{
			var second = ["初一", "初二", "初三", "初四", "高一", "高二", "高三", "老师"];
			var values = [1, 2, 3, 4, 5, 6, 7, 8];
			$.each(second, function(index, value)
			{
				grade.append('<option value=' + values[index] + '>' + value + '</option>')
			});
		}
		else if(school_type == '大学')
		{
			//alert('ok');
			var high = ['大一', '大二', '大三', '大四', '硕士', '博士', '老师'];
			var values = [1, 2, 3, 4, 5, 6, 7];
			$.each(high, function(index, value)
			{
				grade.append('<option value=' + values[index] + '>' + value + '</option>');
			});
			//alert('ok');
		}
		else if(school_type == '中专' || school_type == '大专')
		{
			var major = ['专一', '专二', '专三', '专四', '专五', '教师'];
			var values = [1, 2, 3, 4, 5, 6];
			$.each(major, function(index, value)
			{
				grade.append('<option value=' + values[index] + '>' + value + '</option>');
			});
		}
		else
		{
			grade.hide();
		}
	}

	function commit()
	{
		var r_name = $('#r_name_input').val();
		var sex = 'M';
		if($('#female').attr('checked'))
		{
			sex = 'F';
		}
		var birth_year = $('#birth_year').val();
		var birth_month = $('#birth_month').val();
		var birth_day = $('#birth_day').val();
		var school_type = $('#school_type').val();
		var school_name = $('#school_name').val();
		var school_grade = $('#grade').val();
		var data = 'r_name=' + r_name + '&sex=' + sex + '&birth_year=' + birth_year +
			'&birth_month=' + birth_month + '&birth_day=' + birth_day + '&school_type=' + school_type
			+ '&school=' + school_name + '&grade=' + school_grade;
		$.ajax(
		{
			type: "POST",
			url: "/info/",
			data: data,
			success: function(html)
			{
				alert(html);
			}

		}); 
		return false;
	}
	
});