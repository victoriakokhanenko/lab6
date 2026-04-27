-------------------------------5.3.2------------------------------------------



from math import gcd


class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                self._n = int(parts[0])
                self._d = int(parts[1])
            else:
                self._n = int(n)
                self._d = 1
        elif isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            self._n = n
            self._d = d

        self.reduce()

    def reduce(self):
        if self._d == 0:
            raise ValueError()
        g = gcd(self._n, self._d)
        self._n = self._n // g
        self._d = self._d // g
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f'Rational("{self._n}/{self._d}")'

    def __call__(self):
        return self._n / self._d

    def ensure_rational(self, other):
        if isinstance(other, int):
            return Rational(other)
        return other

    def __add__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d + self._d * other._n, self._d * other._d)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d - self._d * other._n, self._d * other._d)

    def __rsub__(self, other):
        other = self.ensure_rational(other)
        return other - self

    def __mul__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self.ensure_rational(other)
        if other._n == 0:
            raise ZeroDivisionError()
        return Rational(self._n * other._d, self._d * other._n)

    def __rtruediv__(self, other):
        other = self.ensure_rational(other)
        return other / self


class RationalList:
    def __init__(self, items=None):
        self._list = []
        if items is not None:
            for item in items:
                self._list.append(Rational(item))

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = Rational(value)

    def __len__(self):
        return len(self._list)

    def __add__(self, other):
        new_list = RationalList(self._list)
        if isinstance(other, RationalList):
            for item in other._list:
                new_list._list.append(item)
        else:
            new_list._list.append(Rational(other))
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._list:
                self._list.append(item)
        else:
            self._list.append(Rational(other))
        return self

    def __iter__(self):
        return iter(self._list)


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]

    for filename in files:
        try:
            r_list = RationalList()

            with open(filename, "r") as file:
                for line in file:
                    elements = line.split()
                    for el in elements:
                        r_list += el

            total_sum = sum(r_list)

            print(filename)
            print("Кількість елементів:", len(r_list))
            print("Сума (раціональний дріб):", total_sum)
            print("Сума (десятковий дріб):", total_sum())
            print("-" * 40)

        except FileNotFoundError:
            print("Файл не знайдено:", filename)
            print("-" * 40)





-------------------------------6.3.1------------------------------------------


from math import gcd

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                self._n = int(parts[0])
                self._d = int(parts[1])
            else:
                self._n = int(n)
                self._d = 1
        elif isinstance(n, Rational):
            self._n = n._n
            self._d = n._d
        else:
            self._n = n
            self._d = d
        
        self.reduce()

    def reduce(self):
        if self._d == 0:
            raise ValueError()
        g = gcd(self._n, self._d)
        self._n = self._n // g
        self._d = self._d // g
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return f'Rational("{self._n}/{self._d}")'

    def __call__(self):
        return self._n / self._d

    def ensure_rational(self, other):
        if isinstance(other, int):
            return Rational(other)
        return other

    def __add__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d + self._d * other._n, self._d * other._d)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._d - self._d * other._n, self._d * other._d)

    def __rsub__(self, other):
        other = self.ensure_rational(other)
        return other - self

    def __mul__(self, other):
        other = self.ensure_rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self.ensure_rational(other)
        if other._n == 0:
            raise ZeroDivisionError()
        return Rational(self._n * other._d, self._d * other._n)

    def __rtruediv__(self, other):
        other = self.ensure_rational(other)
        return other / self


class RationalListIterator:
    def __init__(self, rational_list):
        self._sorted_list = sorted(
            rational_list._list, 
            key=lambda r: (r._d, r._n), 
            reverse=True
        )
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sorted_list):
            item = self._sorted_list[self._index]
            self._index += 1
            return item
        raise StopIteration


class RationalList:
    def __init__(self, items=None):
        self._list = []
        if items is not None:
            for item in items:
                self._list.append(Rational(item))

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = Rational(value)

    def __len__(self):
        return len(self._list)

    def __add__(self, other):
        new_list = RationalList(self._list)
        if isinstance(other, RationalList):
            for item in other._list:
                new_list._list.append(item)
        else:
            new_list._list.append(Rational(other))
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._list:
                self._list.append(item)
        else:
            self._list.append(Rational(other))
        return self

    def __iter__(self):
        return RationalListIterator(self)


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    
    for filename in files:
        try:
            r_list = RationalList()
            
            with open(filename, "r") as file:
                for line in file:
                    elements = line.split()
                    for el in elements:
                        r_list += el
                        
            print(filename)
            print("Послідовність за ітератором:")
            
            output = []
            for item in r_list:
                output.append(str(item))
                
            print(" ".join(output))
            print("-" * 40)
            
        except FileNotFoundError:
            print("Файл не знайдено:", filename)
            print("-" * 40)
