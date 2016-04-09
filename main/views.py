from django.shortcuts import render
# -*- coding: utf-8 -*-
import random 
import numpy as np
from django.views.generic import View

# Create your views here.

def matrixolustur():
	n=12
	global Matrix
	Matrix = np.empty([n, n], dtype = str)
	alfabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']
	for i in range(n):
		for j in range(n):
			Matrix[i][j]=random.choice(alfabe)
	usedpositions = []
	kelimepositions = []	
	return Matrix,usedpositions,kelimepositions

###################################PRINT 2 FONKSIYONUM#########################################################

def printing2(Matrix,n=12):
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
	

###################################KELIME YERLESTIRME FONKSIYONUM##########################################################

def kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict):
	global Matrix
	a = len(kelime)
	yerlestirme=random.randint(1,6)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
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
					kelimeyerlestir(kelime,usedpositions,kelimepositions,mydict)
					break
			posson=[p1+1,p2+1]
	return usedpositions,kelimepositions,mydict


class Home(View):
	def get(self, request):
		n=12
		global Matrix	
		global correctwords
		correctwords = set()	
		Matrix = np.empty([n, n], dtype =  object)
		alfabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Y','Z']
		for i in range(n):
			for j in range(n):
				Matrix[i][j]=random.choice(alfabe)
		
		usedpositions = []
		kelimepositions = []
		global mydict
		global wordlist
		mydict = {}
		wordlist = []
		kelime_dosyasi = open("kelime.txt","r")
		for klm_number,i in enumerate(kelime_dosyasi):
			mydict[i.strip()]=[]
			usedpositions,kelimepositions,mydict = kelimeyerlestir(i.strip(),usedpositions,kelimepositions,mydict)
			print(i.strip(),mydict[i.strip()])
			wordlist.append(i.strip())
		global nliste
		nliste=[]
		for i in range(n):
			nliste.append(i)
		
		matrixzip=[{'n': t[0], 'item': t[1]} for t in zip(nliste,Matrix)]
		return render(request, 'base.html', {
			'wordlist': wordlist,
			'matrixzip':matrixzip,
			'nliste':nliste,
		})
	
	def post(self, request):
		if "control" in request.POST:
			word = request.POST['word'].strip()
			firstpos1 = request.POST['firstpos1'].strip()
			firstpos2 = request.POST['firstpos2'].strip()
			lastpos1 = request.POST['lastpos1'].strip()
			lastpos2 = request.POST['lastpos2'].strip()
			word = word.upper()
			global Matrix3
			Matrix3 = Matrix.copy()
			condition = "yanlis"
			if(word in mydict):
				if(int(firstpos1)==mydict[word][0][0] and int(firstpos2)==mydict[word][0][1] and int(lastpos1)==mydict[word][-1][0] and int(lastpos2) == mydict[word][-1][1]):
					correctwords.add(word)
					condition = 'Dogru Bildiniz :)'
				if(len(mydict) ==len(correctwords)):
						condition = 'KAZANDINIZ'

			else:
				condition = 'Oyun kapsaminda aranan<br>bir kelime degildir'

			for word in correctwords:
				poslist = mydict[word]
				for pos in poslist:
					i = pos[0]
					j = pos[1]
					hede = Matrix3[i][j]
					Matrix3[i][j]='<div id="correctw">' +hede +'</div>'

			matrixzip=[{'n': t[0], 'item': t[1]} for t in zip(nliste,Matrix3)]
			return render(request, 'puzzle.html', {
				'wordlist':wordlist,
				'correctwords':correctwords,
				'condition':condition,
				'word':word,
				'matrixzip':matrixzip,
				'nliste':nliste,
			})

class About(View):
	def get(self, request):
		return render(request, 'about.html', {
		})

class Game(View):
	def get(self, request):
		return render(request, 'game.html', {
		})

