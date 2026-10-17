import json
import os


class BookManager:
    def __init__(self, file_path="books.json"):
        self.file_path = file_path
        self.books = self._load_all()

    def _load_all(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_all(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def all(self):
        return self.books

    def get(self, index):
        if 0 <= index < len(self.books):
            return self.books[index]
        return None

    def create(self, data):
        data.pop('csrf_token', None)
        self.books.append(data)

    def update(self, index, data):
        if 0 <= index < len(self.books):
            data.pop('csrf_token', None)
            self.books[index] = data


books = BookManager()