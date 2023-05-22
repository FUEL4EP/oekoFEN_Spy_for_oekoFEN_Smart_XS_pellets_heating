#/usr/bin/env python3

import socket
import collections
from time import sleep
import datetime
import os
import gc

max_stack_size = 40
period_time = 5
first_run = True
gc.collect()

#https://stackoverflow.com/questions/48024167/creating-a-list-of-stacks-in-python
#https://www.pythoncentral.io/stack-tutorial-python-implementation/
#https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/


class Stack: #LIFO type
    def __init__(self):
        self.items =  []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        #Checking to avoid duplicate entries
        if item not in self.items:
          if self.size() >= max_stack_size:
            self.pop()
          #Adding elements to stack
          print( "Stack : Adding %s" % item )
          self.items.append(item)
          return True
        else:
          #print( "Stack : Omitting duplicate %s" % item )
          return False

    def pop(self):
        removed_item = self.items.pop(0)
        print( "Stack : Removing %s" % removed_item )
        return removed_item 

    def size(self):
        return len(self.items)

    def printStack(self):
        for item in reversed(self.items):
            print (item)

    def listStack(self):
        return self.items

myStack = Stack()

number_of_urls = 0
url_ip_stack_list = []
i=0
url_list=[]
with open("allowed_urls.txt","r") as urls:
  for line in urls:
    number_of_urls = number_of_urls + 1
    url_list.append(line.strip())
    url_ip_stack_list.append(Stack()) 

print ( url_list )

#loop with delay
while True:
  #tstart = datetime.datetime.now()
  #print( "\n\n\nIteration %d\n" % i)
  k=0
  update_flag = False
  for j in url_list:

    try:
      ip_addrs = socket.gethostbyname_ex(j)[2]
      #print ( j, ip_addrs )
      for ip in ip_addrs:
        #print (j,ip)
        add_flag = url_ip_stack_list[k].push(ip)
        update_flag = update_flag or add_flag
        #print ( "Stack %d has size %d\n" % (k, url_ip_stack_list[k].size()) )
    except (socket.error, socket.gaierror) as err:
      #print ("cannot resolve hostname %s : %s" % (j, err)) #!!!!!!!!!!!!! err
      gc.collect()
      sleep(120)
    k=k+1
  i=i+1
  if update_flag:
    #print ( "\n\n===================================> update\n\n")

    #File in write mode
    WriteBshFile = open("create_and_update_myip_whitelist_forward_queue.bsh",
 "w")
    WriteBshFile.write ("#!/bin/bash -f\n")
    WriteBshFile.write("#Created on %s\n" % datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") )
    #print ( first_run )
    if first_run:
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -F\n")
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -X\n")
      #WriteBshFile.write ("#list current ipset\n")
      #WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -L\n")
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset create -exist my_whitelist hash:ip\n")
    else:
      #WriteBshFile.write ("#list current ipset\n")
      #WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -L\n")
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset create -exist my_whitelist.new hash:ip\n")

    l=0
    for j in url_list:
      WriteBshFile.write ("#allowed URL %s\n" % j)
      for m in url_ip_stack_list[l].listStack():
        if first_run:
          WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -exist add my_whitelist %s\n" % m)
        else:
          WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -exist add my_whitelist.new %s\n" % m)
      l=l+1

    if not first_run:   
      #WriteBshFile.write ("#list current ipset\n")
      #WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -L\n")
      WriteBshFile.write ("#Swap the old and new sets\n")
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -W  my_whitelist.new my_whitelist\n")
      WriteBshFile.write ("#Get rid of the old set, which is now under new-set\n")
      WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -X my_whitelist.new\n")
    #WriteBshFile.write ("#list current ipset\n")
    #WriteBshFile.write ("/usr/bin/sudo /sbin/ipset -L\n")
    WriteBshFile.close()

    os.system("/bin/bash create_and_update_myip_whitelist_forward_queue.bsh")
    first_run = False

  #tend = datetime.datetime.now()
  #print ( (tend - tstart).microseconds )
  sleep(period_time)
k=0
for j in url_list:
  #print ( "Stack %d for '%s' has size %d\n" % (k, url_list[k], url_ip_stack_list[k].size()) )
  k=k+1

            


