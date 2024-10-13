def printLabel(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  
  print('\n' + '-'*30)
  
  for key, value in kwargs.items():
    print(f'{key} : {value}')


printLabel("rehan", "shakil", "shaikh", state='maharashtra', city='mumbai', pin='400060')