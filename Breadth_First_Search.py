from collections import deque

graph = {'a': ['b', 'c', 'd'],
         'e': ['a', 'b'],
         'c': ['d'],
         'f': ['a', 'm'],
         'd': ['f']}


def check(item):
    return True if item[-1] == 'm' else False


def bfs(graph: dict, top: str) -> bool:
    searched_list = []
    series = deque()
    series += graph[top]
    while series:
        item = series.popleft()
        if item not in searched_list:
            if check(item):
                print(item)
                return True
            else:
                rows = graph.get(item)
                if rows is not None:
                    series += rows
                    searched_list.append(item)
    return False


if __name__ == '__main__':
    bfs(graph, 'a')
