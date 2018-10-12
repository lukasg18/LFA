#!/usr/bin/env python
# -*- coding: utf-8 -*-

import conversorBib
import sys

def main():
	
	texto = conversorBib.leArquivo(sys.argv[2])
	# conversorBib.maquina(conversorBib.tokens(texto),sys.argv[4])
	
if __name__=="__main__":
	main()
