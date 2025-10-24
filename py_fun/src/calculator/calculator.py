class Calculator:
    """Multilingual, safe calculator with Roman numerals, singleton and factorization."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # word digits
    WORDS = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,
        "six":6,"seven":7,"eight":8,"nine":9,
        "null":0,"eins":1,"zwei":2,"drei":3,"vier":4,"fuenf":5,"fünf":5,
        "sechs":6,"sieben":7,"acht":8,"neun":9,
        "cero":0,"uno":1,"dos":2,"tres":3,"cuatro":4,
        "cinco":5,"seis":6,"siete":7,"ocho":8,"nueve":9,
        "ноль":0,"один":1,"два":2,"три":3,"четыре":4,
        "пять":5,"шесть":6,"семь":7,"восемь":8,"девять":9,
        "零":0,"一":1,"二":2,"两":2,"三":3,"四":4,
        "五":5,"六":6,"七":7,"八":8,"九":9,
    }

    ROMAN = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    def _roman_to_int(self, s: str) -> int:
        s = s.upper()
        total, prev = 0, 0
        for ch in reversed(s):
            val = self.ROMAN[ch]
            total += -val if val < prev else val
            prev = val
        return total

    def _to_number(self, x):
        if isinstance(x, (int, float)):
            return float(x)

        t = str(x).strip()
        low = t.lower()
        up  = t.upper()

        if low in self.WORDS:
            return float(self.WORDS[low])

        if len(up) > 0 and all(ch in self.ROMAN for ch in up):
            return float(self._roman_to_int(up))

        try:
            return float(t)
        except ValueError:
            raise ValueError(f"Cannot convert {x!r} to number")

    def add(self, a, b): return self._to_number(a) + self._to_number(b)
    def sub(self, a, b): return self._to_number(a) - self._to_number(b)
    def mul(self, a, b): return self._to_number(a) * self._to_number(b)
    def div(self, a, b):
        b_val = self._to_number(b)
        if b_val == 0:
            raise ZeroDivisionError("Division by zero")
        return self._to_number(a) / b_val

    def factorize(self, n):
        x = self._to_number(n)
        if x != int(x):
            raise ValueError("Factorize only works with integers")
        x = int(abs(x))
        if x <= 1:
            return [x]

        factors = []
        while x % 2 == 0:
            factors.append(2)
            x //= 2

        f = 3
        while f * f <= x:
            while x % f == 0:
                factors.append(f)
                x //= f
            f += 2

        if x > 1:
            factors.append(x)

        return factors
