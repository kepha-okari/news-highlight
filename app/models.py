class Sources:
    """ Sources class to define the news source objects """

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    """ Articles class to define the articles object """

    def __init__(self, author, title, description, urlToImage, url):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
