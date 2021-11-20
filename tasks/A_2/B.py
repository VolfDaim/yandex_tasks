import math

x_word = input()
z_word = input()

index = -1
len_x = len(x_word)
len_z = len(z_word)

if len_x < len_z:
    x_word = x_word * math.ceil(len_z / len_x)

len_x = len(x_word)
id = [i for i in range(len_x) if x_word[i] == z_word[0] and len_x - i <= len_z]

for i in id:
    if x_word[i:] == z_word[:len_x - i]:
        index = i
        break

if index != -1:
    if len_x - index == len_z:
        z_word = ''
    else:
        z_word = z_word[len_x - index:]

while z_word.startswith(x_word):
    z_word = z_word[len_x:]

print(z_word)
