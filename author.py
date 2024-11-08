import json

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_details(self):
        return {
            "name": self.__name,
            "biography": self.__biography
        }

    def save_to_file(self):
        author_data = self.get_details()
        with open("authors.txt", "a") as file:
            file.write(json.dumps(author_data) + "\n")

    @staticmethod
    def load_from_file():
        authors = []
        try:
            with open("authors.txt", "r") as file:
                for line in file:
                    author_data = json.loads(line.strip())
                    author = Author(name=author_data["name"], biography=author_data["biography"])
                    authors.append(author)
        except FileNotFoundError:
            print("No authors file found.")
        return authors
