function turnLightOn(socket_num) {

	$.get("api/socketon", { "socket_num": socket_num })
		.done(function(data) {
			updateUI(JSON.parse(data));
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function turnLightOff(socket_num) {

	$.get("api/socketoff", { "socket_num": socket_num })
		.done(function(data) {
			updateUI(JSON.parse(data));
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function updateSocketStatus() {

	$.get("api/socketstatus")
		.done(function(data) {
			updateUI(JSON.parse(data));
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function init() {

	$("#errorText").hide();
	updateSocketStatus();
}

function updateUI(socket_states) {
	$("#errorText").hide();
	if (socket_states["1"]) {
		$("#TurnOnButton1").hide();
		$("#TurnOffButton1").show();
		$("#socket1Status").html("ON");
		$("#socket1Status").css("color", "green");
	}
	else if (!socket_states["1"]) {
		$("#TurnOnButton1").show();
		$("#TurnOffButton1").hide();
		$("#socket1Status").html("OFF");
		$("#socket1Status").css("color", "red");
	}

	if (socket_states["2"]) {
		$("#TurnOnButton2").hide();
		$("#TurnOffButton2").show();
		$("#socket2Status").html("ON");
		$("#socket2Status").css("color", "green");
	}
	else if (!socket_states["2"]){
		$("#TurnOnButton2").show();
		$("#TurnOffButton2").hide();
		$("#socket2Status").html("OFF");
		$("#socket2Status").css("color", "red");
	}
}

init();