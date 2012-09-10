$(document).ready(function(){
	$("#quick_say").focus(function()
	{
		$(this).css("min-height", "80px");
	});

	$('#public_say').click(function()
	{
		$('#quick_say').css("max-height", "40px");
	});
})