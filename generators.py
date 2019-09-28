# -*- coding: utf-8 -*-
"""Language Tour: Generators"""

if __name__ == "__main__":
    # Ternary cmp
    val = 32
    val if val >= 0 else -val

    # List
    var_list = [i for i in range(20) if i % 3 > 0]
    # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    var_list = [(i, j) for i in range(2) for j in range(3)]
    # => [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

    # Set
    {n**2 for n in range(12)}

    # Dict
    {n: n**2 for n in range(6)}
    # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Generator
    G = (n**2 for n in range(12))
    list(G)  # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    list(G)  # => []

    def gen():
        """Generates x^2 from x=0 to x=11."""
        for idx in range(12):
            yield idx**2  # A la place de retourner une seule valeur,
            # on en retourne plusieurs

    print(*gen())

    # => 0 1 4 9 16 25 36 49 64 81 100 121

    # Exemple de fonction
    def gen_primes(max_range):
        """Generate primes up to max_range"""
        primes = set()
        for idx in range(2, max_range):
            if all(idx % p > 0 for p in primes):
                primes.add(idx)
                yield idx

    print(*gen_primes(100))

    # => 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
