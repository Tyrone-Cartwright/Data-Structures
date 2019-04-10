class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_tree = BinarySearchTree(value)

        if value < self.value:
            if self.left == None:
                self.left = new_tree

            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

    def get_max(self):
        while self.right is not None:
            self = self.right
        return self.value

    def for_each(self, cb):
        if self.value is None:
            cb(self.value)
        elif self.left is None and self.right is None:
            cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)
            cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
            cb(self.value)
