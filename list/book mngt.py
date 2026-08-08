books = ["Python", "Java", "C++"]

books.append("HTML")

search = input("Enter book to search: ")

if search in books:
    print("Book found")
else:
    print("Book not found")

remove = input("Enter book to remove: ")

if remove in books:
    books.remove(remove)

print("All books:", books)
print("Total books:", len(books))
