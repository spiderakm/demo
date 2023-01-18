import random
import string
n = int(input())

upper = string.ascii_uppercase
num = string.digits

all = upper + num

tem = random.sample(all,n)

p = "".join(tem)
print(p)