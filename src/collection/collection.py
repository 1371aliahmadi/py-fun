class Collection:
    """Collection helper functions."""

    def contains(self, s, e):
        """Count occurrences of e in s."""
        return s.count(e)

    def zip(self, s, p):
        """Pair consecutive elements from s and p."""
        return list(zip(s, p))

    def pset(self, s):
        """Return powerset of s."""
        from itertools import combinations
        result = []
        for r in range(len(s) + 1):
            result.extend([list(c) for c in combinations(s, r)])
        return result

    def perm(self, p):
        """Return permutations of p."""
        from itertools import permutations
        return [list(x) for x in permutations(p)]
