#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def calcular_diferenca():
	input_file  = open('input.txt','r')
	output_file = open('output.txt','r')

	len_in  = len(input_file.read())
	len_out = len(output_file.read())

	in_size = os.path.getsize('C:\Users\Lucas\workspace\compress-yo\input.txt')
	out_size = os.path.getsize('C:\Users\Lucas\workspace\compress-yo\output.txt')

	print("Input size: " + str(in_size) + " bytes")
	print("Output size: " + str(out_size) + " bytes\n")
	a = int(100 - (float(out_size) / float(in_size) * 100))
	print( "Compression rate: %d%s"%(a,"%"))

	# if(len_in > len_out):
	# 	print('Input e maior que output por ' + str(len_in - len_out) + ' caracteres')
	# else:
	# 	if(len_out > len_in):
	# 		print('Output e maior que input por ' + str(len_out - len_in) + ' caracteres')
	# 	else:
	# 		print('O tamanho e o mesmo')

	input_file.close()
	output_file.close()