import json
import csv

catalog = [
    {
        "id": 1,
        "title": "Python Pro",
        "author": "John Zelle",
        "genre": "Technical",
        "price": 650,
        "copies": 15
    },
    {
        "id": 2,
        "title": "Cosmos",
        "author": "Cari Segan",
        "genre": "Science",
        "price": 480,
        "copies": 20
    }
]

next_id = 1

def add_book_entry(catalog, next_id):

    while True:
        title = input("Enter Book title: ")

        if title == "":
            print("Book title cannot be empty, try again")
        else:
            break

    while True:
        author = input("Enter Book author: ")
        
        if author == "":
            print("Book author cannot be empty, try again")
        else:
            break

    while True:
            genre = input("Enter Book genre: ")
            
            if genre == "":
                print("Book genre cannot be empty, try again")
            else:
                break

    while True:
            try:
                price = float(input("Enter Book price: "))

                if price <= 0:
                    print("Book price should be more than 0, try again")
                else:
                    break

            except ValueError:
                print("Please enter the valid price")

    while True:
                try:
                    copies = int(input("Enter Book author: "))
    
                    if copies < 0:
                        print("Book copies cannot be negatice, try again")
                    else:
                        break
    
                except ValueError:
                    print("Please enter the valid input")

     


    book = {
        "id": next_id,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }

    catalog.append(book)

    print("Book Added Succesfully")

    return next_id + 1  



        


    ...

def render_catalog(catalog):

    if not catalog:
        print("No books available.")
        return

    ...

def query_books(catalog: list[dict], search_term: str) -> list[dict]:
    ...

def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    ...

def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    ...

def load_catalog_from_file(filepath: str) -> list[dict]:
    ...




def main():

    while True:

        print("'='* 50, MAIN MENU, '='* 50 ")
        print("1.Add Book")
        print("2.View Catalog")
        print("3.Search Books")
        print("4.Update Details")
        print("5.Delete Book")
        print("6.Save to File")
        print("7.Load from File")
        print("Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            print("Add Book : ")
            ...
        elif choice == "2":
            print("View Catalog : ")
            ...
        elif choice == "3":
            print("Search Books : ")
            ...
        elif choice == "4":
            print("Update Details : ")
            ...
        elif choice == "5":
            print("Delete Book : ")
            ...
        elif choice == "6":
            print("Save to File : ")
            ...
        elif choice == "7":
            print("Load from File : ")
            ...
        else:
            print("Exit")




if __name__ = "__main__": 
    main()