class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
        return self.items

    def __enter__(self):
        self._backup = self.items[:]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.items = self._backup
        return exc_type is None

    def __repr__(self):
        return f"MyList({self.items})"


my_list = MyList()
print("Boshlang'ich:", my_list)

with my_list as lst:
    lst.append(1)
    lst.append(2)
    print("With blok ichida:", lst)
    raise ValueError("Something went wrong!")

print("With blokdan keyin (xatolik bilan):", my_list)

with my_list as lst:
    lst.append(3)
    print("With blok ichida:", lst)

print("With blokdan keyin (xatoliksiz):", my_list)
