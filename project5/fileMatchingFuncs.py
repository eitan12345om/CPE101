# Project 5 - File Matching #
# Name: Eitan Simler
# Section: 17
# Instructor: Brian Jones

from operator import *

def main():
   f = 'oldMaster.dat'
   g = open('sorted_oldMaster.dat', 'w')
   
   entries = read_file(f)
   entries.sort(key = attrgetter('account_num'))
   
   write_file(g, entries)

   g.close()

   h = open('newMaster.dat', 'w')
   i = open('transaction.dat', 'r')

   transactions = [Transaction(*line.split()) for line in i if line.split()]
   for transaction in transactions:
      new_bal = add_transaction(transaction, entries)
      if new_bal:
         new_bal[1].balance = new_bal[0]
      else:
         print 'Unmatched transaction record for account %s' % transaction.account_num

   write_file(h, entries)

   i.close()
   h.close()

class Entry:
   def __init__(self, account_num, name, balance, phone, city):
      self.account_num = account_num
      self.name = name
      self.balance = float(balance)
      self.phone = phone
      self.city = city
   def __eq__(self, other):
      return self.account_num == other.account_num and self.name == other.name and self.balance == other.balance and self.phone == other.phone and self.city == other.city

class Transaction:
   def __init__(self, account_num, difference):
      self.account_num = account_num
      self.difference = float(difference)
   def __eq__(self, other):
      return self.account_num == other.account_num and self.difference == other.difference

def add_transaction(transaction, entries):
   for entry in entries:
      if transaction.account_num == entry.account_num:
         return (entry.balance + transaction.difference, entry)
   return None

def read_file(f):
   g = open(f, 'r')
  
   temp = [Entry(*[line.split()[0]] + [' '.join(line.split()[1:3])] + line.split()[3:]) for line in g if line.split()]
   g.close()
   return temp

def write_file(f, entries):
   for entry in entries:
      f.write('%s   %-11s   %-7.2f   %s   %-11s\n' % (entry.account_num, entry.name, entry.balance, entry.phone, entry.city))


if __name__ == '__main__':
   main()
