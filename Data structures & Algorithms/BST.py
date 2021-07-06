class BsTree:
    def __init__(self,Rvalue=None):
        self.Rvalue = Rvalue
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.left}{str(self.Rvalue)}{self.right}"

    def _insert(self,ins_val):
        """Takes ins_val as argument,  ins_val --> ins_val to be inserted to the Tree"""
        if not self.Rvalue:
            self.Rvalue = ins_val
        if self.Rvalue > ins_val:
            if not self.left:
                self.left = BsTree(ins_val)
            else:
                self.left._insert(ins_val)
        if self.Rvalue < ins_val:
            if not self.right:
                self.right = BsTree(ins_val)
            else:
                self.right._insert(ins_val)
    
    def _rootval(self):
        """Returns Root Node value of the tree, if the tree is empty return None"""
        return self.Rvalue
    
    def _isEmpty(self):
        """ return Ture if the tree is empty """
        if self.Rvalue == self.left == self.right == None:
            return True
        else:
            return False

    def _search(self,ser_val):
        """Returns true if the value exist in the Tree """
        if self.Rvalue:
            if ser_val == self.Rvalue:
                return True
        if self.Rvalue > ser_val:
            if self.left != None:
                return self.left.search(ser_val)
            else:
                return False
        if self.Rvalue < ser_val:
            if self.right != None:
                return self.right.search(ser_val)
            else:
                return False
                
    def _min(self):
        """returns the min value of the tree """
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.Rvalue

    def _max(self):
        """returns the max value of the tree """
        curr = self
        while curr.right is not None:
            curr = curr.right
        return curr.Rvalue

    def _delete(self,del_val):
        if del_val == self.Rvalue:
            pass

            


a= BsTree()
a._insert(50)
a._insert(60)
a._insert(40)
a._insert(30)
a._insert(45)
a._insert(55)
a._insert(75)
a._insert(75)
print(a._isEmpty())