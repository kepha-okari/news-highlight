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

    def __init__(self, author, title, description, urlToImage, url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt

    @classmethod
    def publish_date_format(cls,publishedAt):
        '''
        Function that changes the format of the date from UTC to display-friendly format

        Args:
            publishedAt : The date for the article, in UTC (+0).
        '''
        date_to_display = publishedAt[:10]

        return date_to_display
