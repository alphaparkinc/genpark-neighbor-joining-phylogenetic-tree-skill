# genpark-neighbor-joining-phylogenetic-tree-skill

[![CI](https://github.com/alphaparkinc/genpark-neighbor-joining-phylogenetic-tree-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-neighbor-joining-phylogenetic-tree-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> Neighbor-Joining (NJ) distance-based phylogenetic tree reconstruction algorithm calculating Q-matrices and star tree node clustering.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Bioinformatic Pipeline] -->|Genomic Sequence / Distances| Engine[genpark-neighbor-joining-phylogenetic-tree-skill]
    Engine --> AlignmentEngine[DP Matrix / FM-Index / Tree Topology Engine]
    AlignmentEngine --> Output[(Alignment Score / Phylogeny / State Annotation)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Groundbreaking biological algorithms (Needleman-Wunsch, Smith-Waterman, BWT/FM-Index, NJ Trees, HMMs).
- Native Model Context Protocol (MCP) server support for AI agent bioinformatic analysis.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-neighbor-joining-phylogenetic-tree-skill.git
cd genpark-neighbor-joining-phylogenetic-tree-skill
```

## Quickstart

```bash
python example_usage.py
```
