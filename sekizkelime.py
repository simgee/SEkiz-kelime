# -*- coding: utf-8 -*-
import random 
import numpy as np
n=12
global Matrix
Matrix = np.empty([n, n], dtype = str)
alfabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']
for i in range(n):
	for j in range(n):
		Matrix[i][j]=random.choice(alfabe)

global usedpositions
usedpositions = []
global kelimepositions
kelimepositions = []

###################################KELIME YERLESTIRME FONKSIYONUM##########################################################

def kelimeyerlestir(kelime):
	global Matrix
	a = len(kelime)
	yerlestirme=random.randint(5,6)
	if yerlestirme<4:
		b=11-a
		if yerlestirme == 1:
			p1=random.randint(0, 11)
			p2=random.randint(0, b)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p2 += 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
						mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1,p2-1]
		if yerlestirme == 2:
			p1=random.randint(0, b)
			p2=random.randint(0, 11)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p1 += 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
						mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1-1,p2]
		if yerlestirme == 3:
			p1=random.randint(0, b)
			p2=random.randint(0, b)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p1 += 1
					p2 += 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
						mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1-1,p2-1]
	else:
		b=len(kelime)
		if yerlestirme == 4:
			p1=random.randint(0, 11)
			p2=random.randint(b, 11)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p2 -= 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
						mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1,p2+1]
		if yerlestirme == 5:
			p1=random.randint(b, 11)
			p2=random.randint(0, 11)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p1 -= 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
						mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1+1,p2]		
		if yerlestirme == 6:
			p1=random.randint(b, 11)
			p2=random.randint(b, 11)
			posilk=[p1,p2]
			kelimepositions = []
			Matrix2=Matrix.copy()
			for index,harf in enumerate(kelime):
				if [p1,p2] not in usedpositions:
					Matrix2[p1][p2]=harf
					usedpositions.append([p1,p2])
					kelimepositions.append([p1,p2])
					p1 -= 1
					p2 -= 1
					if index == len(kelime)-1:
						Matrix=Matrix2.copy()
	 					mydict[kelime]=kelimepositions
				else:
					for el in kelimepositions:
						usedpositions.remove(el)
					kelimeyerlestir(kelime)
					break
			posson=[p1+1,p2+1]

###################################PRINT FONKSIYONUM##########################################################

def printing():
	column=0
	row=0
	myfirstline = "    "
	for i in range(n):
		if len(str(row))==1:
			myfirstline +="0" + str(row) + " |"
		else:
			myfirstline += str(row) + " |"
		row = row + 1
	print(myfirstline)

	for item in Matrix:
		if len(str(column))==1:
			mystr="0" + str(column) + " | "
		else:
			mystr=str(column) + " | "
		for i in item:
			for j in i:
				mystr = mystr + j+ " | " 
				if len(mystr) == n*4+5:
					print("-----------------------------------------------------")
					print(mystr)
		column +=1


###################################PRINT 2 FONKSIYONUM#########################################################

def printing2():
	column=0
	row=0
	myfirstline = "  "
	for i in range(n):
		if len(str(row))==1:
			myfirstline +="0" + str(row) + " "
		else:
			myfirstline += str(row) + " "
		row = row + 1
	print(myfirstline)

	for item in Matrix:
		if len(str(column))==1:
			mystr="0" + str(column) + " "
		else:
			mystr=str(column) + " "
		for i in item:
			for j in i:
				mystr = mystr + j+ "  " 
				if len(mystr) == n*3+3:
					print(mystr)
		column +=1

###################################CONTROL FONKSIYONUM#########################################################

def control(tahmin):
	while(tahmin.upper()!="EXIT"):
		if(tahmin.upper() in mydict):
			print (tahmin.upper()+" sözlüktedir")	
			position1 = raw_input("Lütfen buldugunuz kelimenin ilk pozisyonunu giriniz:")
			position2 = raw_input("Lütfen buldugunuz kelimenin son pozisyonunu giriniz:")
			positionilk = position1.split(",")
			positionson = position2.split(",")
			if(int(positionilk[0])==mydict[tahmin.upper()][0][0] and int(positionilk[1])==mydict[tahmin.upper()][0][1] and int(positionson[0])==mydict[tahmin.upper()][-1][0] and int(positionson[1]) == mydict[tahmin.upper()][-1][1]):
				print("Doğru Bildiniz :)")
				print(mydict[tahmin.upper()])
				bilinen.add(tahmin)
				#print bilinen
				if(klm_number + 1==len(bilinen)):
					print("Kazandınız!! Kelimelerin hepsini bildiniz.")
					break
			else:
				print("Yanlış")
		else:
			print("Girdiğiniz kelime oyun kapsamında aranan bir kelime değildir")
		tahmin = raw_input("Lütfen buldugunuz kelimeyi giriniz:").strip()



global mydict
mydict = {}
kelime_dosyasi = open("kelime.txt","r")
for klm_number,i in enumerate(kelime_dosyasi):
	mydict[i.strip()]=[]
	kelimeyerlestir(i.strip())
	print(i.strip(),mydict[i.strip()])

printing2()

bilinen=set()
	
tahmin = raw_input("Lütfen buldugunuz kelimeyi giriniz:").strip()
control(tahmin)



