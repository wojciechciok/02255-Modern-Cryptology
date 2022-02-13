from AES import Aes
from key_scheduler import KeyScheduler


aes = Aes('000102030405060708090a0b0c0d0e0f', 4, verbose=True)
aes.encrypt('ff000000000000000000000000000000')


"""
plaintext: ff000000000000000000000000000000
original key:  000102030405060708090a0b0c0d0e0f
Adding round key
ff 04 08 0c
01 05 09 0d
02 06 0a 0e
03 07 0b 0f
-----------------
round:  1
Sub bytes
16 f2 30 fe
7c 6b 01 d7
77 6f 67 ab
7b c5 2b 76
Shift rows
16 f2 30 fe
6b 01 d7 7c
67 ab 77 6f
76 7b c5 2b
Mix columns
80 2c b0 27
1f 6d d9 9c
29 33 5d 21
da 51 61 5c
Round key:
d6 d2 da d6
aa af a6 ab
74 72 78 76
fd fa f1 fe
Adding round key
56 fe 6a f1
b5 c2 7f 37
5d 41 25 57
27 ab 90 a2
-----------------
round:  2
Sub bytes
b1 bb 02 a1
d5 25 d2 9a
4c 83 3f 5b
cc 62 60 3a
Shift rows
b1 bb 02 a1
25 d2 9a d5
3f 5b 4c 83
3a cc 62 60
Mix columns
13 97 9f de
80 25 9b ee
a4 90 a6 c9
a6 dc 14 6e
Round key:
b6 64 be 68
92 3d 9b 30
cf bd c5 b3
0b f1 00 fe
Adding round key
a5 f3 21 b6
12 18 00 de
6b 2d 63 7a
ad 2d 14 90
-----------------
round:  3
Sub bytes
06 0d fd 4e
c9 ad 63 1d
7f d8 fb da
95 d8 fa 60
Shift rows
06 0d fd 4e
ad 63 1d c9
fb da 7f d8
60 95 d8 fa
Mix columns
7b f0 61 fe
31 2b 9e 4e
e6 65 6d 39
9c 9f d5 2c
Round key:
b6 d2 6c 04
ff c2 59 69
74 c9 0c bf
4e bf bf 41
Adding round key
cd 22 0d fa
ce e9 c7 27
92 ac 61 86
d2 20 6a 6d
-----------------
last round
Sub bytes
bd 93 d7 2d
8b 1e c6 cc
4f 91 ef 44
b5 b7 02 3c
Shift rows
bd 93 d7 2d
1e c6 cc 8b
ef 44 4f 91
3c b5 b7 02
Round key:
47 95 f9 fd
f7 35 6c 05
f7 3e 32 8d
bc 03 bc fd
Adding round key
fa 06 2e d0
e9 f3 a0 8e
18 7a 7d 1c
80 b6 0b ff

"""
