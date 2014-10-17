def calcular_diferenca():
	input_file  = open('input.txt','r')
	output_file = open('output.txt','r')

	len_in  = len(input_file.read())
	len_out = len(output_file.read())

	if(len_in > len_out):
		print('Input e maior que output por ' + str(len_in - len_out) + ' caracteres')
	else:
		if(len_out > len_in):
			print('Output e maior que input por ' + str(len_out - len_in) + ' caracteres')
		else:
			print('O tamanho e o mesmo')

	input_file.close()
	output_file.close()

calcular_diferenca()