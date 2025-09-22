import sys
input = sys.stdin.readline

numlist = []

for line in sys.stdin:
    numlist.append(int(line.strip()))

def postorder(node, numlist):
    root = node
    leftnumlist = []
    rightnumlist = []
    if(numlist):
        for i in range(1,len(numlist)):
            if(numlist[i] > node):
                rightnumlist = numlist[i:]
                break
            else:
                leftnumlist.append(numlist[i])
        
        if(leftnumlist): postorder(leftnumlist[0], leftnumlist)
        if(rightnumlist): postorder(rightnumlist[0], rightnumlist)

    print(node)

postorder(numlist[0], numlist)

# def bst(num, current):
#     if (tree):
#         tree[num] = {"left": None, "right": None}
#     if(num > current):
#         if(tree[current]["right"] == None):
#             tree[current]["right"] = num
#         else:
#             bst(num, tree[current]["right"])
#     else:
#         if(tree[current]["left"] == None):
#             tree[current]["left"] = num
#         else:
#             bst(num, tree[current]["left"])
#
# for i in range(1, len(numlist)): 
#     current = numlist[0]
#     num = numlist[i]
#     while True:
#         if num < current:
#             if tree[current]["left"] is None:
#                 tree[current]["left"] = num
#                 tree[num] = {"left": None, "right": None}
#                 break
#             else:
#                 current = tree[current]["left"]
#         else:
#             if tree[current]["right"] is None:
#                 tree[current]["right"] = num
#                 tree[num] = {"left": None, "right": None}
#                 break
#             else:
#                 current = tree[current]["right"]
