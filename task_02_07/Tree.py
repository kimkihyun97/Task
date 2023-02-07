import random

class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.memory = []

    def MakeTree(self, sellAry):
        current = TreeNode()
        current.data = sellAry[0]
        self.memory.append(current)
        root = current

        for item in sellAry[1:]:
            next_node = TreeNode()
            next_node.data = item

            current = root
            while True:

                if item == current.data: break
                if current.data < next_node.data:
                    if current.left == None:
                        current.left = next_node
                        self.memory.append(next_node)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = next_node
                        self.memory.append(next_node)
                        break
                    current = current.right

        print('complete tree')
        return self.memory

    def order(self, node):
        if node == None: return
        print(node.data, end='  ')
        TreeNode.order(self, node.left)
        TreeNode.order(self, node.right)

if __name__ == "__main__":
    dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
    sellAry = [random.choice(dataAry) for _ in range(20)]
    tree = TreeNode()
    root = tree.MakeTree(sellAry)[0]
    print('sell arr ->', end='  ')
    tree.order(root)