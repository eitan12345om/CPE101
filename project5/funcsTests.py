# Project 5 - File Matching #
# Name: Eitan Simler
# Section: 17
# Instructor: Brian Jones

import unittest
from fileMatchingFuncs import *

class TestCases(unittest.TestCase):
          
   def test_entry_init(self):
      entry = Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO')
      self.assertEqual(entry.account_num, '345')
      self.assertEqual(entry.name, 'Bob Jones')
      self.assertAlmostEqual(entry.balance, 87.12)
      self.assertEqual(entry.phone, '8055551234')
      self.assertEqual(entry.city, 'SLO')   

   def test_read_file_0(self):
      entries = []
      entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
      entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
      # call read_file with 'test0.dat'
      self.assertEqual(read_file('test0.dat'), entries)

   def test_read_file_1(self):
      entries = []
      entries.append(Entry('100', 'Alan Jones', 348.17, '8053564820', 'SLO'))
      entries.append(Entry('700', 'Suzy Green', -14.22, '8052586912', 'SLO'))
      entries.append(Entry('300', 'Mary Smith', 27.19, '8057901237', 'Santa_Maria'))
      entries.append(Entry('800', 'Mike Rosen', -104.58, '8051200891','Pismo_Beach'))
      # call read_file with 'test1.dat'
      self.assertEqual(read_file('test1.dat'), entries)

   def test_transaction_init1(self):
      transaction = Transaction('345', 20.23)
      self.assertEqual(transaction.account_num, '345')
      self.assertEqual(transaction.difference, 20.23)
   def test_transaction_init2(self):
      transaction = Transaction('120', -20.23)
      self.assertEqual(transaction.account_num, '120')
      self.assertEqual(transaction.difference, -20.23)
     
   def test_add_transaction1(self):
      entries = [Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO'), Entry('120', 'Sarah Smith', 50.00, '8056551234', 'SLO')]
      transaction = Transaction('345', 20.23)
      self.assertAlmostEqual(add_transaction(transaction, entries)[0], 107.35)
      self.assertEqual(add_transaction(transaction, entries)[1], entries[0])
   def test_add_transaction2(self):
      entries = [Entry('345', 'Bob Jones', 87.12, '8055551234', 'SLO'), Entry('120', 'Sarah Smith', 50.00, '8056551234', 'SLO')]
      transaction = Transaction('125', 20.23)
      self.assertEqual(add_transaction(transaction, entries), None)


      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

