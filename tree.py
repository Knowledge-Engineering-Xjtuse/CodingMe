# -*- coding: utf-8 -*-

"""
@author: stop
"""

class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#深度
def depth(tree):
    if tree == None:
        return 0
    left,right = depth(tree.left),depth(tree.right)
    return max(left,right) + 1

#前序遍历
def pre_order(tree):
    if tree == None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

#中序遍历
def mid_order(tree):
    if tree==None:
        return
    mid_order(tree.left)
    print(tree.data)
    mid_order(tree.right)

#后序遍历
def post_order(tree):
    if tree==None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)

#层次遍历
def level_order(tree):
     if tree == None:
        return
     q = []
     q.append(tree)
     while q:
         current = q.pop(0)
         print(current.data)
         if current.left != None:
            q.append(current.left)
         if current.right != None:
            q.append(current.right)

if __name__=='__main__':

    tree = node('D',
                node('B',
                     node('A'),
                     node('C')
                     ),
                node('E',
                     right = node('G',
                                  node('F')
                                  )
                     )
                )
    print('前序遍历：')
    pre_order(tree)
    print('\n')
    print('中序遍历：')
    mid_order(tree)
    print('\n')
    print('后序遍历：')
    post_order(tree)
    print('\n')
    print("层次遍历")
    # level2_order(tree)