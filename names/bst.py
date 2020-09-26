class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # * IF LESS, INSERT
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
                
        # * IF GREATER, INSERT
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        # * IF ROOT VALUE == TO TARGET
        if self.value == target:
            return True
        
        # * A VALUE LESS ROOT, IS LEFT
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        # * ANY VALUE GREATER THAN ROOT, IS TO RIGHT
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        while not self.right:
            return self.right.value
        else:
            return self.right.get_max()