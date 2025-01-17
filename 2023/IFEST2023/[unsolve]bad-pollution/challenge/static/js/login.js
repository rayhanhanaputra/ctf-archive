(function($) {
	$.fn.catchEnter = function(sel) {
		return this.each(function() {
			$(this).on('keyup', sel, function(e) {
				if (e.keyCode == 13)
					$(this).trigger("enterkey");
			})
		});
	};
})(jQuery);


$(document).ready(function() {
	$("#login-btn").on('click', function() {
		auth('login')
	});
	$("#register-btn").on('click', function() {
		auth('register')
	});
	$("#email").catchEnter().on('enterkey', function() {
		auth('login')
	});
	$("#password").catchEnter().on('enterkey', function() {
		auth('login')
	});
});

function toggleInputs(state) {
	$("#email").prop("disabled", state);
	$("#password").prop("disabled", state);
	$("#login-btn").prop("disabled", state);
	$("#register-btn").prop("disabled", state);
}


async function auth(intent) {

	toggleInputs(true);
	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.hide();

	let email = $("#email").val();
	let pass = $("#password").val();
	if ($.trim(email) === '' || $.trim(pass) === '') {
		toggleInputs(false);
		card.text("Please input email and password first!");
		card.attr("class", "alert alert-danger");
		card.show();
		return;
	}

	const data = {
		email: email,
		password: pass
	};

	await fetch(`/api/${intent}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
			},
			body: new URLSearchParams(data)
		})
		.then((response) => response.json()
			.then((resp) => {
				if (response.status == 200) {
					card.text(resp.message);
					card.attr("class", "alert alert-success");
					card.show();
					if (intent == 'login'){
						window.location.href = '/home';
					}
					return;
				}
				card.text(resp.message);
				card.attr("class", "alert alert-danger");
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

	toggleInputs(false);
}