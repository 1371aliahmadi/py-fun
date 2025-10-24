from src.calculator.calculator import Calculator
from src.collection.collection import Collection

def main():
    c1 = Calculator()
    c2 = Calculator()
    col = Collection()

    print(f' 1: c1.add(1, 2)\t-> {c1.add(1, 2)}')
    print(f' 2: c2.add(8, 3)\t-> {c2.add(8, 3)}')
    print(f' 3: c1.add("1", "1")\t-> {c1.add("1", "1")}')

    print("\nMultilingual tests:")
    print(c1.add("one", "four"))       # 5
    print(c1.add("drei", 9))           # 12
    print(c1.add("семь", "восемь"))    # 15
    print(c1.add("三", "四"))          # 7
    print(c1.add("VI", "IV"))          # 10

    print("\nFactorization tests:")
    print(c2.factorize("три"))         # [3]
    print(c2.factorize("X"))           # [2, 5]
    print(c2.factorize("ocho"))        # [2, 2, 2]
    print(c2.factorize(3 + 5))         # [2, 2, 2]
    print(c2.factorize(27))            # [3, 3, 3]
    print(c2.factorize(1092))          # [2, 2, 3, 7, 13]
    print(len(c2.factorize(32768)))    # 15

    print("\nCollection tests:")
    print(col.contains([1,2,2,3],2))                # 2
    print(col.zip([1,2,3],["a","b","c"]))           # [(1,'a'),(2,'b'),(3,'c')]
    print(len(col.pset([1,2,3])))                   # 8 subsets
    print(len(col.perm([1,2,3])))                   # 6 permutations
