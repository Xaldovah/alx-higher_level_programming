$(document).ready(function() {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
		const movies = data.results;

		const listMovies = $('#list_movies');

		$.each(movies, function(index, movie) {
			listMovies.append('<li>' + movie.title + '</li>');
		});
	});
});
