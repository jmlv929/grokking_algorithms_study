
#适用于无加权图  寻找最短路径
from collections import deque  #队列 先进先出


def search_person(graph, name):  # name是根节点的名字 graph是一个字典/散列表
    search_queue = deque()  #建立一个新队列
    search_queue += graph['you']
    searched_people = []
    while search_queue:
        people = search_queue.popleft()
        if people not in searched_people:   #检查过就不再检查了
            if people == name:
                print('I find !')
                return True
            else:
                search_queue += graph[people]
                searched_people += people
    return False



if __name__ == '__main__':
    graph = {}
    graph['you'] = ['alice','bob','claire']

    graph['alice'] = ['peggy']
    graph['bob'] = ['anuj','peggy']
    graph['claire'] = ['thom','jonny']

    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_person(graph, 'thom')



