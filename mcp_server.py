import sys
import json
from client import NeighborJoining

def main():
    nj = NeighborJoining()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "reconstruct":
            tree = nj.reconstruct(params.get("dist_matrix", []), params.get("labels", []))
            res = {"tree": tree}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
