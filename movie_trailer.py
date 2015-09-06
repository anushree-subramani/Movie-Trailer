import fresh_tomatoes
import media

pursuit_of_happyness = media.Movie("The Pursuit of Happyness", "Chris Gardner's nearly one-year struggle being homeless", "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg", "https://www.youtube.com/watch?v=89Kq8SDyvfg")

whistle_blower = media.Movie("The WhistleBlower", "One woman's fight for all other women", "https://upload.wikimedia.org/wikipedia/en/2/28/The_Whistleblower_Poster.jpg", "https://www.youtube.com/watch?v=al3anBiHwmI")

frozen = media.Movie("Frozen", "Bond of Two Sisters", "http://img3.wikia.nocookie.net/__cb20131002122858/disney/images/5/58/Frozen-movie-poster.jpg", "https://www.youtube.com/watch?v=TbQm5doF_Uc")

fugitive = media.Movie("Fugitive", "Prove yourself even if it means standing up against the world", "https://upload.wikimedia.org/wikipedia/en/c/c7/The_Fugitive_movie.jpg", "https://www.youtube.com/watch?v=ETPVU0acnrE")

movies_list = [pursuit_of_happyness, whistle_blower, frozen, fugitive]

fresh_tomatoes.open_movies_page(movies_list)
