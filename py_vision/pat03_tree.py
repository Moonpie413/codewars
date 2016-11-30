#!/usr/bin/env python3
# -*- coding:utf-8 -*-

' 03-树2 List Leaves '

from collections import deque

class TNode(object):
    ' node '
    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    @property
    def left(self):
        ' getter method of left '
        return self.__left

    @property
    def right(self):
        'getter method of right'
        return self.__right

    def __str__(self):
        return 'left: %s, right: %s' % (self.left, self.right)

class Tree(object):
    ' class of Tree '
    def __init__(self):
        self.index = 0
        self.__creat_tree()
        self.root = self.__find_root()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.treelength:
            raise StopIteration
        left = self.treelist[self.index].left
        right = self.treelist[self.index].right
        self.index += 1
        return (left, right)

    def __creat_tree(self):
        ' 创建一个包含树的list '
        self.treelength = int(input('input tree length: \n'))
        self.treelist = []
        print('please input tree nodes')
        for i in range(self.treelength):
            nodestr = input('input for node %d : ' % i)
            self.treelist.append(TNode(nodestr[0], nodestr[1]))

    def __find_root(self):
        ' find root index '
        lis = [str(x) for x in range(self.treelength)]
        for node in self.treelist:
            if node.left != '-' and node.left in lis:
                lis.remove(node.left)
            if node.right != '-' and node.right in lis:
                lis.remove(node.right)
        return int(lis[0])

    def find_childs(self):
        ' find all childs '
        queue = deque([self.root])
        result = []
        while len(queue) != 0:
            parent = queue.popleft()
            left = self.treelist[parent].left
            right = self.treelist[parent].right
            if left == '-' and right == '-':
                result.append(str(parent))
                continue
            if left != '-':
                queue.append(int(left))
            if right != '-':
                queue.append(int(right))
        return result

    def print_tree(self):
        ' simple print the entir tree '
        for i in self.treelist:
            print(i)

def test():
    ' simple test '
    t = Tree()
    print(' '.join(t.find_childs()))

if __name__ == '__main__':
    test()
