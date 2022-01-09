// Linus movement
$('#forward').on('mousedown', function(){
	$.get('/forward');
	});
$('#forward').on('mouseup', function(){
	$.get('/stop');
	});
$('#backward').on('mousedown', function(){
	$.get('/backward');
	});
$('#backward').on('mouseup', function(){
	$.get('/stop');
	});
$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});
$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});
	
// Torvalds movement
$('#north').on('mousedown', function(){
	$.get('/north');
	});
$('#north').on('mouseup', function(){
	$.get('/stoptwo');
	});
$('#south').on('mousedown', function(){
	$.get('/south');
	});
$('#south').on('mouseup', function(){
	$.get('/stoptwo');
	});
$('#west').on('mousedown', function(){
	$.get('/west');
	});
$('#west').on('mouseup', function(){
	$.get('/stoptwo');
	});
$('#east').on('mousedown', function(){
	$.get('/east');
	});
$('#east').on('mouseup', function(){
	$.get('/stoptwo');
	});
// Servo movement
$('#min').on('mousedown', function(){
	$.get('/servomin');
	});
$('#mid').on('mousedown', function(){
	$.get('/servomid');
	});
$('#max').on('mousedown', function(){
	$.get('/servomax');
	});
$('#min2').on('mousedown', function(){
	$.get('/servomin2');
	});
$('#mid2').on('mousedown', function(){
	$.get('/servomid2');
	});
$('#max2').on('mousedown', function(){
	$.get('/servomax2');
	});
// PWM Motors
$('#thirty').on('mousedown', function(){
	$.get('/thirty');
	});
$('#fifty').on('mousedown', function(){
	$.get('/fifty');
	});
$('#full').on('mousedown', function(){
	$.get('/full');
	});
// Eye blink
$('#linus').on('mousedown', function(){
	$.get('/linuson');
	});
$('#linus').on('mouseup', function(){
	$.get('/linusoff');
	});
$('#torvalds').on('mousedown', function(){
	$.get('/torvaldson');
	});
$('#torvalds').on('mouseup', function(){
	$.get('/torvaldsoff');
	});
