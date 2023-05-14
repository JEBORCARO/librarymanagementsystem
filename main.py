class Library:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.members = []

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members.append(member)

    def edit_item(self, isbn, item_data):
        for item in self.items:
            if item.isbn == isbn:
                item.update(item_data)
                break

    def delete_item(self, isbn):
        for item in self.items:
            if item.isbn == isbn:
                self.items.remove(item)
                break

    def list_items(self):
        for item in self.items:
            print(item)

    def borrow_item(self, member_id, item_isbn):
        for item in self.items:
            if item.isbn == item_isbn:
                if item.availability == "available":
                    item.availability = "borrowed"
                    self.members[member_id].borrowed_items.append(item)
                    break
                else:
                    print("Item is borrowed")
                    break

    def return_item(self, member_id, item_isbn):
        for item in self.items:
            if item.isbn == item_isbn:
                if item.availability == "borrowed":
                    item.availability = "available"
                    self.members[member_id].borrowed_items.remove(item)
                    break
                else:
                    print("Item is not borrowed")
                    break

    def write_to_files(self):
        with open("items.txt", "w") as f:
            for item in self.items:
                f.write(
                    f"{item.title},{item.author},{item.publisher},{item.isbn},{item.category},{item.availability},{item.type}" + "\n")

        with open("members.txt", "w") as f:
            for member in self.members:
                f.write(f"{member.name},{member.member_id}" + "\n")

        with open("library.txt", "w") as f:
            f.write(self.name)

        borrowed_items = []
        for member in self.members:
            borrowed_items = borrowed_items + member.borrowed_items
            with open("borrowed.txt", "a") as f:
                for item in borrowed_items:
                    f.write(
                        f"{item.title},{item.author},{item.publisher},{item.isbn},{item.category},{item.availability},{item.type}" + "\n")

    def __str__(self) -> str:
        return self.name


class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    def __str__(self) -> str:
        return f"{self.name},{self.member_id}"


class Item:
    def __init__(self, title: str, author: str, publisher: str, isbn, category: str, availability: str, item_type: str) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category
        self.availability = availability
        self.isbn = isbn
        self.type = item_type

    def __str__(self) -> str:
        return f"{self.title}({self.isbn}) by {self.author}"


class Book(Item):
    def __init__(self, title: str, author: str, publisher: str, isbn, category: str, availability: str, item_type: str) -> None:
        super().__init__(title, author, publisher, isbn, category, availability, item_type)

    def __str__(self) -> str:
        return super().__str__()


class Article(Item):
    def __init__(self, title: str, author: str, publisher: str, isbn, category: str, availability: str, item_type: str) -> None:
        super().__init__(title, author, publisher, isbn, category, availability, item_type)

    def __str__(self) -> str:
        return super().__str__()


class DigitalMedia(Item):
    def __init__(self, title: str, author: str, publisher: str, isbn, category: str, availability: str, item_type: str) -> None:
        super().__init__(title, author, publisher, isbn, category, availability, item_type)

    def __str__(self) -> str:
        return super().__str__()


def main():
    library = Library("My Library")

    with open("items.txt", "r") as f:
        for line in f:
            title, author, publisher, isbn, category, availability, media_type = line.strip().split(",")
            if media_type == "article":
                library.add_item(
                    Article(title, author, publisher, isbn, category, availability, media_type))
            elif media_type == "book":
                library.add_item(
                    Book(title, author, publisher, isbn, category, availability, media_type))
            elif media_type == "media":
                library.add_item(
                    DigitalMedia(title, author, publisher, isbn, category, availability, media_type))

    with open("members.txt", "r") as f:
        for line in f:
            name, member_id = line.strip().split(",")
            library.add_member(
                Member(name, member_id))

    while True:
        print("What would you like to do?")
        print("1. Add an item")
        print("2. Edit an item")
        print("3. Delete an item")
        print("4. List all items")
        print("5. Borrow an item")
        print("6. Return an item")
        print("7. Quit")

        choice = input()
        if choice == "1":
            # title, author, publisher, isbn, category, availability, media_type
            item_title = input("Enter the item's title: ")
            item_author = input("Enter the item's author: ")
            item_publisher = input("Enter the item's publisher: ")
            item_isbn = input("Enter the item's ISBN: ")
            item_category = input("Enter the item's category: ")
            item_type = input("Enter the item's type (book/media/article):")
            item_availability = 'available'
            if item_type == "article":
                library.add_item(
                    Article(item_title, item_author, item_publisher, item_isbn, item_category, item_availability, item_type))
            elif item_type == "book":
                library.add_item(
                    Book(item_title, item_author, item_publisher, item_isbn, item_category, item_availability, item_type))
            elif item_type == "media":
                library.add_item(
                    DigitalMedia(item_title, item_author, item_publisher, item_isbn, item_category, item_availability, item_type))

        elif choice == "2":
            item_isbn = input("Enter the item ISBN: ")
            item_title = input("Enter the item's title: ")
            item_author = input("Enter the item's author: ")
            item_publisher = input("Enter the item's publisher: ")
            item_isbn = input("Enter the item's ISBN: ")
            item_category = input("Enter the item's category: ")
            library.edit_item(item_isbn, {
                              'title': item_title, 'author': item_author, 'publisher': item_publisher, 'isbn': item_isbn, 'category': item_category})
        elif choice == "3":
            item_isbn = input("Enter the item ISBN: ")
            library.delete_item(item_isbn)
        elif choice == "4":
            for item in library.items:
                print(item)
        elif choice == "5":
            member_id = input("Enter the member ID: ")
            item_isbn = input("Enter the item ISBN: ")
            library.borrow_item(int(member_id), item_isbn)
        elif choice == "6":
            member_id = input("Enter the member ID: ")
            item_isbn = input("Enter the item ISBN: ")
            library.return_item(int(member_id), item_isbn)
        elif choice == "7":
            break

        library.write_to_files()


if __name__ == "__main__":
    main()
