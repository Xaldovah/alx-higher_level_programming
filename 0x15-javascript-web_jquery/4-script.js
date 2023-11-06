$(document).ready(function () {
	$('#toggle_header').click(function() {
		const $headerElement = $('header');

		if ($headerElement.hasClass('red')) {
			$headerElement.removeClass('red').addClass('green');
		} else {
			$headerElement.removeClass('green').addClass('red');
		}
	});
});
