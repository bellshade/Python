# ford fulkerson adalah algoritma greedy
# yang menghitung aliran maksimum dalam jaringan
# aliran atau dalam grafik

# cara kerja algoritma
# - inisialisasi aliran di semua sisi ke 0
# - meskipun ada jalur augmentasi antara sumber dan
#   sink, tambahkan jalur ke aliran
# - memperbarui grafik dari sisa

# algoritma ini digunakan dalam
# - pipa distribusi air
# - problem pencocokan bipartit

def bfs(graph, s, t, parent) -> bool:
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def FordFulkerson(graph, source, sink):
    """
    >>> graph =  [
    ... [0, 16, 13, 0, 0, 0],
    ... [0, 0, 10, 12, 0, 0],
    ... [0, 4, 0, 0, 14, 0],
    ... [0, 0, 9, 0, 0, 20],
    ... [0, 0, 0, 7, 0, 4],
    ... [0, 0, 0, 0, 0, 0],
    ... ]
    >>> source, sink = 0, 5
    >>> FordFulkerson(graph, 0, 5)
    23
    """
    parent = [-1] * (len(graph))
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == "__main__":
    import doctest

    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]

    source, sink = 0, 5
    print(FordFulkerson(graph, source, sink))

    doctest.testmod()
