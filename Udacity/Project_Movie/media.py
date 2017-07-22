import webbrowser as wb

class Movie():

    def __init__(self,movie_title,sline,image,trailer):

        self.title= movie_title
        self.storyline= sline
        self.poster_image_url= image
        self.trailer_youtube_url= trailer

    def show_trailer(self):
        wb.open(trailer_youtube_url)




