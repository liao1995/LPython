import media
import webbrowser
toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://player.youku.com/player.php/sid/XMTQxOTgwNDc0MA==/v.swf")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "http://player.youku.com/player.php/sid/XODMwMjI2NTQ4/v.swf")


print(avatar.storyline)
