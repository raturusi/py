class MyStore:
    def __init__(self, address):
        self.address = address
        self.__received = {}
        self.__transfered = {}
        self.__r = 0
        self.__t = 0
        self.p = ''

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, p):
        if self.__getvalidate(p):
            self.__p = '0'
        else:
            self.__p = p

    def __getvalidate(self, p):
        if not p.isdigit():
            return True
        elif int(p) < 0:
            return True
        else:
            return False

    def __provodka(self, question, operation='+'):
        self.p = input(question)
        if operation == '+':
            self.__r = int(self.p)
        else:
            self.__t = int(self.p)

    def equipment_receiving(self, e):
        q = self.__received.get(e)
        self.__r = 0
        self.__provodka('Сколько ' + e.model + ' принять на склад: ')
        if q is not None:
            q += self.__r
            self.__received[e] = q
        else:
            self.__received.update({e: self.__r})

    def equipment_transfering(self, e):
        q = self.__received.get(e)
        if q is None or q <= 0:
            print(f'На складе {e.model} нет')
        else:
            self.__t = 0
            q_t = self.__transfered.get(e)
            self.__provodka('Сколько ' + e.model + ' передать со склада (максимум ' + str(q) + '): ', '-')
            self.__received[e] = q - self.__t
            if q_t is not None:
                q_t += self.__t
                self.__transfered[e] = q_t
            else:
                self.__transfered.update({e: self.__t})

    def __str__(self):
        store_eq = []
        not_store_eq = []
        for key, value in self.__received.items():
            store_eq.append(key.model + ' = ' + str(value))
        for key, value in self.__transfered.items():
            not_store_eq.append(key.model + ' = ' + str(value))
        return 'На складе ' + self.address + ':\n' + '\n'.join(store_eq) + '\nПередано:\n' + '\n'.join(not_store_eq)


class MyOfficeEquipment:
    def __init__(self, model):
        self.model = model


class Printer(MyOfficeEquipment):
    def __init__(self, duplex, model):
        self.duplex = duplex
        self.__type = 'printer'
        super().__init__(model)


class Xerox(MyOfficeEquipment):
    def __init__(self, color, model):
        self.color = color
        self.__type = 'xerox'
        super().__init__(model)


class Scanner(MyOfficeEquipment):
    def __init__(self, resolution, model):
        self.__resolution = resolution
        self.__type = 'scаnner'
        super().__init__(model)


p1 = Printer(True, 'Epson l355')
p2 = Printer(False, 'HP ColorJet500')
x1 = Xerox(True, 'LG 111')
x2 = Xerox(False, 'Xerox 100')
x2 = Xerox(False, 'Xerox 100')
s1 = Scanner(300, 'Canon E100')
s2 = Scanner(500, 'Epson C200')
store = MyStore('Н.Ногород, пр.Гагарина, 168')

store.equipment_receiving(p1)
store.equipment_receiving(p2)
store.equipment_receiving(x1)
store.equipment_receiving(x2)
store.equipment_receiving(s1)
store.equipment_receiving(s2)

store.equipment_transfering(p1)
store.equipment_transfering(p2)
store.equipment_transfering(x1)
store.equipment_transfering(x2)
store.equipment_transfering(s1)
store.equipment_transfering(s2)

print(store)
