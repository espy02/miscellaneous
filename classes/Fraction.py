class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        if denominator == 0:
            raise ZeroDivisionError
        if type(numerator) is float or type(denominator) is float:
            raise Exception("Error: numerator and denominator must be integers")

        gcd = self.GCD(numerator, denominator)
        self.n = numerator // gcd
        self.d = denominator // gcd

    def getNumerator(self):
        return self.n

    def getDenominator(self):
        return self.d

    def setNumerator(self, numerator: int):
        self.n = numerator

    def setDenominator(self, denominator: int):
        self.d = denominator

    # Greatest common divisor
    def GCD(self, d1: int, d2: int):
        greatest_denominator = max(abs(d1), abs(d2))
        smallest_denominator = min(abs(d1), abs(d2))
        if smallest_denominator == 0:
            return greatest_denominator
        else:
            return self.GCD(smallest_denominator, greatest_denominator % smallest_denominator)

    @staticmethod
    def floatToFraction(fl):
        string_fl = str(fl)
        new_n = ""
        point_index = 0
        for i in range(len(string_fl)):
            if string_fl[i] != ".":
                new_n += string_fl[i]
            if string_fl[i] == ".":
                point_index = i
        new_d = "1"
        for _ in range(len(new_n) - point_index):
            new_d += "0"
        return Fraction(int(new_n), int(new_d))

    def __add__(self, other):
        if type(other) is int:
            other = Fraction(other, 1)
        if type(other) is float:
            other = Fraction.floatToFraction(other)
        new_n = (self.getNumerator() * other.getDenominator()) + (other.getNumerator() * self.getDenominator())
        new_d = self.getDenominator() * other.getDenominator()
        gcd = self.GCD(new_n, new_d)
        new_n //= gcd
        new_d //= gcd
        return Fraction(new_n, new_d)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if type(other) is int:
            other = Fraction(other, 1)
        if type(other) is float:
            other = Fraction.floatToFraction(other)
        new_n = self.getNumerator() * other.getNumerator()
        new_d = self.getDenominator() * other.getDenominator()
        gcd = self.GCD(new_n, new_d)
        new_n //= gcd
        new_d //= gcd
        return Fraction(new_n, new_d)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) is int:
            other = Fraction(other, 1)
        if type(other) is float:
            other = Fraction.floatToFraction(other)
        new_n = self.getNumerator() * other.getDenominator()
        new_d = self.getDenominator() * other.getNumerator()
        gcd = self.GCD(new_n, new_d)
        new_n //= gcd
        new_d //= gcd
        return Fraction(new_n, new_d)

    def __pow__(self, power):
        new_n = self.n ** power
        new_d = self.d ** power
        return Fraction(new_n, new_d)

    def __rpow__(self, other):
        return other**(self.n/self.d)

    def __abs__(self):
        new_n = abs(self.n)
        new_d = abs(self.d)
        return Fraction(new_n, new_d)

    def __eq__(self, other):
        if type(other) is int:
            return float(self) == float(other)
        return self.getNumerator() == other.getNumerator() and self.getDenominator() == other.getDenominator()

    def __ne__(self, other):
        return not (self == other)

    def __int__(self):
        return self.n // self.d

    def __float__(self):
        return self.n / self.d

    def __bool__(self):
        if self.n == 0:
            return False
        return True

    def __str__(self):
        if self.n % self.d == 0:
            return str(int(self))
        return str(self.getNumerator()) + "/" + str(self.getDenominator())
