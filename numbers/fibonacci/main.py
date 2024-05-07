def main(x):
  if x <= 1:
    return x
  else:
    return main(x-1) + main(x-2)

n = int(input("Enter a # thing: "))

if n <= 0:
  print("Positive integer bro")
elif n >= 30:
  print("Too big (that's what she said)")
else:
  print("Fibonacci sequence:\n")
  for i in range(n):
    print(main((i)))
