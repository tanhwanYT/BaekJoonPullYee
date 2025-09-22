import sys
input = sys.stdin.readline

n = int(input())
tree = {}

def preorder(node):
    if(node != '.'):
        left, right = tree[node]
        print(node, end = "")
        preorder(left)
        preorder(right)

def inorder(node):
    if(node != '.'):
        left, right = tree[node]
        inorder(left)
        print(node, end = "")
        inorder(right)

def postorder(node):
    if(node != '.'):
        left, right = tree[node]
        postorder(left)
        postorder(right)
        print(node, end = "")

for i in range(n):
    parent, left, right = map(str, input().split())
    tree[parent] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
