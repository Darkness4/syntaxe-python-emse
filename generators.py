# -*- coding: utf-8 -*-
"""Language Tour: Generators"""

from typing import List, Tuple, Set, Generator, Dict, Iterable, Iterator

if __name__ == "__main__":
    # Ternary compare
    val: int = 32
    print(val if val >= 0 else -val)

    # List
    var_list: List[int] = [i for i in range(20) if i % 3 > 0]
    # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    var_list: List[Tuple[int]] = [(i, j) for i in range(2) for j in range(3)]
    # => [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    # Set
    var_set: Set[int] = {n**2 for n in range(12)}

    # Dict
    var_set: Dict[int, int] = {n: n**2 for n in range(6)}
    # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Generator/Iterable/Iterator
    G: Generator[int, None, None] = (n**2 for n in range(12))
    G: Iterable[int] = (n**2 for n in range(12))  # Implique
    G: Iterator[int] = (n**2 for n in range(12))  # Equivalent
    list(G)  # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    list(G)  # => []  # Car, itérable qu'une seule fois !

    # NOTE: Le type hint indique ici : [YieldType, SendType, ReturnType]
    # Le choix dépend de l'usage de la fonction.

    def gen() -> Iterable[int]:
        """Generates x^2 from x=0 to x=11."""
        for idx in range(12):
            yield idx**2  # A la place de retourner une seule valeur,
            # on en retourne plusieurs

    print(*gen())

    # => 0 1 4 9 16 25 36 49 64 81 100 121

    # Exemple de fonction
    def gen_primes(max_range: int) -> Iterable[int]:
        """Generate primes up to max_range"""
        primes = set()
        for idx in range(2, max_range):
            if all(idx % p > 0 for p in primes):
                primes.add(idx)
                yield idx

    print(*gen_primes(100))

    # => 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

    for prime in gen_primes(100):
        print(prime)
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97
