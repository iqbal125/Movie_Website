#Creates movies objects with title, storyline, image, and trailer
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Create a Movie class instance """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

""" List of Movies """
#Toy Story 2
#Zootopia
#Monsters Inc
#Fight Club
#The Dark Knight
#The Mask
