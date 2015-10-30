from Timing import Timer

class HashDB(object):
  """
  A data base object
  Attributes: 
    mainDB: main hash table of names and values
    occurrences: hash table of values and number of occurrences in the database
  Methods:
    set: add a new value to the db and update number of occurrences
    get: return the value for the name of an entry
    unset: remove a value from the db and update number of occurrences
    numequal: return the number of occurrences for a given value
    parseInput: parses stdin to determine which method to call
  """

  def __init__(self):
    self.mainDB = {}
    self.occurrences = {}

  def set(self, key, value):
    '''
    key: Entry to be added to db
    val: value of that entry
    '''
    self.mainDB[key] = value
    if self.occurrences.has_key(value):
      self.occurrences[value] += 1
    else:
      self.occurrences[value] = 1

  def get(self, key):
    '''
    key: Entry to get from db
    '''
    try:
      return self.mainDB[key]
    except KeyError:
      return 'NULL'
  
  def unset(self, key):
    '''
    key: Entry to remove from db
    '''
    try:
      val = self.mainDB[key]
      del self.mainDB[key]
      self.occurrences[val] += -1
    except:
      pass

  def numequal(self, key):
    '''
    key: Entry to get from occurrences
    '''
    try:
      return self.occurrences[key]
    except KeyError:
      return 0

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
  Timer(HashDB())