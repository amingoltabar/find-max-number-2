maximum=0
for i in range(500):
    a=int(input('enter the positive integer'))
    while a<=0:
          a=int(input('enter the positive integer'))
    if a>maximum:
          maximum=a
print(maximum)
