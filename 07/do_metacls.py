#!usr/bin/env python3
#--*-- coding: utf-8 --*--

class ListMataclass(type):
    def __new__(cls, name, base, attrs):
        print('cls = ', cls)
        print('name = ', name)
        print('base = ', base)
        print('attrs = ', attrs)
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, base, attrs)

class MyList(list, metaclass=ListMataclass):
    pass

L = MyList()
L.add(1)
L.add(1)
print(L)


