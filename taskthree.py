def common(l1, l2):
    print(list(set(l1)&set(l2)))

def only_in_l1(l1,l2):
    print(list(set(l1)-set(l2)))

l1 = ['a', 'b', 'c']
l2 = ['b','d']
common(l1, l2)
only_in_l1(l1, l2)