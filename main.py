def is_even():
  print("I will check if the numbers are even or not")
  input_value = int(input("Set value to check: >_ "))
  if input_value % 2 == 0:
    print("The number is even")
    input_value = True
  else:
    print("The number is odd")
    input_value = False
  return input_value


is_even()