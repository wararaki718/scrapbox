import dataclasses

@dataclasses.dataclass
class PaperBook:
    body: str = None


if __name__ == '__main__':
    book = PaperBook()
    print(book.body)
    book = PaperBook(body='hello')
    print(book.body)
    book.body = 'world'
    print(book.body)
