import numpy as np

from key_scheduler import KeyScheduler
from constants import S


class Aes:
    def __init__(self, key, rounds, verbose=False):
        self.verbose = verbose
        self.key = key
        self.rounds = rounds

    def encrypt(self, plaintext):
        self.key_scheduler = KeyScheduler(self.key)
        self.blocks = []
        for i in range(16):
            self.blocks.append([int(plaintext[i * 2:i * 2 + 2], 16)])

        self.blocks = np.array(self.blocks)
        self.blocks = np.reshape(self.blocks, (4, 4))
        self.blocks = self.blocks.T

        if self.verbose:
            print('plaintext:', plaintext)
            print('original key: ', self.key)

        key = self.key_scheduler.to_matrix(self.key)
        self.add_round_key(key)

        for i in range(self.rounds - 1):
            if self.verbose:
                print('-----------------')
                print('round: ', i+1)
            self.round()

        if self.verbose:
            print('-----------------')
            print("last round")
        self.round(last=True)
        return self.blocks

    def add_round_key(self, key):
        new_blocks = self.blocks
        for j in range(4):
            for i in range(4):
                new_blocks[i, j] ^= key[i, j]
        self.blocks = new_blocks
        if self.verbose:
            print("Adding round key")
            self.print_block()

    def round(self, last=False):
        self.sub_bytes()
        self.shift_rows()
        if not last:
            self.mix_columns()
        key = self.key_scheduler.get_next_key()
        if self.verbose:
            print("Round key: ")
            for row in key:
                print(self.to_hex(row[0]), self.to_hex(row[1]),
                      self.to_hex(row[2]), self.to_hex(row[3]))
        self.add_round_key(key)

    def shift_rows(self):
        new_blocks = self.blocks
        for i in range(4):
            new_blocks[i] = np.roll(new_blocks[i], -i)
        self.blocks = new_blocks
        if self.verbose:
            print("Shift rows")
            self.print_block()

    def sub_bytes(self):
        for i, row in enumerate(self.blocks):
            for j, cell in enumerate(row):
                self.blocks[i, j] = S[cell]

        if self.verbose:
            print("Sub bytes")
            self.print_block()

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
        if self.verbose:
            print("Mix columns")
            self.print_block()

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
