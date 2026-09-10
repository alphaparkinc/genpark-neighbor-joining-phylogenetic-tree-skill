class NeighborJoining:
    """
    Neighbor-Joining (NJ) Phylogenetic Tree Reconstruction.
    Clusters taxa by evaluating Q-matrix rate differences.
    """
    def reconstruct(self, dist_matrix, labels):
        names = list(labels)
        D = [row[:] for row in dist_matrix]

        while len(names) > 2:
            n = len(names)
            r = [sum(D[i]) / (n - 2) for i in range(n)]

            min_q = float("inf")
            best_pair = (0, 1)
            for i in range(n):
                for j in range(i + 1, n):
                    q = (n - 2) * D[i][j] - sum(D[i]) - sum(D[j])
                    if q < min_q:
                        min_q = q
                        best_pair = (i, j)

            i, j = best_pair
            new_name = f"({names[i]},{names[j]})"

            new_dist = []
            for k in range(n):
                if k != i and k != j:
                    d_uk = (D[i][k] + D[j][k] - D[i][j]) / 2.0
                    new_dist.append(d_uk)

            new_D = []
            kept_indices = [k for k in range(n) if k != i and k != j]
            for row_idx in kept_indices:
                new_row = [D[row_idx][col_idx] for col_idx in kept_indices]
                new_D.append(new_row)

            for idx, d_val in enumerate(new_dist):
                new_D[idx].append(d_val)
            new_dist.append(0.0)
            new_D.append(new_dist)

            names = [names[k] for k in kept_indices] + [new_name]
            D = new_D

        return f"({names[0]},{names[1]})"
