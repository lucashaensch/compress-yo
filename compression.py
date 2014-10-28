#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper
lenght_string = 0

def encode_rle(): # Encoda string inputada
	lst = []
	prev = ''
	count = 1
	output_string = ''
	output_file = open('output.txt','w')

	# Get input string 
	input_file = open('input.txt','r')
	input_string = input_file.read()
	input_file.close()

	for character in input_string:
		if character != prev:
			if prev:
				entry = (prev,count)
				lst.append(entry)
			count = 1
			prev = character
		else:
			count += 1
	else:
		entry = (character,count)
		lst.append(entry) 

	# Transforma os grupos na string comprimida
	for group in lst:
		output_string += str(group[1]) + group[0] + '.'

	# Verifica se vale a pena comprimir e retorna o melhor resultado
	if(len(output_string) > len(input_string)):
		output_file.write(input_string)
		output_file.close()
		helper.calcular_diferenca()
		return output_string
	else:
		output_file.write(output_string)
		output_file.close()
		helper.calcular_diferenca()
		return output_string

def decode_rle(input_string): # Decoda string encodada com RLE
	output_string = ''
	pieces = input_string.split(".")
	if len(pieces) > 1:
		for piece in pieces:
			if(piece != '' and piece != None):
				output_string += str(int(piece[:-1]) * piece[-1])

	return output_string

### Test-drive ###
encoded_string = encode_rle()

print('\nencoded_string: ' + encoded_string)
print('decoded_string: ' + decode_rle(encoded_string))
