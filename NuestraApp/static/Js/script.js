document.addEventListener('DOMContentLoaded', () => {
    console.log('Script cargado y DOM listo');

    const searchInput = document.getElementById('searchInput');
    const genreSelect = document.getElementById('genreSelect');
    const yearSelect = document.getElementById('yearSelect');
    const movies = document.querySelectorAll('.movie-poster');

    function filterMovies() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedGenre = genreSelect.value;
        const selectedYear = yearSelect.value;

        movies.forEach(movie => {
            const title = movie.dataset.title.toLowerCase();
            const genre = movie.dataset.genre;
            const year = movie.dataset.year;

            const matchesSearch = title.includes(searchTerm);
            const matchesGenre = selectedGenre === "" || genre === selectedGenre;
            const matchesYear = selectedYear === "" || year === selectedYear;

            if (matchesSearch && matchesGenre && matchesYear) {
                movie.style.display = "";
            } else {
                movie.style.display = "none";
            }
        });
    }

    searchInput.addEventListener('input', filterMovies);
    genreSelect.addEventListener('change', filterMovies);
    yearSelect.addEventListener('change', filterMovies);

    // Para filtrar en la carga inicial (opcional)
    filterMovies();
});