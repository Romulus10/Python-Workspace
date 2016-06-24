# coding: utf-8

import Containers


def save(name, t):
    """
    Saves the current account to a file with the same name as the account.
    :param name: string
    :param t: list<Transaction>
    """
    f = open(name + '.txt', 'w')
    f.write(name + '\n')
    for x in t:
        f.write(x.name + ';' + str(x.category) + ';' + str(x.date) + ';' + str(x.value) + '\n')
    f.close()


def load(name):
    """
    Loads [name].txt to the program as an account.
    :rtype: dict
    :param name: string
    :return: {transactions, categories, category_amounts}
    """
    l = []
    m = []
    n = []
    f = open(name + '.txt', 'r')
    x = f.readlines()
    number = 0
    x.pop(0)
    for y in x:
        y = y.strip('\n')
        y = y.split(';')
        z = Containers.Transaction(number, y[0], y[1], y[2], y[3])
        if y[1] not in m:
            m.append(y[1])
            n.append(y[3])
        else:
            n[m.index(y[1])] += y[3]
        l.append(z)
        number += 1
    f.close()
    return {'transactions': l, 'categories': m, 'category_amounts': n}


def new(name):
    """
    Creates an empty account in the program, and an empty text file [name].txt.
    :rtype: list
    :param name: string
    :return: x
    """
    f = open(str(name) + '.txt', 'w')
    f.write(name)
    x = []
    f.close()
    return x


def copy(name1, name2):
    assert isinstance(name1, str)
    assert isinstance(name2, str)
    f1 = open(name1 + '.txt', 'r')
    f2 = open(name2 + '.txt', 'w')
    content = f1.readlines()
    for x in content:
        f2.write(x)
    f1.close()
    f2.close()
