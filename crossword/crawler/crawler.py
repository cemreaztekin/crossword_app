from logger import*
import services
import json

class Crawler:
    def __init__(self):
        self.data = None
        self.crawler()
        self.to_file()

    def crawler(self):
        try:
            self.data= services.get_clues()
        except Exception as e:
            logger.info(e)

    def to_file(self):
        try:
            with open("../data.json", "w") as file:
                json.dump(self.data, file, indent=3)
        except Exception as e:
            logger.info(e)

