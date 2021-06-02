print("Bạn chọn Búa,Kéo hay Bao")

p = input()
from random import randint
c = randint(0,2)
if c == 0:
	c = "Kéo"
if c == 1:
	c ="Búa"
if c == 2:
	c = "Bao"
print("________________")
print("Bạn chọn " + p)
print("Máy tính chọn " + c)
print("________________")
if p == c:
	print("Hòa")
else:
	if p  == "Búa":
		if c  == "Bao":
			print("Máy tính thắng")
		else:
			print("Máy tính thua")
	elif  p  == "Kéo":
		if c  == "Búa":
			print("Máy tính thắng")
		else:
			print("Máy tính thua")
	elif  p  == "Bao":
		 if c  == "Kéo":		
		 	print("Máy tính thắng")
		 else:
		 	print("Máy tính thua")
	else:
		print("xin vui lòng nhập lại")
	









