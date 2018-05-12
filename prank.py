import mouse as m
import keyboard as k
import random

def p(str):
	print("click")

def main():
	for i in range(5):
		for i in range(50):
			m.move(random.randint(1, 1400),random.randint(1, 1200), absolute=True, duration=0.25)
		k.write("Prank")



if __name__ == '__main__':
	main()
