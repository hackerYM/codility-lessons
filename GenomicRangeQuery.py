## Range Minimum Query using Sparse Table (N * logN)
## https://brilliant.org/wiki/sparse-table/

# from math import floor, log
#
#
# class DnaSparseTable:
#
#     def __init__(self, text):
#
#         self.table = self._build_sparse_table(text)
#         # print(self.table)
#
#     def _build_sparse_table(self, text):
#
#         N, M = len(text), floor(log(len(text), 2)) + 1
#         factor_map = {"A": 1, "C": 2, "G": 3, "T": 4}
#
#         table = [[0 for _ in range(N)] for _ in range(M)]
#         table[0] = [factor_map[ch] for ch in text]
#
#         for i in range(1, M):
#             shift_j = 1 << (i-1)
#             for j in range(0, N - shift_j):
#                 table[i][j] = min(table[i-1][j], table[i-1][j + shift_j])
#
#         return table
#
#     def query(self, front, rear):
#
#         L = rear - front + 1
#         K = floor(log(L, 2))
#
#         return min(self.table[K][front], self.table[K][front + L - (1 << K)])
#
#
# def solution(S, P, Q):
#
#     dna_table = DnaSparseTable(S)
#     return [dna_table.query(p, q) for p, q in zip(P, Q)]

## Prefix Sums (N + M)
## https://codility.com/media/train/3-PrefixSums.pdf

def solution(S, P, Q):

    dna_sums = [[0] * (len(S) + 1) for _ in range(4)]

    for i_ch, ch in enumerate(S):
        for i_dna, dna in enumerate("ACGT"):
            dna_sums[i_dna][i_ch+1] = dna_sums[i_dna][i_ch] + (1 if dna == ch else 0)

    factors = []
    # print(dna_sums)

    for p, q in zip(P, Q):
        for i_dna in range(4):
            if dna_sums[i_dna][q+1] - dna_sums[i_dna][p] > 0:
                factors.append(i_dna + 1)
                break

    return factors
