from contextlib import contextmanager


class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
        return self.items

    def __repr__(self):
        return f"MyList({self.items})"


@contextmanager
def manage_list(my_list):
    backup = my_list.items[:]
    try:
        yield my_list
    except Exception as e:
        my_list.items = backup
        raise e


my_list = MyList()
print("Boshlang'ich:", my_list)

try:
    with manage_list(my_list) as lst:
        lst.append(1)
        lst.append(2)
        print("With blok ichida:", lst)
        raise ValueError("Something went wrong!")
except ValueError:
    pass

print("With blokdan keyin (xatolik bilan):", my_list)

try:
    with manage_list(my_list) as lst:
        lst.append(3)
        print("With blok ichida:", lst)
        # Xatolik yuzaga kelmaydi
except ValueError:
    pass

print("With blokdan keyin (xatoliksiz):", my_list)
