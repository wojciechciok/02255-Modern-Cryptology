from AES import Aes
from constants import S, SI
import numpy as np


class SquareAttack():

    def __init__(self, aes) -> None:
        self.aes = aes
        self.rc = []
        self._set_round_constants(4)

    def get_labmda_set(self, inactive_value):
        lambda_set = []
        inactive_values = inactive_value * 15
        for i in range(256):
            plain_text = '{:02x}'.format(i) + inactive_values
            lambda_set.append(plain_text)
        return lambda_set

    def to_hex(self, val):
        return '{:02x}'.format(val)

    def print_block(self, block):
        for row in block:
            print(self.to_hex(int(row[0])), self.to_hex(int(row[1])),
                  self.to_hex(int(row[2])), self.to_hex(int(row[3])))

    def attack(self):

        # decrypted_key = ""
        # for y in range(4):
        #     for x in range(4):
        #         decrypted_key_byte = self.guess_correct_key_byte_for_position(
        #             x, y)
        #         print(self.to_hex(decrypted_key_byte))
        #         decrypted_key += self.to_hex(decrypted_key_byte)

        # for i in range(4, 0, -1):
        #     decrypted_key = self.get_previous_round_key(decrypted_key, i)
        # print(decrypted_key)
        decrypted_key = "47f7f7bc95353e03f96c32bcfd058dfd"
        # for y in range(4):
        #     for x in range(4):
        #         decrypted_key_byte = self.guess_correct_key_byte_for_position(
        #             x, y)
        #         print(self.to_hex(decrypted_key_byte))
        #         decrypted_key += self.to_hex(decrypted_key_byte)

        for i in range(4, 0, -1):
            decrypted_key = self.get_previous_round_key(decrypted_key, i)
            print(decrypted_key)
        # print(decrypted_key)

    def guess_correct_key_byte_for_position(self, x, y):
        guessed = False
        i = 0

        guessed_parts = []
        while not guessed:
            lambda_set = self.get_labmda_set(self.to_hex(i))
            encrypted_lambda_set = []

            for plain_text in lambda_set:
                encrypted_lambda_set.append(self.aes.encrypt(plain_text))

            guessed_key_parts = self.get_all_possible_correct_guesses(
                encrypted_lambda_set, x, y)

            if len(guessed_parts) < 1:
                guessed_parts = guessed_key_parts
            else:
                guessed_parts = set(guessed_parts).intersection(
                    set(guessed_key_parts))

            if len(guessed_parts) == 1:
                break
            i += 1
        return list(guessed_parts)[0]

    def get_all_possible_correct_guesses(self, encrypted_lambda_set, x, y):
        guessed_values = []
        for i in range(256):
            if self.is_key_part_guess_correct(encrypted_lambda_set, x, y, i):
                guessed_values.append(i)
        return guessed_values

    def is_key_part_guess_correct(self, encrypted_lambda_set, x, y, guessed_byte):
        reversed_bytes = []
        for encrypted_matrix in encrypted_lambda_set:
            reversed_byte = self.reverse_last_round(
                encrypted_matrix, guessed_byte, x, y)
            reversed_bytes.append(reversed_byte)
        return self.is_guess_correct(reversed_bytes)

    def is_guess_correct(self, reversed_bytes):
        result = 0
        for i in reversed_bytes:
            result ^= i
        return result == 0

    def reverse_last_round(self, encrypted_matrix, guessed_byte, x, y):
        encrypted_byte = encrypted_matrix[x, y]
        encrypted_byte ^= guessed_byte
        encrypted_byte = SI[encrypted_byte]
        return encrypted_byte

    def get_alterd_last_key_part(self, k3, round):
        k_part_length = int(len(k3) / 4)

        k3_parts = [k3[k_part_length:k_part_length*2],
                    k3[k_part_length*2:k_part_length*3], k3[k_part_length*3:k_part_length*4], k3[0:k_part_length]]
        for i, part in enumerate(k3_parts):
            k3_parts[i] = S[int(part, 16)]

        ri = self.rc[round-1]
        k3_parts[0] ^= ri
        k3_assembled = ''
        for part in k3_parts:
            k3_assembled += '{:02x}'.format(part)
        k3_assembled = int(k3_assembled, 16)

        return k3_assembled

    def _set_round_constants(self, rounds):
        for _ in range(rounds):
            i = len(self.rc) + 1
            if i == 1:
                rc = 1
            elif i > 1 and self.rc[i-2] < 0x80:
                rc = 2*self.rc[i-2]
            else:
                rc = (2*self.rc[i-2]) ^ 0x11B
            self.rc.append(rc)

    def get_previous_round_key(self, round_key, round):
        key_length = len(round_key)
        k_length = int(key_length/4)
        k0 = int(round_key[0:k_length], 16)
        k1 = int(round_key[k_length:k_length*2], 16)
        k2 = int(round_key[k_length*2:k_length*3], 16)
        k3 = int(round_key[k_length*3:k_length*4], 16)

        prev_k3 = k3 ^ k2
        prev_k2 = k2 ^ k1
        prev_k1 = k1 ^ k0
        altered_k3 = self.get_alterd_last_key_part(
            '{:08x}'.format(prev_k3), round)
        prev_k0 = k0 ^ altered_k3
        return '{:08x}'.format(prev_k0) + '{:08x}'.format(prev_k1) + '{:08x}'.format(prev_k2) + '{:08x}'.format(prev_k3)


aes = Aes('000102030405060708090a0b0c0d0e0f', 4)
sa = SquareAttack(aes)
sa.attack()
