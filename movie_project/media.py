import webbrowser

class Movie(object):
    """ Returns information regarding a particular movie """
    def __init__(self, movie_title, movie_storyline, poster_image,
                trailer_youtube):
                
        self.title  = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """ Plays a trailer of a movie """
        webbrowser.open_new_tab(self.youtube_trailer_url)
