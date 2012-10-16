$(document).ready(function(){
	var hand_down = false;

	//获得好友请求
	get_friend_request();

	$("#quick_say").focus(function()
	{
		//$(this).css("min-height", "80px");
		if(hand_down)
			return;
		$('#quick_say').attr('value', '');
		$(this).animate({height : "100px"});
		$('#say_bottom').show();
		$('#public_say').show();
		hand_down = true;
	});

	$('#public_say').click(function()
	{
		var say = $('#quick_say').val();
		hand_down = false;
		$('#quick_say').animate({height : '40px'}, function()
		{
			$('#say_bottom').hide();
		});
		$('#quick_say').attr('value', '');
		if(say == null || say == '')
		{
			$('#quick_say').attr('value', '发布说说');
			return;
		}
			
		//存储说说
		$.ajax(
		{
			type: "post",
			data: "say=" + say,
			url: "/public_say/",
			success: function(html)
			{
				$('#quick_say').attr('value', html);
				window.setTimeout(function()
				{
					$('#quick_say').attr('value', '发布说说');
				}, 1000);
			}
		});
		
	});

	function get_friend_request()
	{
		$.ajax(
		{
			type:'get',
			url: '/get_friend_request/',
			success: function(html)
			{
				var json = eval('(' + html + ')');
				if(json.type == 'error')
				{
					alert(json.info);
					return;
				}
				else
				{
					var list = json.list;
					if(list.length == 0)
						return;
					else
					{
						for(var i = 0; i < list.length; i ++)
						{
							var show_html = '<div class="center_one" id="' + list[i].u_name + '"><div class="r_name">' + list[i].r_name
							 + '想加你为好友</div><button class="agree">同意</button><button class="disagree">拒绝</button></div>';
							$('#center').prepend(show_html);
						}
					}
				}
				//发出好友确认
				$('.agree').click(function()
				{
					var button = $(this);
					var u_name = $(this).parent().attr('id');
					var disagree = $(this).parent().children('.disagree');
					button.unbind('click');
					disagree.unbind('click');
					$.ajax(
					{
						type: 'GET',
						data: 'type=agree&friendFrom=' + u_name,
						url:'/friend_confirm/',
						success:function(html)
						{
							
							if(html != null && html != '')
							{
								alert(html);
							}

						}
					});
				});
				//
				$('.disagree').click(function()
				{
					var button = $(this);
					var u_name = $(this).parent().attr('id');
					var agree = $(this).parent().children('.agree');
					button.unbind('click');
					agree.unbind('click');
					$.ajax(
					{
						type: 'GET',
						data: 'type=disagree&friendFrom=' + u_name,
						url:'/friend_confirm/',
						success:function(html)
						{
							
							if(html != null && html != '')
							{
								alert(html);
							}

						}
					});
				});
			}
		});
	}
	
})