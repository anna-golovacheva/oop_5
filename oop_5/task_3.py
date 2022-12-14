class MyList(list):
    def __init__(self, some_list):
        super().__init__(some_list)
        print('Работает магический метод init')

    def __getitem__(self, item):
        super().__getitem__(item)
        print('Работает магический метод getitem')

    def __str__(self):
        print('Работает магический метод str')
        return super(MyList, self).__str__()


    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        print('Работает магический метод setitem')

    def __len__(self):
        print('Работает магический метод len')
        return super(MyList, self).__len__()


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))