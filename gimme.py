from sys import argv
import sys
import random
import os.path
import os

def load_items_from_file(filename = 'gimme.txt'):
  if (os.path.isfile(filename)):
    contents = open(filename)
    return contents.readlines()
  return [] 

def add_item(item, filename = 'gimme.txt'):
  if (item in items):
    return
  with open(filename, "a") as item_file:
    item_file.write(item + '\n')


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
  input = raw_input('\nWhat do you want to do? ')
  if input == 'g' or input == 'l':
      print 'Getting list...'
      
  if os.path.exists('gimme.txt'):
      filename = open('gimme.txt')
      print filename.read()
  else:
      print "No file"
  if input == 'n' or input == 'a':
    new_item = raw_input("\nWhat do you wana add? ")
    add_item(new_item)
    load_items_from_file()
  if input == 'd' or input == 'r':
    exit_or_not = raw_input("Are you sure you want to delete your file?(y/n): ")
    if exit_or_not =='y':
      os.remove('gimme.txt')
      print "deleted!"

  if input == '-i' or input == 'info':
    print """ g, l = get list \\ n, a = add  \n d, r = delete \\ y, n = yes/no
    """
    
print 'exiting...'

