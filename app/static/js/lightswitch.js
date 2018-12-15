function turnLightOn() {

	$.get("api/lighton")
		.done(function(data) {
			updateUI(true);
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function turnLightOff() {

	$.get("api/lightoff")
		.done(function(data) {
			updateUI(false);
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function getLightStatus() {

	$.get("api/lightstatus")
		.done(function(data) {
			updateUI(data === "1");
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function init() {

	$("#errorText").hide();
	updateUI(getLightStatus());
}

function updateUI(state) {
	$("#errorText").hide();
	if (state) {
		$("#TurnOnButton").hide();
		$("#TurnOffButton").show();
		$("#lightStatus").html("ON");
		$("#lightStatus").css("color", "green");
	}
	else {
		$("#TurnOnButton").show();
		$("#TurnOffButton").hide();
		$("#lightStatus").html("OFF");
		$("#lightStatus").css("color", "red");
	}
}

init();