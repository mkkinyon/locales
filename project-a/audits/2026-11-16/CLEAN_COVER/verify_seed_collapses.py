#!/usr/bin/env python3
"""Optional independent finite-base verifier for BLIND_MATHEMATICAL_PACKET.md.

Only the nine-vertex seed and its listed elementary collapses are checked.
No part of the induction or the spectral-sequence theorem is assumed or proved.
Run using Python 3 and no third-party packages.
"""

from itertools import combinations


VERTICES = "abcdefhix"
N = len(VERTICES)
COVERS = (
    "ad", "ax", "bc", "bd", "xc", "xe", "cf", "de", "df",
    "eh", "ei", "fh", "fi",
)
MARKS = ("ad", "df", "fi")


def relation():
    less = {(a, b) for a, b in COVERS}
    for k in VERTICES:
        for i in VERTICES:
            for j in VERTICES:
                if (i, k) in less and (k, j) in less:
                    less.add((i, j))
    return less


LESS = relation()


def is_chain(simplex):
    return all((a, b) in LESS or (b, a) in LESS for a, b in combinations(simplex, 2))


ALL = {
    frozenset(items)
    for k in range(1, N + 1)
    for items in combinations(VERTICES, k)
    if is_chain(items)
}


def weight(simplex):
    return sum(set(edge) <= simplex for edge in MARKS)


def stage(p, omit_a=False):
    return {
        simplex for simplex in ALL
        if weight(simplex) <= p and (not omit_a or "a" not in simplex)
    }


def simplex(label):
    result = frozenset(label)
    assert len(result) == len(label), label
    assert result in ALL, f"Not a chain simplex: {label}"
    return result


def elementary_collapse(current, higher_label, facet_label):
    higher, facet = simplex(higher_label), simplex(facet_label)
    assert higher in current and facet in current, (higher_label, facet_label)
    assert facet < higher and len(higher) == len(facet) + 1
    strict_cofaces = [t for t in current if facet < t]
    assert strict_cofaces == [higher], (
        f"Not free: {facet_label} has cofaces "
        + str(["".join(sorted(t)) for t in strict_cofaces])
    )
    current.remove(higher)
    current.remove(facet)


def verify_collapse(source, target, pairs, description):
    current = set(source)
    for higher, facet in pairs:
        elementary_collapse(current, higher, facet)
    assert current == target, (
        description,
        ["".join(sorted(t)) for t in current - target],
        ["".join(sorted(t)) for t in target - current],
    )
    print(f"PASS {description}: {len(pairs)} elementary collapse pairs")


A_2_TO_1 = [("adfh", "adf"), ("bdfi", "dfi")]
A_1_TO_0 = [
    ("acfix", "acfi"), ("adeh", "adh"), ("adei", "ade"),
    ("adi", "ad"), ("afix", "afi"), ("bdfh", "dfh"),
    ("bcfi", "bfi"), ("cfix", "cfi"), ("bdf", "df"), ("fix", "fi"),
]
B_2_TO_1 = [("bdfi", "dfi")]
B_1_TO_0 = [
    ("bdfh", "dfh"), ("bcfi", "bfi"), ("cfix", "cfi"),
    ("bdf", "df"), ("fix", "fi"),
]
B_0_TO_OCT = [
    ("bdeh", "deh"), ("bcfh", "bfh"), ("bdei", "dei"),
    ("cfhx", "fhx"), ("bde", "de"), ("bcf", "bf"),
    ("bdh", "dh"), ("cfh", "fh"), ("bdi", "di"),
    ("cfx", "fx"), ("bd", "d"), ("cf", "f"),
]


def main():
    for edge in MARKS:
        a, b = edge
        assert (a, b) in LESS
        assert not any(
            (a, c) in LESS and (c, b) in LESS for c in VERTICES
        ), f"Not a cover: {edge}"
    print("PASS all three marked relations are covers")

    a0, a1, a2 = (stage(p) for p in range(3))
    b0, b1, b2 = (stage(p, omit_a=True) for p in range(3))
    assert tuple(map(len, (a0, a1, a2))) == (76, 96, 100)
    assert tuple(map(len, (b0, b1, b2))) == (50, 60, 62)
    print("PASS filtration cardinalities")

    verify_collapse(a2, a1, A_2_TO_1, "A_3,2 -> A_3,1")
    verify_collapse(a1, a0, A_1_TO_0, "A_3,1 -> A_3,0")
    verify_collapse(b2, b1, B_2_TO_1, "B_3,2 -> B_3,1")
    verify_collapse(b1, b0, B_1_TO_0, "B_3,1 -> B_3,0")

    f_vector = tuple(sum(len(t) == size for t in b0) for size in range(1, 5))
    assert f_vector == (8, 20, 18, 4), f_vector
    oct_facets = ("bch", "beh", "bci", "bei", "chx", "ehx", "cix", "eix")
    octahedron = {
        frozenset(face)
        for facet in oct_facets
        for size in range(1, len(facet) + 1)
        for face in combinations(facet, size)
    }
    verify_collapse(b0, octahedron, B_0_TO_OCT, "B_3,0 -> octahedron")
    assert tuple(sum(len(t) == size for t in octahedron) for size in range(1, 4)) == (6, 12, 8)
    print("PASS final octahedral boundary and f-vector")


if __name__ == "__main__":
    main()
