import copy
from HashDB import HashDB
from TreeDB import TreeDB, Node


class BlockHolder(object):
  '''
  A block object to handle commits and rollbacks
  Attributes:
    dbType: string selecting database algorithm
    dbList: a list of each database block
  Methods:
    run: listen for and parse input
    begin: begin new database block
    rollback: discard all changes since last commit
    commit: save all changes by merging into the first database block
    parseInput: parses stdin and determines what function to call
  '''
  def __init__(self, dbType):
    '''
    dbType: string 'hash' or 'tree'
    '''
    self.dbType = dbType
    if self.dbType == 'tree':
      db = TreeDB()
      self.dbList = [db]
    elif self.dbType == 'hash':
      db = HashDB()
      self.dbList = [db]


  def run(self):
    x = str(raw_input()).split()
    if not self.parseInput(x, self.dbList[-1]):
      return False
    return True

  def begin(self):
    if self.dbType == 'hash':
      newDB = HashDB()
      newDB.mainDB = copy.deepcopy(self.dbList[-1].mainDB)
      self.dbList.append(newDB)
    elif self.dbType == 'tree':
      newDB = TreeDB()
      newDB.mainDB = copy.deepcopy(self.dbList[-1].mainDB)
      self.dbList.append(newDB)

  def rollback(self):
    self.dbList = [self.dbList[0],]

  def commit(self):
    if self.dbList[0] == self.dbList[-1]:
      print "NO TRANSACTION"
    else:
      self.dbList = [self.dbList[-1],]

  def parseInput(self, x, block):
    '''
    x: stdin
    block: database block to update
    '''
    if x[0] == 'END':
      return False
    elif x[0] == 'ROLLBACK':
      self.rollback()
    elif x[0] == 'BEGIN':
      self.begin()
    elif x[0] == 'COMMIT':
      self.commit()
    else:
      block.parseInput(x)
    return True


if __name__ == '__main__':
  # db = TreeDB()
  # bh = BlockHolder('tree')
  # while bh.run():
  #   pass

  db = HashDB()
  bh = BlockHolder('hash')
  while bh.run():
    pass