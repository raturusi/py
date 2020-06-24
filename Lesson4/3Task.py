# в пределах от 20 до 240  -> 20...239
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 ==0])