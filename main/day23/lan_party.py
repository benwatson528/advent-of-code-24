import networkx as nx


def solve_p1(networks) -> int:
    g = build_graph(networks)
    fully_connected_subgraphs = [s for s in nx.enumerate_all_cliques(g) if len(s) == 3]
    return len(
        [subgraph for subgraph in fully_connected_subgraphs if any(computer.startswith("t") for computer in subgraph)])


def solve_p2(networks) -> str:
    g = build_graph(networks)
    fully_connected_subgraphs = [s for s in nx.enumerate_all_cliques(g)]
    return ",".join(sorted(max(fully_connected_subgraphs, key=len)))


def build_graph(networks):
    all_computers = {computer for n in networks for computer in n}
    g = nx.Graph()
    g.add_nodes_from(all_computers)
    for n in networks:
        g.add_edge(n[0], n[1])
        g.add_edge(n[1], n[0])
    return g
