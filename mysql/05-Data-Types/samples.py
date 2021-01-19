from collections import namedtuple
from fractions import Fraction
from decimal import Decimal as D, localcontext

with localcontext() as ctx:
    ctx.prec = 6
    pie1 = D("3.14159265358979323846264338327950") / D("2.7182818284590452353")

with localcontext() as ctx:
    ctx.prec = 25
    pie2 = D("3.14159265358979323846264338327950") / D("2.7182818284590452353")
    
    
Numbers1 = namedtuple("Numbers1", "a b c d e")
data1 = [
    Numbers1(1.23, D(pie1), 1_000_000_000_000, 2, Fraction(22, 7)),
    Numbers1(4.56, D(pie2), -22, 5, Fraction(1, 3)),
    Numbers1(7.89, D("1.0"), 56, 9, Fraction(10, 2))
]

Numbers2 = namedtuple("Numbers2", "a b c d e")
data2 = [
    Numbers1(1.23, D(pie1), 1_000_000_000_000, 2, Fraction(22, 7)),
    Numbers2(4.56, D(pie2), -22, 5, Fraction(1, 3)),
    Numbers1(7.89, D("1.0"), 56, 9, Fraction(10, 2))
]

Numbers3 = namedtuple("Numbers3", "a b c d e")
data3 = [
    Numbers3("$1.23", D(pie1), 1_000_000_000_000, 2, Fraction(22, 7)),
    Numbers3("$4.56", D(pie2), -22, 5, Fraction(1, 3)),
    Numbers3("$7.89", D("1.0"), 56, 9, Fraction(10, 2))
]

data4 = [
    ("$1.23", D(pie1), 1_000_000_000_000, 2, Fraction(22, 7)),
    Numbers1("$4.56", D(pie2), -22, 5, Fraction(1, 3)),
    Numbers1("$7.89", D("1.0"), 56, 9, Fraction(10, 2))
]

data5 = [
    Numbers1("$4.56", D(pie2), -22, 5, Fraction(1, 3))
]

data6 = [
    Numbers1(1.23, D(pie1), 100_000_000_000_000_000_000, 2, Fraction(22, 7)),
    Numbers1(4.56, D(pie2), -22, 5, Fraction(1, 3)),
    Numbers1(7.89, D("1.0"), 56, 9, Fraction(10, 2))
]
