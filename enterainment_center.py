import media
import webbrowser
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://player.youku.com/player.php/sid/XMTQxOTgwNDc0MA==/v.swf")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "http://player.youku.com/player.php/sid/XODMwMjI2NTQ4/v.swf")

inception = media.Movie("Inception",
			"A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO",
			"https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg",
			"http://www.imdb.com/video/imdb/vi4219471385/imdb/embed?autoplay=true")

movies = [toy_story, avatar, inception]
fresh_tomatoes.open_movies_page(movies)
