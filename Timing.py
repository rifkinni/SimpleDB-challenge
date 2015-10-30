from timeit import timeit
from random import randint


class Timer(object):
  '''
  A Timer object to measure database efficiency
  Attributes:
    alpha: alphabet letters
    db: the database
  Methods:
    populateDB: fills the database with 10,000 randomly generated entries
    timeAll: runs set, get, numequal, and unset 1000 times each and times them
    timeSet: run set with a random entry
    timeGet: run get with a random entry
    timeNumEqual: run numequal with a random entry
    timeUnset: run unset with a random entry
  '''

  def __init__(self, db):
    self.alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    self.db = self.populateDB(db)
    self.timeAll()

  def populateDB(self, db):
    for i in range(10000):
      x = self.alpha[randint(0, 25)] + self.alpha[randint(0, 25)] + self.alpha[randint(0, 25)]
      db.set(x, randint(0, 100))
    return db

  def timeAll(self):
    print "set:", timeit(self.timeSet, number=1000), "seconds"
    print "get:", timeit(self.timeGet, number=1000), "seconds"
    print "numequal:", timeit(self.timeNumEqual, number=1000), "seconds"
    print "unset:", timeit(self.timeUnset, number=1000), "seconds"

  def timeSet(self):
    self.db.set(self.alpha[randint(0, 25)], randint(0, 100))
  
  def timeGet(self):
    self.db.get(self.alpha[randint(0, 25)])
  
  def timeNumEqual(self):
    self.db.numequal(randint(0, 100))
  
  def timeUnset(self):
    self.db.unset(self.alpha[randint(0, 25)])