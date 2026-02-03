import json

def add():
    write = {
        "python": {"total": 10, "available": 7},
        "java": {"total": 9, "available": 8}
    }
    with open("file.json", "w", encoding="utf-8") as file:
        json.dump(write, file, indent=4)

def get_info():
    with open("file.json", "r", encoding="utf-8") as file:
        library = json.load(file)
        print(library)
        for book, info in library.items():
              print(f"Book: {book}")
              print(f"Total: {info['total']}")
              print(f"Available: {info['available']}")
              print("-" * 20)


# add()
get_info()
