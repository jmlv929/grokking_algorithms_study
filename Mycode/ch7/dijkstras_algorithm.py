
#适用于加权图
#只适用于 有向无环图 处理不了负权边 主要根据costs中的键 先找到最小的数值 查找其邻居 并更新其数值 以及  更新其父节点
#节点一旦被处理 表示前往该节点没有更便宜的路径！！

def dijkstras(graph, costs, parents):
    processed = []
    node = search_lowest_costs(costs, processed)
    while node is not None:    #能找到node 就一直进行下去  主要
        neighbors = graph[node]   #该node节点的邻居
        cost = costs[node]   #该node节点的数值 表示到达该节点的最短时间（加权） 第一次查找时 最小的即为最短的 这是这个算法决定的  只能处理有向无环，并负权边也处理不了 因为节点已经更新过就不再更新
        for i in neighbors.keys():
            new_cost = cost + neighbors[i]
            if new_cost < costs[i]:        #最短时间小于当前邻居对应的时间
                costs[i] = new_cost
                parents[i] = node
        processed += [node]     #节点一旦被处理  表示没有前往该节点更 便宜 的路径   加入处理过的列表 之后就不再处理
        node = search_lowest_costs(costs, processed)
    return costs, parents

def search_lowest_costs(costs_dict, processed_list):  #寻找costs值最低的node 在pocessed列表中的就不再查找 因为已经计算过最短路径
    low_cost_keys = None
    low_cost = float('inf')
    for item in costs_dict:
        if item not in processed_list:
            if costs_dict[item] < low_cost:
                low_cost = costs_dict[item]
                low_cost_keys = item
    return low_cost_keys

if __name__ == '__main__':
    graph = {}         #创建 图  包括每个节点 以及 他的邻居（另一个字典）

    graph['start'] = {}
    graph['start']['A'] = 6
    graph['start']['B'] = 2

    graph['A'] = {}
    graph['A']['end'] = 1

    graph['B'] = {}
    graph['B']['A'] = 3
    graph['B']['end'] = 5

    graph['end'] = {}

    costs = {}
    costs['A'] = 6
    costs['B'] = 2
    costs['end'] = float('inf')

    parents = {}
    parents['A'] = 'start'
    parents['B'] = 'start'
    parents['end'] = None

    print(dijkstras(graph, costs, parents))
