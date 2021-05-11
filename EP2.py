import math as m


def f(x):
    """Essa função retorna a função escolhida"""
    return m.exp(x) - m.cos(x) - x - 2


def fd(x):
    """Essa função retorna a derivada da função escolhida"""
    return m.exp(x) + m.sin(x) - 1


def Bisseccao(f, a, b, i=1, li=[], la=[], lb=[], lx=[], ls=[], e=10**-15, j=100):
    """Essa função calcula e armazena os valores pelo método de Bisseccao em varias listas e depois as retornam"""
    if i == 1:
        li = []
        la = []
        lb = []
        lx = []
        ls = []
    Fa = f(a)
    Fb = f(b)
    x = (a + b)/2
    Fx = f(x)
    s = abs((a-b)/2)
    li += [i]
    la += [a]
    lb += [b]
    lx += [x]
    ls += [s]
    if s < e or i > j:
        return li, la, lb, lx, ls
    else:
        if Fx > 0 and Fa > 0:
            a = x
            return Bisseccao(f, a, b, i+1, li, la, lb, lx, ls)
        elif Fx < 0 and Fb < 0:
            b = x
            return Bisseccao(f, a, b, i+1, li, la, lb, lx, ls)


def printBisseccao(li, la, lb, lx, ls, i=1):
    """Recebe as listas da Função Bisseccao e printa uma tabela com os valores de a, b, raiz e erro"""
    if i == 1:
        print("Método da Bissecção: a = {} e b = {}".format(la[0], lb[0]))
        print("---------------------------------------------------------------------------------------------------------------")
        print(" i                a                            b                       Raiz                         Erro")
        print("---------------------------------------------------------------------------------------------------------------")
        print(" {}         {:.15f}           {:.15f}         {:.15f}            {:.15f}".format(li[0], la[0], lb[0], lx[0], ls[0]))
        return printBisseccao(li[1:], la[1:], lb[1:], lx[1:], ls[1:], i + 1)
    else:
        if len(li) == 1:
            print("{}         {:.15f}           {:.15f}         {:.15f}            {:.15f}".format(li[0], la[0], lb[0], lx[0], ls[0]))
            print("")
            print("A raiz aproximada da Função f é {:.15f}.".format(lx[0]))
            print("--------------------------------------------------------------------------------------------------------------")
            return
        elif i < 10:
            print(" {}         {:.15f}           {:.15f}         {:.15f}            {:.15f}".format(li[0], la[0], lb[0], lx[0], ls[0]))
            return printBisseccao(li[1:], la[1:], lb[1:], lx[1:], ls[1:], i + 1)
        else:
            print("{}         {:.15f}           {:.15f}         {:.15f}            {:.15f}".format(li[0], la[0], lb[0], lx[0], ls[0]))
            return printBisseccao(li[1:], la[1:], lb[1:], lx[1:], ls[1:], i+1)


def Newton(f, fd, x, i=1, li=[], lx=[], lxi=[], ls=[], e=10**-15, j=100):
    """Essa função calcula e armazena os valores pelo método de Newton-Raphson em varias listas e depois as retornam"""
    if i == 1:
        li = []
        lx = []
        lxi = []
        ls = []
    xi = x - (f(x)/fd(x))
    s = abs((xi-x)/xi)
    li += [i]
    lx += [x]
    lxi += [xi]
    ls += [s]
    if s < e or i > j:
        return li, lx, lxi, ls
    else:
        x = xi
        return Newton(f, fd, x, i+1, li, lx, lxi, ls)


def printNewton(li, lx, lxi, ls, i=1):
    """Recebe as listas da Função Newton e printa uma tabela com os valores de x, raiz e erro"""
    if i == 1:
        print("Método de Newton-Raphson: x1 = ", lx[0])
        print("---------------------------------------------------------------------------------")
        print(" i                 x                         Raiz                     Erro")
        print("---------------------------------------------------------------------------------")
        print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
        return printNewton(li[1:], lx[1:], lxi[1:], ls[1:], i+1)
    else:
        if len(li) == 1 and li[0] < 10:
            print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            print("")
            print("A raiz aproximada da Função f é {:.15f}.".format(lxi[0]))
            print("---------------------------------------------------------------------------------")
        elif len(li) == 1:
            print("{}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            print("")
            print("A raiz aproximada da Função f é {:.15f}.".format(lxi[0]))
            print("---------------------------------------------------------------------------------")
        elif i < 10:
            print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            return printNewton(li[1:], lx[1:], lxi[1:], ls[1:], i + 1)
        else:
            print("{}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            return printNewton(li[1:], lx[1:], lxi[1:], ls[1:], i+1)


def Secante(f, x, y, i=1, li=[], lx=[], lxi=[], ls=[], ly=[], e=10**-15, j=100):
    """Essa função calcula e armazena os valores pelo método da Secante em varias listas e depois as retornam"""
    if i == 1:
        li = []
        lx = []
        lxi = []
        ls = []
        ly = []
    xi = x - ((f(x)*(x-y))/(f(x)-f(y)))
    s = abs((xi - x) / xi)
    li += [i]
    lx += [x]
    lxi += [xi]
    ls += [s]
    ly += [y]
    if s < e or i > j:
        return li, lx, lxi, ls, ly
    else:
        y = x
        x = xi
        return Secante(f, x, y, i+1, li, lx, lxi, ls, ly)


def printSecante(li, lx, lxi, ls, ly, i=1):
    """Recebe as listas da Função Secante e printa uma tabela com os valores de x, raiz e erro"""
    if i == 1:
        print("Método da Secante: x0 = {} e x1 = {}".format(ly[0], lx[0]))
        print("---------------------------------------------------------------------------------")
        print(" i                 x                         Raiz                     Erro")
        print("---------------------------------------------------------------------------------")
        print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
        return printSecante(li[1:], lx[1:], lxi[1:], ls[1:], ly, i+1)
    else:
        if len(li) == 1 and li[0] < 10:
            print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            print("")
            print("A raiz aproximada da Função f é {:.15f}.".format(lxi[0]))
            print("---------------------------------------------------------------------------------")
        elif len(li) == 1:
            print("{}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            print("")
            print("A raiz aproximada da Função f é {:.15f}.".format(lxi[0]))
            print("---------------------------------------------------------------------------------")
        elif i < 10:
            print(" {}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            return printSecante(li[1:], lx[1:], lxi[1:], ls[1:], ly, i + 1)
        else:
            print("{}         {:.15f}           {:.15f}        {:.15f}".format(li[0], lx[0], lxi[0], ls[0]))
            return printSecante(li[1:], lx[1:], lxi[1:], ls[1:], ly, i+1)


def teste1():
    """Faz o primeiro teste"""
    lib, lab, lbb, lxb, lsb = Bisseccao(f, 7, 1)
    printBisseccao(lib, lab, lbb, lxb, lsb)
    lin, lxn, lxin, lsn = Newton(f, fd, 7)
    printNewton(lin, lxn, lxin, lsn)
    lis, lxs, lxis, lss, lys = Secante(f, 7, 8)
    printSecante(lis, lxs, lxis, lss, lys)
    return lib, lxb, lin, lxin, lis, lxis


def teste2():
    """Faz o segundo teste"""
    lib2, lab2, lbb2, lxb2, lsb2 = Bisseccao(f, -3, 1)
    printBisseccao(lib2, lab2, lbb2, lxb2, lsb2)
    lin2, lxn2, lxin2, lsn2 = Newton(f, fd, -3)
    printNewton(lin2, lxn2, lxin2, lsn2)
    lis2, lxn2, lxis2, lsn2, lyn2 = Secante(f, -3, -10)
    printSecante(lis2, lxn2, lxis2, lsn2, lyn2)
    return lib2, lxb2, lin2, lxin2, lis2, lxis2


def Main():
    """Chama todas as outras funções"""
    print("Os seguintes métodos númericos para achar uma raiz usará a seguinte função:")
    print("f(x) = e^(x) - cos(x) - x - 2")
    print("Derivada da função f:")
    print("f'(x) = e^(x) + sen(x) - 1")
    print("-----------------------------------")
    lib, lxb, lin, lxin, lis, lxis = teste1()
    lib2, lxb2, lin2, lxin2, lis2, lxis2 = teste2()


Main()