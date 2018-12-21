function turnSocketOn(socket_num) {
	$.get("api/socketon", { "socket_num": socket_num })
		.done(function(data) {
			updateUI(JSON.parse(data));
		})
		.fail(function(data) {
			$("#errorText").show();
		});
}

function turnSocketOff(socket_num) {
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

function setTimer(socket_num) {
	let startTime = $(`#socket${socket_num}StartTime`).val();
	let endTime = $(`#socket${socket_num}EndTime`).val();

	$.get("api/settimer", { "socket_num": socket_num, "start_time": startTime, "end_time": endTime })
		.done(function(data) {
			$(`#timer${socket_num}ClearText`).hide();
			$(`#timer${socket_num}ErrorText`).hide();
			$(`#timer${socket_num}SuccessText`).show();
		})
		.fail(function(data) {
			$(`#timer${socket_num}ClearText`).hide();
			$(`#timer${socket_num}SuccessText`).hide();
			$(`#timer${socket_num}ErrorText`).show();
		});
}

function clearTimer(socket_num) {
	$(`#socket${socket_num}StartTime`).val('');
	$(`#socket${socket_num}EndTime`).val('');

	$.get("api/cleartimer", { "socket_num": socket_num })
		.done(function(data) {
			$(`#timer${socket_num}ErrorText`).hide();
			$(`#timer${socket_num}SuccessText`).hide();
			$(`#timer${socket_num}ClearText`).show();
		})
		.fail(function(data) {
			$(`#timer${socket_num}ClearText`).hide();
			$(`#timer${socket_num}SuccessText`).hide();
			$(`#timer${socket_num}ErrorText`).show();
		});
}

function init() {
	$("#errorText").hide();
	$("#timer1SuccessText").hide();
	$("#timer1ErrorText").hide();
	$("#timer1ClearText").hide();
	$("#timer2SuccessText").hide();
	$("#timer2ErrorText").hide();
	$("#timer2ClearText").hide();

	$('#socket1StartPicker').datetimepicker({
        format: 'LT'
    });
    $('#socket1EndPicker').datetimepicker({
        format: 'LT'
    });
    $('#socket2StartPicker').datetimepicker({
        format: 'LT'
    });
    $('#socket2EndPicker').datetimepicker({
        format: 'LT'
    });

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