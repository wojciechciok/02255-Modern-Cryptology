import numpy as np
from constants import S


class KeyScheduler:
    def __init__(self, key):
        self.keys = [key]
        self.rc = []

    def get_round_constant(self):
        i = len(self.rc) + 1
        if i == 1:
            rc = 1
        elif i > 1 and self.rc[i-2] < 0x80:
            rc = 2*self.rc[i-2]
        else:
            rc = (2*self.rc[i-2]) ^ 0x11B
        self.rc.append(rc)
        return rc

    def get_next_key(self):
        latest_key = self.keys[-1]
        key_length = len(latest_key)
        k_length = int(key_length/4)
        k0 = int(latest_key[0:k_length], 16)
        k1 = int(latest_key[k_length:k_length*2], 16)
        k2 = int(latest_key[k_length*2:k_length*3], 16)
        k3 = latest_key[k_length*3:k_length*4]
        k_part_length = int(len(k3) / 4)

        k3_parts = [k3[k_part_length:k_part_length*2],
                    k3[k_part_length*2:k_part_length*3], k3[k_part_length*3:k_part_length*4], k3[0:k_part_length]]
        for i, part in enumerate(k3_parts):
            k3_parts[i] = S[int(part, 16)]

        ri = self.get_round_constant()
        k3_parts[0] ^= ri
        k3_assembled = ''
        for part in k3_parts:
            k3_assembled += '{:02x}'.format(part)
        k3_assembled = int(k3_assembled, 16)
        k0 = k0 ^ k3_assembled
        k1 = k0 ^ k1
        k2 = k1 ^ k2
        k3 = int(k3, 16)
        k3 = k2 ^ k3

        new_key = '{:02x}'.format(
            k0) + '{:02x}'.format(k1) + '{:02x}'.format(k2) + '{:02x}'.format(k3)
        print(new_key)
        self.keys.append(new_key)
        new_key_mat = []
        for i in range(16):
            new_key_mat.append([int(new_key[i * 2:i * 2 + 2], 16)])
        new_key_mat = np.array(new_key_mat)
        new_key_mat = np.reshape(new_key_mat, (4, 4))
        return new_key_mat
