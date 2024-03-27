$(document).ready(function() {
	$("#submit-btn").on('click', addOpinion);
	$("#content-box").on('keydown', function() {
		$("#resp").text('')
	});

});


async function addOpinion() {
	$("#submit-btn").prop("disabled", true);
	let card = $("#resp");
	let content = $("#content-box").val();
	if ($.trim(content) === '') {
		$("#submit-btn").prop("disabled", false);
		card.text("Still Empty, we need your opinion :)");
		return;
	}
	const data = {
		content: content
	};
	await fetch('/api/addopinion', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})
		.then((response) => response.json())
		.then((resp) => {
			card.text(resp.message);
		})
		.catch((error) => {
			card.text(error);
		});
	$("#submit-btn").prop("disabled", false);
}