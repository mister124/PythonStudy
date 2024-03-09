from data_structure import stack

# 최대공약수 구하기


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

# 올바른 괄호 사용 판단


def correct_bracket(str):
    b_stack = stack()
    for i in str:
        if i == '(':
            b_stack.push(i)
        elif i == ')':
            if len(b_stack) == 0:
                return False
            else:
                b_stack.pop()
    if len(b_stack) == 0:
        return True
    else:
        return False

# infix->postfix->calculation


def in_to_post(str):
    outstack = []
    opstack = stack()
    op = ['+', '-', '*', '/', '(', ')']
    for i in str:
        if i not in op:
            outstack.append(i)
        else:
            if i == '(':
                opstack.push(i)
            elif i == ')':
                while opstack.top() != '(':
                    outstack.append(opstack.pop())
                opstack.pop()
            elif i == '+' or '-':
                if len(opstack) == 0 or opstack.top() == '(':
                    opstack.push(i)
                else:
                    outstack.append(opstack.pop())
                    opstack.push(i)
            elif i == '*' or '/':
                if len(opstack) == 0 or opstack.top() in ['(', '+', '-']:
                    opstack.push(i)
                else:
                    outstack.append(opstack.pop())
                    opstack.push(i)
    while len(opstack) != 0:
        outstack.append(opstack.pop())
    return ''.join(outstack)


print(in_to_post('A+B*(C-D)/E'))

# 재귀적 DFS
# currTime = 1
# def DFS(v):  # v 방문 중
#     mark[v] = 'visited'
#     pre[v] = currTime
#     currTime += 1
#     for each edge(v, w): # v의 인접한 모든 vertex w에 대해서
#         if mark[w] != 'visited':
#             parent[w] = v
#             DFS(w)
#     # v에 인접한 모든 vertex를 고려함
#     post[v] = currTime # v에서 DFS 완료된 시간
#     currTime += 1
# def DFS(G): # G를 DFS search
#     for all vertex in G:
#         mark[v] = 'unvisited'
#     for all vertex in v:
#         if mark[v] != 'visited':
#             DFS(v)
# 비재귀적 DFS
# def DEF(s): # s부터 DFS 시작
#     stack.push((None: parent node, s: current node))
#     while stack is not empty:
#         p, v = stack.pop()
#         if v is 'unvisited':
#             mark[v] = 'visited'
#             parent[v] = p
#             for each edge(v, w): # 후순위부터
#                 if w is 'unvisited':
#                 stack.push((v, w))


# def BellmanFord():
#     for i in range(n-1):
#         for each edge(u, v) in G:
#             if dist[u] > dist[u] + w(u, v):
#                 relax(u, v)


# def Dijkstra():
#     s = 0 # node 0 is source
#     dist = [0, INF, INF, ..., INF]
#     parent = [None, ..., None]
#     heap <- all nodex v with key dist[v]
#     while heap is not empty:
#         u = Q.deleteMin()
#         for each edge u -> v:
#             relax(u, v)
#             Q.decreaseKey(v, dist[v]):heapify_up in heap
#     return dist, parent