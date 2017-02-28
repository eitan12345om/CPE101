def max_101(num1, num2):
   if num1 > num2:
      return num1
   return num2

def max_of_three(num1, num2, num3):
   #biggest = max_101(num1, num2)
   #return max_101(biggest, num3)
   if num1 > num2 and num1 > num3:
      return num1
   elif num2 > num1 and num2 > num3:
      return num2
   else:
      return num3


def rental_late_fee(late_days):
   if late_days <= 0:
      fee = 0
   elif late_days <= 9:
      fee = 5
   elif late_days <= 15:
      fee = 7
   elif late_days <= 24:
      fee = 19
   else:
      fee = 100
   return fee

