graph = {}
graph['pl'] = {}
graph['pl']['gt'] = 15
graph['pl']['ba'] = 20

graph['ps'] = {}
graph['ps']['ba'] = 35
graph['ps']['gt'] = 30

graph['ba'] = {}
graph['ba']['pi'] = 10

graph['gt'] = {}
graph['gt']['pi'] = 20

graph['pi'] = {}



infinity = float("inf")

costs = {}
costs["pl"] = 5
costs["ps"] = 0
costs["ba"] = infinity
costs["gt"] = infinity
costs["pi"] = infinity

parents = {}
parents["pl"] = "gq"
parents["ps"] = "gq"
parents["ba"] = None
parents["gt"] = None
parents["pi"] = None
processed = []


def get_path(dict, end_name):
    path = []
    value = dict[end_name]
    while value is not None:
        value = dict.get(end_name)
        end_name = value
        if value is not None:
            path.append(value)
    return path[::-1]


def find_lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float('inf')
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

if __name__ == '__main__':
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(get_path(parents, 'pi'))
