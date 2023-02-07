import os
from task_02_07 import Tree

if __name__ == '__main__' :
    fname_ary=[]
    folder_name="C:/Program Files/Common Files/"
    for dirName, subDirlist,fnames in os.walk(folder_name) :
        for fname in fnames :
            fname_ary.append(fname)

    tree_floder= Tree.TreeNode()
    root = tree_floder.MakeTree(fname_ary)[0]
    print('floder ->', end='  ')
    tree_floder.order(root)