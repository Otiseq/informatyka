import math

def szescian():
    a = float(input("a= "))
    p = 6 * a ** 2
    return f"Pole= {p}"

def prostopadloscian():
    a = float(input("a= "))
    b = float(input("b= "))
    c = float(input("c= "))
    p = 2 * a * b + 2 * b * c + 2 * a * c
    return f"Pole= {p}"

def graniastoslup():
    a = float(input("a= "))
    b = float(input("b= "))
    h = float(input("h= "))
    pP = a * b
    pB = 2 * (a * h) + 2 * (b * h)
    p = 2 * pP + pB
    return f"Pole= {p}"

def walec():
    r = float(input("r= "))
    h = float(input("h= "))
    pP = math.pi * r ** 2
    p = 2 * pP + 2 * math.pi * r * h
    return f"Pole= {p}"

def stozek():
    r = float(input("r= "))
    h = float(input("h= "))
    pP = math.pi * r ** 2
    l = math.sqrt(r ** 2 + h ** 2)
    p = pP + math.pi * r * l
    return f"Pole= {p}"

def kula():
    r = float(input("r= "))
    p = 4 * math.pi * r ** 2
    return f"Pole= {p}"

def kolo():
    r = float(input("r= "))
    p = math.pi * r ** 2
    return f"Pole= {p}"

def romb():
    d1 = float(input("d1= "))
    d2 = float(input("d2= "))
    p = (d1 * d2) / 2
    a = math.sqrt((d1 / 2) ** 2 + (d2 / 2) ** 2)
    return f"Pole= {p}"

def wysokosc_trojkata():
    a = float(input("a= "))
    b = float(input("b= "))
    h = math.sqrt(a ** 2 - (b / 2) ** 2)
    return f"Wysokość= {h}"

def przekatna_kwadratu():
    a = float(input("a= "))
    d1 = a * math.sqrt(2)
    return f"Przekątna= {d1}"
