
# cnet5051

A Python package for generating and analyzing network models with tools to aid in formatting degree distributions for visualization.

---

## Installation

You can install **cnet5051** via pip:

```bash
pip install cnet5051
```

---


## Models

**`configuration_model(deg_seq: list[int]) -> nx.MultiGraph`**

Generates a **MultiGraph** from a degree sequence.

**Parameters**:
- `deg_seq` (list of integers): The degree sequence for the graph.

**Returns**:
- `nx.MultiGraph`: A graph where each vertex has the assigned degree.

**Example code:**
```python
import cnet5051

deg_seq = [2, 3, 3, 4]
graph = cnet5051.configuration_model(deg_seq)
```


---



**`chung_lu_model(deg_seq: list[int]) -> nx.Graph`**

Generates a **Graph** using the Chung-Lu model from the given degree sequence.

**Parameters**:
- `deg_seq` (list of integers): The degree sequence for the graph.

**Returns**:
- `nx.Graph`: A graph based on the Chung-Lu model.

**Example code:**

```python
import cnet5051

deg_seq = [2, 2, 3, 4]
graph = cnet5051.chung_lu_model(deg_seq)
```
---

## Plotting

**`degree_distribution(G, number_of_bins=15, log_binning=True, density=True, directed=False)`**

Calculates and returns the degree distribution of a network.

**Parameters**:
- `G` (nx.Graph): The network whose degree distribution to calculate.
- `number_of_bins` (int): The number of bins for the output vectors.
- `log_binning` (bool): Whether to use log binning for a log-log axis.
- `density` (bool): If `True`, returns probability density. If `False`, returns node counts.
- `directed` (bool or str): If `False`, assumes an undirected network. If `True`, specifies "in" or "out" for in- or out-degree distributions in a directed network.

**Returns**:
- `bins_out` (np.ndarray): The binned degree values.
- `probs` (np.ndarray): The probability densities or node counts.

**Example code:**
```python
import cnet5051
import networkx as nx

G = nx.erdos_renyi_graph(100, 0.05)
bins, probs = cnet5051.degree_distribution(G)
```

**`log_binning(items: list, number_of_bins: int = 15, density: bool = True)`**

```python
import numpy as np

def log_binning(items: list, number_of_bins: int = 15, density: bool = True):
    items = np.array(items)
    bins_out = np.logspace(np.log10(min(items)), np.log10(max(items)), number_of_bins)
    
    hist, _ = np.histogram(items, bins=bins_out, density=density)
    
    return bins_out, hist

# Example usage of log_binning
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
bins, probs = log_binning(data, number_of_bins=5)
```
---

## Generators

**`preferential_generator(n: int, a: float) -> nx.Graph`**

Generates a **Graph** with `n` nodes using preferential attachment.

**Parameters**:
- `n` (int): The number of nodes in the graph.
- `a` (float): Exponent to modify the probability of each new node connecting to an existing node.

**Returns**:
- `nx.Graph`: A graph generated using the preferential attachment model.

**Example code:**
```python
import cnet5051

n = 100
a = 0.5
graph = cnet5051.preferential_generator(n, a)
```
---

**`random_walk_generator(n: int, p: float) -> nx.Graph`**

Generates a **Graph** with `n` nodes, where each node connects to a random node with a probability `p` of attaching to the neighbor of a random node.

**Parameters**:
- `n` (int): The number of nodes in the graph.
- `p` (float): The probability that a node connects to a neighbor of a random node.

**Returns**:
- `nx.Graph`: A graph generated using the random walk model.

**Example code:**
```python
import cnet5051

n = 100
p = 0.3
graph = cnet5051.random_walk_generator(n, p)
```
---

## Copyright

- Copyright © 2025 Adam Perhala.
- Free software distributed under the [MIT License](./LICENSE).


