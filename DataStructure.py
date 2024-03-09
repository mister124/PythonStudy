# stack
# sequential, LIFO(Last In First Out)


class stack:
    # 리스트로 생성
    def __init__(self):
        self.items = []

    # stack의 item 수 return, O(1)
    def __len__(self):
        return len(self.items)

    # stack 변수만으로 stack.items 출력
    def __str__(self):
        return str(self.items)

    # val 삽입, O(1)
    def push(self, val):
        self.items.append(val)

    # Last In return 후 제거, O(1)
    def pop(self):
        try:
            return self.items.pop()
        except:
            print('Stack is empty')

    # Last In return, O(1)
    def top(self):
        try:
            return self.items[-1]
        except:
            print('Stack is empty')

    # stack이 비어있는지 확인
    def isEmpty(self):
        return len(self.items) == 0

    # stack 초기화
    def clear(self):
        self.items = []

    # val 포함 여부 확인
    def isContain(self, val):
        return val in self.items


class node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # head 앞에 node 삽입, O(1)
    def pushFront(self, key):
        newNode = node(key)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # tail 뒤에 node 삽입, O(n)
    def pushBack(self, key):
        newNode = node(key)
        if len(self) == 0:
            self.head = newNode
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = newNode
        self.size += 1

    # head pop, O(1)
    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            size -= 1
            del x  # 객체 x를 메모리에서 삭제
            return key

    # tail pop, O(n)
    def popBack(self):
        if len(self) == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
                self.size -= 1
                return tail
            else:
                prev.next = None
                key = tail.key
                del tail
                self.size -= 1
                return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    def __iterator__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def __len__(self):
        return self.size


class node2:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self


class doublyLinkedList:
    def __init__(self):
        self.head = node2()
        self.size = 0
    # def __iterator__(self):
    # def __str__(self):

    def __len__(self):
        return self.size

    # 조건1: a의 next를 따라가다보면 b가 나옴(a==b 가능)
    # 조건2: a와 b 사이에 head(dummy), x node가 없어야 됨
    # 연산: a와 b 사이를 잘라내서 x의 next에 삽입, O(1)
    # a.p.next=b.n.prev
    # x.next = a, x.n.prev = b
    def splice(self, a, b, x):
        ap, bn, xn = a.prev, b.next, x.next
        ap.next = bn
        bn.prev = ap
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b

    # a를 x 후로 이동, O(1)
    def moveAfter(self, a, x):
        self.splice(a, a, x)

    # a를 x 전으로 이동, O(1)
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    # key 값을 가진 node를 x 후로 삽입, O(1)
    def insertAfter(self,  x, key):
        self.moveAfter(node2(key), x)

    # key 값을 가진 node를 x 전으로 삽입, O(1)
    def insertBefore(self,  x, key):
        self.moveBefore(node2(key), x)

    # key 값을 가진 node를 front에 삽입, O(1)
    def pushFront(self, key):
        self.insertAfter(self.head, key)

    # key 값을 가진 node를 tail에 삽입, O(1)
    def pushBack(self, key):
        self.insertBefore(self.head, key)

    # 탐색 연산: key 탐색, O(n)
    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            else:
                v = v.next
        return None

    # 삭제 연산: node x를 삭제, 탐색 연산 활용, O(n)
    def remove(self, x):
        if x == None or x == self.head:
            return None
        else:
            x.prev.next = x.next
            x.next.prev = x.prev
            del x

    # def popFront(self): O(1)
    # def popBack(self): O(1)
    # def join 두 연결리스트 합침
    # def split 연결리스트를 어떤 node를 기준으로 두 연결리스트로 쪼갬


# hash table
# def findSlot(key):
#     i=f(key)
#     start=i
#     while H[i]==occupied and H[i].key != key:
#         i=(i+1)%m
#         if i == start:
#             return Full
#     return i
# def set(key, value=None):
#     i = findSlot(key)
#     if i == Full: # H 용량 키우기 return None
#     else:
#       if H[i] is occupied:
#           H[i].value=value
#       else:
#           H[i].key, H[i].value = key, value
#       return key
# def search(key):
#     i = findSlot(key)
#     if i == Full: # H 용량 키우기 return None
#     else:
#       if H[i] is occupied:
#           return H[i].value
#       else:
#           return None
# def remove(key): hash function, collision 해소 방식에 따라 성능 달라짐
#     i = findslot(key)
#     if H[i] is unoccupied:
#         return None
#     j = i  # H[i]: 빈 slot, H[j]: 이사해야 할 slot
#     while True:
#         H[i] = None
#         while True:  # H[j] 찾기
#             j = (j+1) % match
#             if H[j] is unoccupied:
#                 return key
#             k = f(H[j].key)
#             if k < i <= j:
#                 break
#         H[i] = H[j]
#         j = i

# cluster 끊어졌을 때 빈칸이 나올 때 까지
# 밀려서 내려온 값들만 땡겨올리기(k=f(H[j].key)<i(빈칸)<j(현재))
# or j<k<i, i<j<k


# heap
# make_heap: heapify-down 사용
# 마지막 순서의 node부터 heap property를 만족할 때 까지
# 더 큰 값을 가진 child node와 swap
# def make_heap(A):
# n = len(A):
# for k in range(n-1, -1, -1):
#     heapify_down(k, n: heap 원소 갯수)
#     # A[k]->heap 성질 만족하는 곳으로
# def heapify_down(k,n):
#     while A[k] != leaf_node:
#         L, R = 2*k+1, 2*k+2
#         m = max_index(A[k], A[L], A[R])
#         if k != m:
#             A[k] <-> A[m]
#             k = m
#         else:
#             break
# def insert(a):
#     A.append(a)
#     A.heapify_up(k: index)
#  while a의 parent node가 더 작으면 계속 교체
# def heapify_up(k):
#     while k>0 and A[(k-1)//2] < A[k]:
#         A[n], A[(k-1)//2] = A[(k-1)//2], A[k]
#         k = (k-1)//2
# def find_max():
#     return A[0]
# def delete_max():
#     if len(A)==0:
#         return None
#     key = A[0]
#     A[0], A[len(A)-1] = A[len(A)-1], A[0]
#     A.pop()
#     heapify_down(0, len(A))
#     return key
#     # 마지막에 있는 node를 root로 후 heapify_down


# BTnode
class BTnode:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = None  # AVLnode

    def __str__(self):
        return str(self.key)

    def preorder(self):  # 현재 방문 중인 node
        if self != None:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):  # 현재 방문 중인 node
        if self != None:
            if self.left:
                self.left.inorder()
            print(self.key)
            if self.right:
                self.right.inorder()

    def postorder(self):  # 현재 방문 중인 node
        if self != None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    # def __iter__(self):
    #     return self.root.__iter___() # pre,in,post order
    # def insert(self, key): key 대소에 따라
    # key의 노드가 있다면 return, 없다면 삽입될 parent node return
    # 추가 조건 필요

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):  # find_loc와 이름만 다름
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

    def insert(self, key):  # O(h)
        p = self.find_loc(key)
        v = BTnode(key)
        # link
        if p == None or p.key != key:
            v = BTnode(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print('key is already in tree')
            return p

    def deleteByMerging(self, x):
        a, b = x.left, x.right
        pt = x.parent
        # c =  x자리를 대체할 node
        # m =  L에서 가장 큰 node
        if a != None:
            c = a
            m = a
            while m.right:
                m = m.right
            if b != None:
                b.parent = m
                m. right = b
        else:
            c = b
        if pt != None:
            if c:
                c.parent = pt
            if pt.key < c.key:
                pt.right = c
            else:
                pt.left = c
        else:
            self.root = c
            if c:
                c.parent = None
        self.size -= 1

    def deleteCopying(self):
        pass

    def rotateRight(self, z):
        if not z:
            return None
        x = z.left
        if x == None:
            return None
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if self.root == z:
            self.root = x
    # rotateLeft


class AVL(BST):  # insert, delete, search에서 height update
    def insert(self, key):  # O(h)
        v = super(AVL, self).insert(key)  # BST의 insert
        # x, y, z 일직선 rotation 1번 or 엇갈림 rotation 2번, O(h)
        # find x: child of y and parent of new, y: z의 child, z: 처음 AVL 꺠진 node, O(h)
        # w = rebalance(x, y, z) : z에 있게 될 node, O(1)
        # if w.parent == None: self.root = w, O(1)
    # def delete(self, u): # O(logn)
    #     v = super(AVL, self).deleteByMerging(u) # height 조건이 깨질 수 있는 가장 깊은 곳의 node
    #     while v != None:
    #         if v is not balanced:
    #             z = v
    #             if z.left.height >= z.right.height:
    #                 y = z.left
    #             else:
    #                 y = z. right
    #             if y.left.height >= y.right.height:
    #                 x = y.left
    #             else:
    #                 x = y. right
    #             v = rebalance(x,y,z) #경우 일직선, 꺽임
    #             w = v
    #             v = v.parent
    #     # v == None
    #     # w == root
    #     self.root = w

    # find x: heavy child of y, y: z의 heavy child, z: 처음 AVL 꺠진 node
    # rebalance 이후 root까지 parent node balance search, O(logn)


# class RBtree(BST):
#     def insert(self, key): # O(logn)
#         x = super(RBtree, self).insert(key)
#         x.color = red
#         # color 재설정
#         # 1. x == T.root: black 2. x.parent.color = black: do nothing
#         # 3. x.parent.color == red and x.uncle color == red:
#         # x.grandparent.color = red, x.parent.color = black, x.uncle.color == black
#         # 4. x.parent.color == red and x.uncle color == black:
#         # x-p-g is linear: right rotation at g, x.grandparent.color = red, x.parent.color = black
#         # x-p-g is triangle: left rotation at p, right rotation at g
#         # and x.grandparent.color = red, x.color = black
#     def delete(self, key): # O(logn), 찾아서 해보기

class setNode:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

    def makeSet(self, x):
        return setNode(x)

    def find(self):
        while self.parent != self:
            self = self.parent
        return self

    def union(self, x, y):
        v, w = x.find(), y.find()
        if v.rank > w.rank:
            v, w = w, v
        v.parent = w
        if v.rank == w.rank:
            w.rank += 1



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
