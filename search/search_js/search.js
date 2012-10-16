$(document).ready(function()
{
	var obj = new Array();
	var obj_len = 0;
	$('#search_submit').click(function()
	{
		$('#search_speci').show();
		$('#search_speci2').animate({height : "400px"}, '1000');
		$('#search_speci2').css('height', '400px');
		var name = $('#search_input').val();
		var data = 'search=' + name; 
		if(name == '' || name == null)
		{
			alert('搜索内容不能为空!');
			return false;
		}
		//获得好友列表
		$.ajax(
		{
			type: "GET",
			data: data,
			url:"/search/",
			success:function(html)
			{
				//alert(html);
				if(html == '[]')
				{
					$('#friends_set').text('没有找到符合条件的的好友!');
					return false;
				}
				//html = '[{"img_src":"/main_page_css/1.jpg", "school_name" : "哈尔滨工业大学", "friend_uname" : "yuri2"}]';
				var json_array = eval('(' + html + ')');
				//alert(friend_html);
				obj_len = json_array.length;
				var friend_html = '';
				//alert(friend_html);
				for(var i = 0; i < json_array.length; i ++)
				{
					obj[i] = '<img id="friend_img" src="' + json_array[i].img_src + '" >'
						+ '<span id="friend_school_name">' + json_array[i].school_name + '</span>'
						+ '<form action="/add_friend/" method="post" onsubmit="return false">'
						+ '<input type="text" name="friend_name" style="display:none;" value="' + json_array[i].friend_uname
						+ '" />' + '<input type="submit" value="+好友" class="add"></form>';
					//注册事件
					
					friend_html += obj[i];
				}
				//alert(friend_html);
				$('#friends_set').html(friend_html);
				//处理添加好友的事件
				$('.add').click(function(event)
				{
					var button = $(this);
					var search_name = $(this).parent().children('input').attr('value');//[0].attr('value');
					//alert(search_name);
					$.ajax(
					{
						type: "post",
						url: "/add_friend/",
						data: 'friendName=' + search_name,
						success:function(html)
						{
							//alert(html);
							button.attr('value', html);
						}
					});
				});
			}

		});
		return false;
	});

	//添加好友
	function add_friend()
	{	
		alert('hello');
		var search_name = $(this).attr('html');
		alert(search_name);
	}
	

	$('#handup').click(function()
	{
		$('#search_speci2').animate({height : '0px'}, '1000', function()
		{
				$('#search_speci').hide();
		});
		//
	})
	
});



