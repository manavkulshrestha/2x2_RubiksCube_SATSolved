import numpy as np


#states[STICKER,POSITION]
class Cube:
	def __init__(self):
		states = np.full((8,24),False,dtype=bool)

		solved = states.copy()
		for i in range(1,24):
			states[i,i] = True

	# def cycle_edges(self, critical_sticker, clockwise=True):
		# if !states[critical_sticker,critical_sticker]:
		# 	return False

		# clockwise = 3 if clockwise else -3

		# for i in range(-1,2):
		# 	states[critical_sticker+i,critical_sticker+i]

	#PRIVATE
	def find_critial_sticker(cubee_pos):
		'''Returns a tuple containing the critical sticker and its position in the cubee, respectively'''
		for position in range(cubee_pos-1,cubee_pos+2):
			for cs_candidate in range(8):
				if states[cs_candidate,position]:
					return (cs_candidate,position)

	#PRIVATE
	def critical_and_adjacent(self, cubee_pos1, cubee_pos2):
		'''Guard ensuring cubee is represented by critical position and the two cubees are adjacent'''
		critical_pos = (cubee_pos1-1)%3 == 0 and (cubee_pos2-1)%3 == 0
		adjacent = abs(cubee_pos1-cubee_pos2) == 3 or (cubee_pos1,cubee_pos2) not in [(1,10),(13,22),(1,22),(4,19),(10,19),(7,16)]

		return critical and adjacent

	def t_perm(self, cubee_pos1, cubee_pos2):
		'''Performs a T-Perm movement on two cubees that are adjacent'''
		if not critical_and_adjacent(cubee_pos1, cubee_pos2):
			return False

		critical_sticker1 = find_critial_sticker(cubee_pos1)
		critical_sticker2 = find_critial_sticker(cubee_pos1)

		states[critical_sticker1] = False
		states[critical_sticker2] = False

		#...

		return True

	def reorient(self, cubee_pos1, cubee_pos2, direction):
		'''Reorients the two cubee positions inwards or outwards depending on the directions'''
		if not critical_and_adjacent(cubee_pos1, cubee_pos2):
			return False

		critical_sticker1 = find_critial_sticker(cubee_pos1)
		critical_sticker2 = find_critial_sticker(cubee_pos1)

		states[critical_sticker1] = False
		states[critical_sticker2] = False

		orient = 1 if direction else -1

		#(csticker, position)
		new_critical_sticker1 = (critical_sticker1[0],cubee_pos1-1+(critical_sticker1[1]+orient)%3)
		new_critical_sticker2 = (critical_sticker2[0],cubee_pos1-1+(critical_sticker1[1]+orient)%3)

		states[new_critical_sticker1] = True
		states[new_critical_sticker2] = True

		return True