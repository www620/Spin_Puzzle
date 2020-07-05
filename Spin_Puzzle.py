from random import randint as rd
import pygame as py
import os

big = 70
small = 7

class Blocks(object):
	def __init__(self, a):
		self.l = []
		self.a = a

		for i in range((self.a // 2) ** 2):
			self.l.append(0)
			self.l.append(1)
			self.l.append(2)
			self.l.append(3)
		
		self.l = rdlist(self.l)

	def swap(self, n):
		if n == -1:
			return

		m = n - self.a

		t = self.l[n]
		self.l[n] = self.l[n - 1]
		self.l[n - 1] = self.l[m - 1]
		self.l[m - 1] = self.l[m]
		self.l[m] = t

	def win(self):
		half = self.a // 2
		for i in range(self.a):
			for j in range(self.a):
				x = self.l[i * self.a + j]
				if j < half:
					if i < half:
						if x != 0:
							return False

					else:
						if x != 1:
							return False

				else:
					if i < half:
						if x != 2:
							return False

					else:
						if x != 3:
							return False

		return True

	def draw(self, screen):
		for i in range(self.a):
			for j in range(self.a):
				x = self.l[i * self.a + j]
				#0 -> 1 0 0
				#1 -> 1 1 0
				#2 -> 0 0 1
				#3 -> 0 1 0
				py.draw.rect(screen, [int(not (x // 2)) * 255, x % 2 * 255, (x == 2) * 255], 
					[i * big, j * big, big, big], 0)


class Buttons():
	def __init__(self, a):
		self.a = a - 1
		self.l = [0] * (self.a - 1) ** 2

	def check(self):
		for event in py.event.get():
			if event.type == py.QUIT:
				os._exit(0)

			if event.type == py.MOUSEBUTTONDOWN:
				mx, my = py.mouse.get_pos()
				for i in range(1, self.a + 1):
					for j in range(1, self.a + 1):
						if i * big - small < mx < i * big + small and j * big - small < my < j * big + small:
							return i * (self.a + 1) + j
		return -1


	def draw(self, screen):
		for i in range(1, self.a + 1):
			for j in range(1, self.a + 1):
				py.draw.circle(screen, [192, 192, 255], [i * big, j * big], small, 0)


def rdlist(list0):
	list0 = list(list0)
	n = len(list0)
	while n > 0:
		n -= 1
		m = rd(0, n)
		list0[n], list0[m] = list0[m], list0[n]
	return list0

def main():
	py.init()
	a = int(input("多大？"))
	screen = py.display.set_mode([a * big, a * big])
	py.display.set_caption("Spin Puzzle")

	blocks = Blocks(a)
	buttons = Buttons(a)
	while not blocks.win():
		screen.fill([0, 0, 0])
		blocks.swap(buttons.check())
		blocks.draw(screen)
		buttons.draw(screen)
		py.display.flip()
	

main()
