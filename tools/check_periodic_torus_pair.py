#!/usr/bin/env python3
"""Finite control for Stone-indexed torus-along-circle gluing.

Construct the 3x3 periodic triangulation of the torus, its induced horizontal
essential circle, and check simplicial homology and a nonzero mod-2 cup
product. Pure Python 3; no external packages.
This verifies finite combinatorial controls, not the sheaf/localic theorem.
"""

from itertools import combinations


def gf2_rank(columns):
    basis = {}
    for value in columns:
        v = value
        while v:
            pivot = v.bit_length() - 1
            if pivot in basis:
                v ^= basis[pivot]
            else:
                basis[pivot] = v
                break
    return len(basis)


def torus(n=3):
    vertices = sorted((i, j) for i in range(n) for j in range(n))
    triangles = set()
    for i, j in vertices:
        a = (i, j)
        b = ((i + 1) % n, j)
        c = ((i + 1) % n, (j + 1) % n)
        d = (i, (j + 1) % n)
        triangles.add(tuple(sorted((a, b, c))))
        triangles.add(tuple(sorted((a, d, c))))
    triangles = sorted(triangles)
    edges = sorted({tuple(sorted(pair)) for t in triangles
                    for pair in combinations(t, 2)})
    return vertices, edges, triangles


def main():
    n = 3
    vertices, edges, triangles = torus(n)
    vix = {v: i for i, v in enumerate(vertices)}
    eix = {e: i for i, e in enumerate(edges)}
    d1 = [(1 << vix[a]) ^ (1 << vix[b]) for a, b in edges]
    d2 = [sum(1 << eix[e] for e in combinations(t, 2))
          for t in triangles]
    r1, r2 = gf2_rank(d1), gf2_rank(d2)
    betti = (len(vertices) - r1,
             len(edges) - r1 - r2,
             len(triangles) - r2)

    row = {(i, 0) for i in range(n)}
    row_edges = [e for e in edges if set(e).issubset(row)]
    row_triangles = [t for t in triangles if set(t).issubset(row)]
    assert len(row) == 3 and len(row_edges) == 3 and not row_triangles

    # The coordinate seam cochains, evaluated on each oriented edge mod 2.
    def alpha(edge):
        return int({edge[0][0], edge[1][0]} == {0, n - 1})

    def beta(edge):
        return int({edge[0][1], edge[1][1]} == {0, n - 1})

    assert all(sum(alpha(e) for e in combinations(t, 2)) % 2 == 0
               for t in triangles)
    assert all(sum(beta(e) for e in combinations(t, 2)) % 2 == 0
               for t in triangles)

    contributions = [t for t in triangles
                     if alpha((t[0], t[1])) * beta((t[1], t[2]))]
    cup_eval = len(contributions) % 2
    assert (len(vertices), len(edges), len(triangles)) == (9, 27, 18)
    assert (r1, r2) == (8, 17)
    assert betti == (1, 2, 1)
    assert cup_eval == 1
    print("Torus f-vector:", (len(vertices), len(edges), len(triangles)))
    print("Boundary ranks mod 2:", (r1, r2), "Betti numbers:", betti)
    print("Full horizontal subcomplex (vertices, edges, faces):",
          (len(row), len(row_edges), len(row_triangles)))
    print("Mod-2 fundamental-class pairing <alpha cup beta, [T]>:",
          cup_eval)
    print("Contributing triangles (lexicographic Alexander-Whitney):",
          contributions)


    # Finite Stone parameter S={0,1}: check the common-upper-bound tuple
    # gluing formula for every ordered pair in the 102-point quotient poset.
    faces = ([frozenset((v,)) for v in vertices]
             + [frozenset(e) for e in edges]
             + [frozenset(t) for t in triangles])
    shared = [f for f in faces if f.issubset(row)]
    outside = [f for f in faces if f not in shared]
    nodes = ([("A", f) for f in shared]
             + [(i, f) for i in (0, 1) for f in outside])
    assert len(shared) == 6 and len(faces) == 54 and len(nodes) == 102

    def leq(a, b):
        tag_a, face_a = a
        tag_b, face_b = b
        if tag_a == "A":
            return face_a.issubset(face_b)
        return tag_b != "A" and tag_a == tag_b and face_a.issubset(face_b)

    for a in nodes:
        for b in nodes:
            actual = any(leq(a, witness) and leq(b, witness)
                         for witness in nodes)
            outer_tags = {x[0] for x in (a, b) if x[0] != "A"}
            predicted = (
                len(outer_tags) <= 1
                and any(a[1].issubset(face) and b[1].issubset(face)
                        for face in faces)
            )
            assert actual == predicted, (a, b, actual, predicted)
    print("Upper-hull finite-pair gluing: all 10,404 ordered pairs pass.")


if __name__ == "__main__":
    main()
