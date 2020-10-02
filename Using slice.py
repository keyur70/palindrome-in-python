myStr = input("Enter the string: ")
if str(myStr) == str(myStr)[::-1] #checking using slicing opearator
  print("Palindrome")
else:
  print("Not a Palindrome")
