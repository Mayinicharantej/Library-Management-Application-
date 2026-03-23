class Library:
    def __init__(self, list_of_books, library_name):
        self.available_books = list_of_books
        self.library_name = library_name
        self.lent_books = {} # Dictionary to track which book is lent to whom

    def display_available_books(self):
        print(f"\n--- Books Available in {self.library_name} ---")
        print(f"\n--- Books Available in {self.library_name} ---")
        if not self.available_books:
            print("No books are currently available.")
        else:
            for index, book in enumerate(self.available_books, start=1):
                print(f"{index}. {book}")

    def lend_book(self, requested_book, user_name):
        if requested_book in self.available_books:
            print(f"\nSuccess! '{requested_book}' has been lent to {user_name}.")
            self.available_books.remove(requested_book)
            self.lent_books[requested_book] = user_name
        elif requested_book in self.lent_books:
            print(f"\nSorry, '{requested_book}' is currently checked out by {self.lent_books[requested_book]}.")
        else:
            print(f"\nError: '{requested_book}' does not exist in our system.")

    def return_book(self, returned_book):
        if returned_book in self.lent_books:
            print(f"\nThank you for returning '{returned_book}'.")
            del self.lent_books[returned_book]
            self.available_books.append(returned_book)
        else:
            print("\nError: This book was not borrowed from us, or your input is incorrect.")

    def add_book(self, new_book):
        self.available_books.append(new_book)
        print(f"\nSuccess! '{new_book}' has been added to the library.")

# --- Main Program Loop ---
def main():
    # Initialize the library with some default books
    initial_books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "The Matrix Complete Guide"]
    my_library = Library(initial_books, "Central City Library")

    while True:
        print(f"\n=== Welcome to the {my_library.library_name} System ===")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Donate/Add a New Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_available_books()
            
        elif choice == '2':
            book = input("Enter the exact name of the book you want to borrow: ")
            user = input("Enter your name: ")
            my_library.lend_book(book, user)
            
        elif choice == '3':
            book = input("Enter the exact name of the book you are returning: ")
            my_library.return_book(book)
            
        elif choice == '4':
            book = input("Enter the name of the new book: ")
            my_library.add_book(book)
            
        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            break
            
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()