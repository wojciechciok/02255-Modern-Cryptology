import numpy as np


class Aes:
    def __init__(self, s, key, plaintext, rounds):
        self.S = s
        self.plaintext = plaintext
        self.key = key
        self.rounds = rounds
        self.blocks = []
        for i in range(16):
            self.blocks.append([int(plaintext[i * 2:i * 2 + 2], 16)])
        self.blocks = np.array(self.blocks)
        self.blocks = np.reshape(self.blocks, (4, 4))

    def encrypt(self):
        self.add_key()
        for i in range(self.rounds - 1):
            self.round()
        self.round(last=True)

    def add_round_key(self, key):
        new_blocks = self.blocks
        for j in range(4):
            for i in range(4):
                new_blocks[i, j] ^= key[i, j]

        self.blocks = new_blocks

    def round(self, last=False):
        self.sub_bytes()
        self.shift_rows()
        if not last:
            self.mix_columns()
        self.add_key()

    def shift_rows(self):
        new_blocks = self.bolcks
        for i in range(4):
            new_blocks[i] = np.roll(new_blocks[i], -i)

        self.blocks = new_blocks

    def sub_bytes(self):
        for i, row in enumerate(self.blocks):
            for j, cell in enumerate(row):
                self.blocks[i, j] = self.S[cell]

    def mix_columns(self):
        self.blocks = self.blocks.T
        for i, row in enumerate(self.blocks):
            new_row = np.zeros(4)
            new_row[0] = self.gmul(row[0], 2) ^ self.gmul(
                row[1], 3) ^ self.gmul(row[2], 1) ^ self.gmul(row[3], 1)
            new_row[1] = self.gmul(row[0], 1) ^ self.gmul(
                row[1], 2) ^ self.gmul(row[2], 3) ^ self.gmul(row[3], 1)
            new_row[2] = self.gmul(row[0], 1) ^ self.gmul(
                row[1], 1) ^ self.gmul(row[2], 2) ^ self.gmul(row[3], 3)
            new_row[3] = self.gmul(row[0], 3) ^ self.gmul(
                row[1], 1) ^ self.gmul(row[2], 1) ^ self.gmul(row[3], 2)
            self.blocks[i] = new_row
        self.blocks = self.blocks.T

    def gmul(self, a, b):
        if b == 1:
            return a
        tmp = (a << 1) & 0xff
        if b == 2:
            return tmp if a < 128 else tmp ^ 0x1b
        if b == 3:
            return self.gmul(a, 2) ^ a

    def to_hex(self, val):
        return '{:02x}'.format(val)

    def print_block(self):
        for row in self.blocks:
            print(self.to_hex(row[0]), self.to_hex(row[1]),
                  self.to_hex(row[2]), self.to_hex(row[3]))
