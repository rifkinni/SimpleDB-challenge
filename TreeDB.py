from Timing import Timer


class Node(object):
  """
    A node object representing each entry in a tree
    Attributes:
      left - left child node
      right - right child node
      parent - parent node
      key - database entry
      val - value of database entry
  """
  def __init__(self, parent=None, key=None, val=None):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.val = val

class TreeDB(object):
  """
  A binary search tree database
  Attributes:
    mainDB - root node of the main database
    rootOccurrences - root node of the occurrences database

  Methods:
    set: add a new value to the db and update number of occurrences
    setMain: add a new value recursively to the main database
    setOccurrences: update recursively the number of occurrences
    get: return the value for the name of an entry
    numequal: return the number of occurrences for a given value
    search: recursively searches the tree and returns a node with the given key
    unset: remove a value from the db and update number of occurrences
    unsetMain: remove a node from the tree
    unsetRoot: handles the edge case where the node to unset is also the tree's root
    unsetOccurrences: update number of occurrences
    updateParents: update the node parent attribute on unset
    printNodes: debugging method to recursively display each node
    parseInput: parses stdin to determine which method to call
  """
  def __init__(self):
    self.mainDB = Node()
    self.rootOccurrences = Node()
  
  def set(self, key, val):
    '''
    key: Entry to be added to tree
    val: value of that entry
    '''
    self.setOccurrences(self.rootOccurrences, val)
    self.setMain(self.mainDB, key, val)

  def setOccurrences(self, node, key):
    '''
    node: the node to compare
    key: Val of main db to be incremented in occurrences
    '''
    if node.key == None: #if it doesn't exist, set to 1
      node.key = key
      node.val = 1

    elif key == node.key: #if it already exists, increment by 1
      node.val += 1
    
    elif key > node.key: 
      if not node.right: 
        node.right = Node(parent=node, key=key, val=1) #create new node for entry
        return
      self.setOccurrences(node.right, key) #go to next node
    
    elif key < node.key:
      if not node.left:
        node.left = Node(parent=node,key=key, val=1) #create new node for entry
        return
      self.setOccurrences(node.left, key) #go to next node


  def setMain(self, node, key, val):
    '''
    node: the node to compare
    key: Entry to be added to tree
    val: value of that entry
    '''
    if node.key == None: 
      node.key = key
      node.val = val

    elif key == node.key: #update value 
      node.val = val
    
    elif key > node.key:
      if not node.right:
        node.right = Node(parent=node, key=key, val=val) #create new node for entry
        return
      self.setMain(node.right, key, val) #go to next node
    
    elif key < node.key:
      if not node.left:
        node.left = Node(parent=node,key=key, val=val) #create new node for entry
        return
      self.setMain(node.left, key, val) #go to next node


  def search(self, node, key):
    '''
    node: the node to compare
    key: Entry to find in the tree
    '''
    if node != None:
      if key == node.key:
        return node #node found
      elif key > node.key:
        return self.search(node.right, key) #compare next node
      elif key < node.key:
        return self.search(node.left, key) #compare next node
    else:
      return None #node not found

  def get(self, key):
    '''
    key: Entry to get from the tree
    '''
    node = self.search(self.mainDB, key)
    if node == None:
      return "NULL"
    else:
      return node.val

  def numequal(self, key):
    '''
    key: Entry to get from the tree
    '''
    node = self.search(self.rootOccurrences, key)
    if node == None:
      return 0
    else:
      return node.val
  
  def unset(self, key):
    '''
    key: Entry to remove from tree
    '''
    node = self.search(self.mainDB, key) #update mainDB
    if node != None:
      val = node.val #get value to update occurrences
      self.unsetMain(node)

    else:
      val = None
    self.updateParents(self.mainDB)
    
    node = self.search(self.rootOccurrences, val) #update occurrences
    if node != None:
      self.unsetOccurrences(node)

  def unsetOccurrences(self, node): 
    '''
    node: node in occurrences tree to decrement
    '''
    if node.val:
      node.val -= 1

  def unsetRoot(self, node):
    '''
    node: the root of the tree to be removed
    '''
    if node.left and node.right: #two children
      predecessor = node.right
      while predecessor.left:
        predecessor = predecessor.left
      self.unsetMain(predecessor)
      self.mainDB.key, self.mainDB.val = [predecessor.key, predecessor.val]

    elif node.left and not node.right: #only left child
      self.mainDB = node.left
    
    elif node.right and not node.left: #only right child
      self.mainDB = node.right
    
    elif not node.left and not node.right: #no children
      self.mainDB = Node()
  
  def unsetMain(self, node):
    '''
    node: node to remove from the tree
    '''
    if node == self.mainDB:
      self.unsetRoot(node)

    else:
      if node.left and node.right: #two children
        predecessor = node.right
        while predecessor.left:
          predecessor = predecessor.left #get node to replace it 
        node.key, node.val = [predecessor.key, predecessor.val]
        self.unsetMain(predecessor) #remove that node

      elif node.left and not node.right: #only left child
        if node.parent.left:
          if node.key == node.parent.left.key:
            node.parent.left = node.left
        if node.parent.right:
          if node.key == node.parent.right.key:
            node.parent.right = node.left
      
      elif node.right and not node.left: #only right child
        if node.parent.left:
          if node.key == node.parent.left.key:
            node.parent.left = node.right
        if node.parent.right:
          if node.key == node.parent.right.key:
            node.parent.right = node.right
      
      elif not node.left and not node.right: #no children
        if node == node.parent.left:
          node.parent.left = None
          node = None
        elif node == node.parent.right:
          node.parent.right = None
          node = None

  def updateParents(self, node):
    '''
    node: parent node to update children with
    '''
    if node != None:
      if node.left:
        node.left.parent = node #update left child
        self.updateParents(node.left)
      if node.right:
        node.right.parent = node #update right child
        self.updateParents(node.right)

  def printNodes(self, node):
    '''
    node: node to print
    '''
    if node != None:
      self.printNodes(node.right)
      self.printNodes(node.left)

  def parseInput(self, x):
    '''
    x: stdin
    '''
    if x[0] == 'SET':
      self.set(x[1], x[2])
    elif x[0] == 'UNSET':
      self.unset(x[1])
    elif x[0] == 'GET':
      print self.get(x[1])
    elif x[0] == 'NUMEQUALTO':
      print self.numequal(x[1])


if __name__ == '__main__':
  Timer(TreeDB())