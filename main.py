# Inserir 30 números aleatórios, tamanho: Árvore binária
#from typing_extensions import Self
""" 
from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None 
        
    def size(self):
            if self.left and self.right:
                return 1 + self.left.size() + self.right.size()
            elif self.left:
                return 1 + self.left.size()
            elif self.right:
                return 1 + self.right.size()
            else:
                return 1

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def inserir_30(self):
        for i in range(30):
            value = randint(1,100)
            self.insert(value)

"""

# Caminhamento em árvores binárias: pós ordem, em ordem 
# e pré ordem

"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 
class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
     
    def inorder(self, root, result = []):
        if root:
            self.inorder(root.left, result)
            # print(root.val)
            result.append(root.val)
            self.inorder(root.right, result)

    def preorder(self, root, result = []):
        if root:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)
        
    def postorder(self, root, result = []):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.val)
        
        
        

    
bst = BST()
# Driver program to test the above functions
# Let us create the following BST
#     50
#   /   \
#  30   70
# / \   / \
#20 40 60 80
 
r = Node(50)
r = bst.insert(r, 100)
r = bst.insert(r, 20)
r = bst.insert(r, 40)
r = bst.insert(r, 70)
r = bst.insert(r, 60)
r = bst.insert(r, 80)

# Print inoder traversal of the BST
#mylist = [] 
#bst.inorder(r, mylist)
#print(mylist)
"""


# Árvore AVL, a árvore que tem o balanceamento,
# a altura e troca as posições dos nós

""" 
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 

class AVLTree(object):
    list1 = []
      
    def insert(self, root, key):
        if not root:
                return TreeNode(key)
        elif key < root.val:
                root.left = self.insert(root.left, key)
        else:
                root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
    
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
                return self.rightRotate(root)
    
        if balance < -1 and key > root.right.val:
                return self.leftRotate(root)
    
        if balance > 1 and key > root.left.val:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
    
        if balance < -1 and key < root.right.val:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
    
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        self.list1.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        
        #print(self.list1)
        
    def search(self, value):
        for i in range(len(self.list1)):
            if (self.list1[i] == value):
                return self.list1[i]
        
 
 
#tree = AVLTree()
#root = None
 
#root = tree.insert(root, 10)
#root = tree.insert(root, 20)

#print(root.right.val)

#     04
#   /   \
#  02    06
# / \   / \
#01 03 05 07

Os menores valores localizados à esquerda
"""

# Caminhamento em largura: usamos a fila
# primeiro a entrar e primeiro a sair.

"""
from collections import deque

class Node:
     def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root=None):
        self.root = root        
            
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
        
    def breadth_first_traversal(self, root):
        if not root: return []
        queue, result = deque([root]), []
        
        number = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)
                number.append(node.value)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
             
        solute = number
        
        return solute
        
        
#     04
#   /   \
#  02    06
# / \   / \
#01 03 05 07

R: 04, 02, 06, 01, 03, 05, 07

"""

# Árvore heap:
#Heaps são árvores binárias. 
#É importante deixar claro desde 
#já que são árvores binárias, 
#mas não são árvores binárias de pesquisa.
#Mais especificamente, duas propriedades 
#definem o Heap:

#1. O valor de um nó é maior ou 
#igual ao valor de seus filhos;

#2. O Heap é uma árvore binária 
#completa ou quase-completa 
#da esquerda para a direita.

""" 
from heapq import heappush, heappop, heapify

class BinaryTreeHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heappush(self.heap, value)

    def remove(self):
        heappop(self.heap)

    def find_parent(self, index):
        return (self.heap[index])

    def find_left_child(self, index):
        return self.heap[2 * index]

    def find_right_child(self, index):
        return self.heap[2 * index + 1]
    
    def print_heap(self):
        print(self.heap)


    # Outras funções podem vir aqui.

tree = BinaryTreeHeap()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print("-> ", tree.find_parent(2))
print("-> ", tree.find_left_child(0))
print("-> ", tree.find_right_child(0))


tree.remove()
tree.print_heap()

"""

# Árvore heap maximal O heap é gerado e mantido 
# no próprio vetor a ser ordenado. Para uma ordenação 
# crescente, deve ser construído um heap máximo 
# (o maior elemento fica na raiz). Para uma ordenação 
# decrescente, deve ser construído um heap mínimo 
# (o menor elemento fica na raiz):
#

""" 
import heapq

class BinaryHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def insert(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def to_list(self):
        convert_positive = [ -x for x in self.data]
        return (convert_positive)

O maior valor fica na raiz
    [88]
    heap.insert(87)
    assert heap.to_list() == [88, 87]
    heap.insert(73)
    assert heap.to_list() == [88, 87, 73]
    heap.insert(47)
    assert heap.to_list() == [88, 87, 73, 47]
"""

#Grafos: GraphLib: https://docs.python.org/pt-br/3/library/graphlib.html
#Grafos: trabalhando com grafos

# Primeiro instalar o networkx
# - pip install networkx
"""
import networkx as nx

# cria um grafo vazio
G = nx.Graph()

# adiciona vértices
G.add_nodes_from([1, 2, 3, 4, 5])

# adiciona arestas
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# calcula o caminho mais curto entre o vértice 1 e o vértice 5
path = nx.shortest_path(G, source=1, target=5)

# mostra o caminho mais curto
print("Caminho mais curto:", path)

# mostra o tamanho do grafo
print("Tamanho do grafo:", G.number_of_nodes())

R: 
Caminho mais curto: [1, 2, 4, 5]
Tamanho do grafo: 5

Um grafo é uma estrutura matemática usada 
para representar relações entre objetos. 
Ele consiste em um conjunto de vértices 
(também chamados de nós) e um conjunto de arestas 
(também chamados de arcos) que conectam esses vértices. 
Cada aresta pode ter um peso ou custo associado que 
representa alguma informação adicional, como distância 
tempo, ou custo.

Grafos são usados em uma variedade de aplicações, 
desde a representação de redes sociais até a modelagem 
de rotas de transporte e comunicação. Eles são comumente 
usados em algoritmos de busca, onde é preciso encontrar 
o caminho mais curto entre dois pontos em um grafo.

Existem diferentes tipos de grafos, como grafos 
direcionados (onde as arestas têm direção) e grafos 
não-direcionados (onde as arestas não têm direção), grafos 
ponderados (onde as arestas têm pesos) e grafos 
não-ponderados (onde as arestas não têm pesos), 
entre outros. Cada tipo de grafo tem 
propriedades e características diferentes, que afetam 
o comportamento dos algoritmos que operam sobre eles.

Aqui está um exemplo simples de um grafo 
não-direcionado e não-ponderado:

     A
    / \
   /   \
  B     C
   \   /
    \ /
     D
Nesse grafo, os vértices são representados 
por letras maiúsculas (A, B, C e D) e as arestas 
são representadas por linhas que ligam os vértices. 
Note que as arestas não têm direção e não têm pesos 
associados.

Por exemplo, existe uma aresta entre o vértice A e o 
vértice B, uma aresta entre o vértice A e o vértice C, uma 
aresta entre o vértice B e o vértice D, e assim por diante.

Esse é um exemplo simples de um grafo que pode ser 
usado em algoritmos de busca e outros problemas de grafos.

"""

#Para calcular o caminho mais longo do grafo:
"""
mport networkx as nx

# cria um grafo vazio
G = nx.Graph()

# adiciona vértices
G.add_nodes_from([1, 2, 3, 4, 5])

# adiciona arestas com pesos
G.add_weighted_edges_from([(1, 2, 1), (1, 3, 2), (2, 3, 3), (2, 4, 4), (3, 4, 5), (4, 5, 6)])

# calcula o caminho mais longo a partir do vértice 1
path = nx.dag_longest_path(G, source=1)

# mostra o caminho mais longo
print("Caminho mais longo:", path)

Nesse exemplo, o grafo tem pesos nas arestas e o algoritmo 
de caminho mais longo usado é o dag_longest_path, que é 
adequado para grafos acíclicos direcionados (DAGs). Note 
que esse algoritmo não funciona para grafos que contêm 
ciclos.

Ao executar esse código, você verá a seguinte saída:

R: 
Caminho mais longo: [1, 2, 4, 5]

sso indica que o caminho mais longo no grafo 
começa no vértice 1 e passa pelos vértices 2, 4 e 5, com um 
comprimento total de 11 (1 + 4 + 6).

"""

#Grafos sem arestas:
"""
Um grafo pode não ter nenhuma aresta, ou seja, pode 
ser um conjunto de vértices sem conexões entre eles. 
Esse tipo de grafo é chamado de grafo vazio ou nulo.

Por exemplo, um grafo vazio com 4 vértices pode ser 
representado da seguinte forma:

 o   o   o   o
 
Nesse grafo, cada vértice é representado por um 
círculo (o) e não há nenhuma aresta que conecte os 
vértices. Esse grafo pode ser útil em certos c
ontextos teóricos ou para representar situações 
onde não há relação entre os objetos representados 
pelos vértices.

"""