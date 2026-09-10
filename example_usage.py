from client import NeighborJoining

def main():
    print("=== Testing Neighbor-Joining Phylogenetic Tree ===")
    nj = NeighborJoining()
    dist = [
        [0, 5, 9, 9],
        [5, 0, 10, 10],
        [9, 10, 0, 8],
        [9, 10, 8, 0]
    ]
    tree = nj.reconstruct(dist, ["A", "B", "C", "D"])
    print("Reconstructed tree topology (Newick format):", tree)

    assert "A" in tree and "B" in tree
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
