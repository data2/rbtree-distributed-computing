import sys
import random
import math
# 创建节点
class Node():
    def __init__(self, tree_node_value):
        self.parent = None
        self.left_tree_node = None
        self.right_tree_node = None
        self.color = 1
        self.tree_node_value = tree_node_value
        self.machine_id_num = None

class RedBlackTree():
    def __init__(self):
        self.Nil = Node(0)
        self.Nil.color = 0
        self.Nil.left_tree_node = None
        self.Nil.right_tree_node = None
        self.root = self.Nil
        self.black_nodes = []

    # 前序
    def pre_order_helper(self, node):
        if node != Nil:
            sys.stdout.write(node.tree_node_value + " ")
            self.pre_order_helper(node.left_tree_node)
            self.pre_order_helper(node.right_tree_node)

    # 中序
    def in_order_helper(self, node):
        if node != Nil:
            self.in_order_helper(node.left_tree_node)
            sys.stdout.write(node.tree_node_value + " ")
            self.in_order_helper(node.right_tree_node)

# 后根
    def post_order_helper(self, node):
        if node != Nil:
            self.post_order_helper(node.left_tree_node)
            self.post_order_helper(node.right_tree_node)
            sys.stdout.write(node.tree_node_value + " ")

    # 搜索树
    def search_tree_helper(self, node, key):
        if node == Nil or key == node.tree_node_value:
            return node

        if key < node.tree_node_value:
            return self.search_tree_helper(node.left_tree_node, key)
        return self.search_tree_helper(node.right_tree_node, key)

    # 删除后平衡树
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left_tree_node:
                s = x.parent.right_tree_node
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_tree_node_rotate(x.parent)
                    s = x.parent.right_tree_node

                if s.left_tree_node.color == 0 and s.right_tree_node.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right_tree_node.color == 0:
                        s.left_tree_node.color = 0
                        s.color = 1
                        self.right_tree_node_rotate(s)
                        s = x.parent.right_tree_node

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right_tree_node.color = 0
                    self.left_tree_node_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left_tree_node
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_tree_node_rotate(x.parent)
                    s = x.parent.left_tree_node

                if s.right_tree_node.color == 0 and s.right_tree_node.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left_tree_node.color == 0:
                        s.right_tree_node.color = 0
                        s.color = 1
                        self.left_tree_node_rotate(s)
                        s = x.parent.left_tree_node

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left_tree_node.color = 0
                    self.right_tree_node_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left_tree_node:
            u.parent.left_tree_node = v
        else:
            u.parent.right_tree_node = v
        v.parent = u.parent

    # 节点删除
    def delete_node_helper(self, node, key):
        z = self.Nil
        while node != self.Nil:
            if node.tree_node_value == key:
                z = node

            if node.tree_node_value <= key:
                node = node.right_tree_node
            else:
                node = node.left_tree_node

        if z == self.Nil:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left_tree_node == self.Nil:
            x = z.right_tree_node
            self.__rb_transplant(z, z.right_tree_node)
        elif (z.right_tree_node == self.Nil):
            x = z.left_tree_node
            self.__rb_transplant(z, z.left_tree_node)
        else:
            y = self.minimum(z.right_tree_node)
            y_original_color = y.color
            x = y.right_tree_node
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right_tree_node)
                y.right_tree_node = z.right_tree_node
                y.right_tree_node.parent = y

            self.__rb_transplant(z, y)
            y.left_tree_node = z.left_tree_node
            y.left_tree_node.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # 插入后平衡树
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right_tree_node:
                u = k.parent.parent.left_tree_node
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left_tree_node:
                        k = k.parent
                        self.right_tree_node_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_tree_node_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right_tree_node

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right_tree_node:
                        k = k.parent
                        self.left_tree_node_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_tree_node_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree
    def __print_helper(self, node, indent, last):
        if node != self.Nil:
            # sys.stdout.write(indent)
            if node.color == 0:
                self.black_nodes.append(node)
            if last:
                # sys.stdout.write("R----")
                indent += "     "
            else:
                # sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            # print(str(node.tree_node_value) + "(" + s_color + ")" + str(node.machine_id_num))
            self.__print_helper(node.left_tree_node, indent, False)
            self.__print_helper(node.right_tree_node, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left_tree_node != self.Nil:
            node = node.left_tree_node
        return node

    def maximum(self, node):
        while node.right_tree_node != self.Nil:
            node = node.right_tree_node
        return node

    def successor(self, x):
        if x.right_tree_node != self.Nil:
            return self.minimum(x.right_tree_node)

        y = x.parent
        while y != self.Nil and x == y.right_tree_node:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left_tree_node != self.Nil):
            return self.maximum(x.left_tree_node)

        y = x.parent
        while y != self.Nil and x == y.left_tree_node:
            x = y
            y = y.parent

        return y

    def left_tree_node_rotate(self, x):
        y = x.right_tree_node
        x.right_tree_node = y.left_tree_node
        if y.left_tree_node != self.Nil:
            y.left_tree_node.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left_tree_node:
            x.parent.left_tree_node = y
        else:
            x.parent.right_tree_node = y
        y.left_tree_node = x
        x.parent = y

    def right_tree_node_rotate(self, x):
        y = x.left_tree_node
        x.left_tree_node = y.right_tree_node
        if y.right_tree_node != self.Nil:
            y.right_tree_node.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right_tree_node:
            x.parent.right_tree_node = y
        else:
            x.parent.left_tree_node = y
        y.right_tree_node = x
        x.parent = y

    def insert(self, key, machine_id_num):
        node = Node(key)
        node.parent = None
        node.tree_node_value = key
        node.left_tree_node = self.Nil
        node.right_tree_node = self.Nil
        node.color = 1
        node.machine_id_num = machine_id_num

        y = None
        x = self.root

        while x != self.Nil:
            y = x
            if node.tree_node_value < x.tree_node_value:
                x = x.left_tree_node
            else:
                x = x.right_tree_node

        node.parent = y
        if y == None:
            self.root = node
        elif node.tree_node_value < y.tree_node_value:
            y.left_tree_node = node
        else:
            y.right_tree_node = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, tree_node_value):
        self.delete_node_helper(self.root, tree_node_value)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


def perform_try(machine_x,
    accuracy_error,
    a_try_times,
    a_try_time_tree_num,
    a_try_time_tree_node_random_num):
    for o in range(a_try_times): #  times try
        tree_list = []
        for z in range(a_try_time_tree_num):
            rb = RedBlackTree()
            x = 0
            # num of rb-tree node
            node_y = machine_x * random.uniform(
                0,a_try_time_tree_node_random_num) 
            for y in random.sample(range(0,1000000000),
                math.floor(node_y)):
                x = 0 if x >= machine_x else x
                rb.insert(y ,x)
                x = x + 1
            rb.print_tree()
            # print(len(rb.black_nodes))
            tree_list.append(rb)
        # print(len(tree_list))

        low = 0
        for tree in tree_list:
            black_machine_arr = []
            for node in tree.black_nodes:
                black_machine_arr.append(node.machine_id_num)
            # print(black_machine_arr)
            dict = {}
            for black_num in black_machine_arr:
                dict[black_num] = dict.get(black_num,0) + 1 
            # print(dict)
            #-min(dict.values())/sum(dict.values()))
            if len(dict) >0 and (max(dict.values())/sum(dict.values())-min(dict.values())/sum(dict.values()))  > accuracy_error :
                low = low + 1
        print("匀散波动误差小于"
            +str(accuracy_error * 100)
            +"%的稳定性为：" 
            + str((1-low / len(tree_list))*100) 
            + "%")

if __name__ == "__main__":
    perform_try(19100,0.0001,100,100,5)
 



