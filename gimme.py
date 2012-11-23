from sys import argv
import sys
import random
import os.path


def load_items_from_file(filename = 'gimme.txt'):
  if (os.path.isfile(filename)):
    contents = open(filename)
    return contents.readlines()
  return []

def add_item(item, filename = 'gimme.txt'):
  if (item in items):
    return
  if(os.path.isfile(filename)):
    with open(filename, "a") as target:
      target.write(item + '\n')


done = []
items = load_items_from_file()

def get_items(count = 0):
  print "Getting %s items" % m
  i = 0
  while (len(items) != len(done)) and (i < count):
    item = random.choice(items)
    if (item not in done):
      i = i + 1
      done.append(item)
      print "Item %d: %s" % (i, item),

input = ''

try:
  filename, count = argv
  m = int(float(count))
  get_items(m)
  sys.exit(0)
except ValueError:
  print 'Did not ask for items, continuing...'


while input != 'q' and input != 'x':
  input = raw_input('what you wanna do? ')
  if input == 'g' or input == 'l':
    print 'getting items'
  if input == 'n' or input == 'a':
    new_item = raw_input("What do you wana add? ")
    add_item(new_item)
    load_items_from_file()

print 'exiting...'

#items = load_items_from_file()
#item1 = raw_input("Task/Item: ")
#item2 = raw_input("Task/Item: ")
#print items
