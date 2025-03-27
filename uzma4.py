import sqlite3

# Connect to SQLite Database (Creates a file 'library.db' if not exists)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Books Table
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    genre TEXT NOT NULL)''')
conn.commit()

# Function to Add a Book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter book genre: ")

    cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
    conn.commit()
    print(f"✅ '{title}' added successfully!")

# Function to View All Books
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("📖 No books found in the library!")
    else:
        print("\n📚 Your Library:")
        print("-" * 40)
        for book in books:
            print(f"ID: {book[0]} | {book[1]} by {book[2]} [{book[3]}]")
        print("-" * 40)

# Function to Search Books by Title
def search_books():
    search_title = input("Enter book title to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + search_title + '%',))
    books = cursor.fetchall()

    if not books:
        print("❌ No books found with that title!")
    else:
        print("\n🔍 Search Results:")
        print("-" * 40)
        for book in books:
            print(f"ID: {book[0]} | {book[1]} by {book[2]} [{book[3]}]")
        print("-" * 40)

# Function to Delete a Book
def delete_book():
    book_id = input("Enter book ID to delete: ")
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Book ID not found!")
    else:
        print("✅ Book deleted successfully!")

# Main Menu
def main():
    while True:
        print("\n📘 Personal Library Manager")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Delete a Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("📚 Exiting Library Manager. Goodbye!")
            conn.close()
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the Program
if __name__ == "__main__":
    main()


