$(document).ready(function()
{
	//alert('hello');
	var writing = false;
	var sayIds;// = new Array();
	var PAGE_MAX = 200;
	var total_pages = 0;
	var now_page = 0;

	fetchall();

	$("#say_input").focus(function()
	{
		var area = $("#say_input");
		//alert("hello");
		if(writing)
			return;
		area.attr('value', '');
		area.animate({height : "100px"}, '1000');
		writing = true;
	});

	$("#submit").click(function()
	{
		if(!writing)
			return;
		writing = false;
		var say_text = $("#say_input").val();
		$("#say_input").animate({height : "50px"}, '1000');
		if(say_text == '' || say_text == null)
		{
			$("#say_input").attr("value", '发布说说');
			return;
		}
		$.ajax(
		{
			type: "post",
			data: "say=" + say_text,
			url: "/public_say/",
			success: function(html)
			{
				$('#say_input').attr('value', html);
				window.setTimeout(function()
				{
					$('#say_input').attr('value', '发布说说');
				}, 1000);
				get_last_one();
			}

		});

	});

	$('#friends_say').click(function(event)
	{

	});

	//获得好友最近的说说
	function get_friend_says()
	{
		$.ajax(
		{
			type:'GET',
			url:'/get_friend_says/',
			success:function()
			{
				
			}
		});
	}

	function fetchall()
	{
		/*获取所有的说说号*/
		$.ajax(
		{
			type:"post",
			url:/all_say/,
			success: function(html)
			{
				var json = eval('(' + html + ')');
				if(json.error == 'Y')
				{
					alert(json.info);
					return;
				}
				else
				{
					sayIds = json.sayIds;
					if(sayIds.length <= PAGE_MAX)
					{
						var data = '';
						for(i = 0; i < sayIds.length; i ++)
						{
							data += sayIds[i] + ',';
						}
						var m = sayIds[i];
						//请求说说的内容
						$.ajax(
						{
							type: 'GET',
							url: /get_says/,
							data:'sayIDs=' + data,
							success:function(html)
							{
								//alert(html);
								html = security(html);
								//解析服务器的数据
								reponse = eval('(' + html + ')');
								//发生错误
								if(reponse.error == 'Y')
								{
									alert(reponse.info);
									return;
								}
								//请求的一些说说
								var says = reponse.says;
								//显示到界面上
								$('#all_say').html('');
								for(i = 0; i < says.length; i ++)
								{
									var tmp ='<div class="a_say" id="' + says[i].sayId + '"><div class="a_say_text">'
										+ change_to_quote(says[i].sayText)
										+ '</div><div class="a_say_time">' + says[i].time + '</div></div>';
									$('#all_say').append(tmp); 
								}
							}
						});
					}
					else
					{

					}
				}
			}
		});
	}

	function generate_index(num)
	{
		var ret = '<a id="page_up">上一页</a>';
		now_page = 1;
		total_pages = num / PAGE_MAX;
		if(num != PAGE_MAX * total_pages)
			total_pages ++;
		for(var i = 1; i <= total_pages; i ++)
			ret += '<a class="page">' + i + '</a>';
		ret += '<a id="page_down">下一页</a>';
		return ret;
	}

	//对用户的说说的内容进行安全处理
	function security(html)
	{
		html = html.replace(new RegExp("<", "gm"), "&lt;");
		html = html.replace(new RegExp("\n","gm"),"<br/>");
		return html;
	}
	//将'`'转换为单引号
	function change_to_quote(html)
	{
		return html.replace(new RegExp("`", "gm"), '\'');
	}

	function get_last_one()
	{
		$.ajax(
		{
			type:"get",
			url: "/get_last_one/",
			success:function(html)
			{
				if(html == '' || html == null)
					return;
				html = security(html);
				last_one = eval('(' + html + ')');
				var tmp ='<div class="a_say" id="' + last_one.sayId + '"><div class="a_say_text">' 
						+ change_to_quote(last_one.sayText)
						+ '</div><div class="a_say_time">' + last_one.time + '</div></div>';
				$('#all_say').prepend(tmp);
			}
		});
	}

})