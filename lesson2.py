import random

symbol="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
numbers = int(input('Какая длина пароля?'))
password = ""
for i in range(numbers):
    password += random.choice(symbol)

print(f'Ваш пароль {password}')