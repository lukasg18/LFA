#!/usr/bin/env python
# -*- coding: utf-8 -*-

import conversorBib
import sys

def main():
	
	matriz = conversorBib.le_arquivo(sys.argv[2])
	conversorBib.separa_informacoes(matriz, sys.argv[4])
	# conversorBib.maquina(conversorBib.tokens(texto),sys.argv[4])
	
if __name__=="__main__":
	main()
