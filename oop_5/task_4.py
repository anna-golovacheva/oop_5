class TeamIterator:
    def __init__(self, team):
        self.team = team
        self.counter_j = -1
        self.counter_s = -1

    def __next__(self):
        if self.counter_j == len(self.team._juniorMembers) - 1 and self.counter_s == len(self.team._seniorMembers) - 1:
            raise StopIteration
        elif self.counter_j < len(self.team._juniorMembers) - 1:
            self.counter_j += 1
            return self.team._juniorMembers[self.counter_j], 'junior'
        else:
            self.counter_s += 1
            return self.team._seniorMembers[self.counter_s], 'senior'


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
