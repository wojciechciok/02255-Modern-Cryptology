Word = bytes


def xor(w1: Word, w2: Word) -> Word:
    return bytes([i ^ j for i, j in zip(w1, w2)])


KEY_SCHEDULER_LOOKUP_TABLE = [
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
    0x01,
    0x02,
    0x04,
    0x08,
    0x10,
    0x20,
    0x40,
    0x80,
    0x1B,
    0x36,
    0x6C,
    0xD8,
    0xAB,
    0x4D,
    0x9A,
    0x2F,
    0x5E,
    0xBC,
    0x63,
    0xC6,
    0x97,
    0x35,
    0x6A,
    0xD4,
    0xB3,
    0x7D,
    0xFA,
    0xEF,
    0xC5,
    0x91,
    0x39,
    0x72,
    0xE4,
    0xD3,
    0xBD,
    0x61,
    0xC2,
    0x9F,
    0x25,
    0x4A,
    0x94,
    0x33,
    0x66,
    0xCC,
    0x83,
    0x1D,
    0x3A,
    0x74,
    0xE8,
    0xCB,
    0x8D,
]


S_BOX = {
    0: 99,
    1: 124,
    2: 119,
    3: 123,
    4: 242,
    5: 107,
    6: 111,
    7: 197,
    8: 48,
    9: 1,
    10: 103,
    11: 43,
    12: 254,
    13: 215,
    14: 171,
    15: 118,
    16: 202,
    17: 130,
    18: 201,
    19: 125,
    20: 250,
    21: 89,
    22: 71,
    23: 240,
    24: 173,
    25: 212,
    26: 162,
    27: 175,
    28: 156,
    29: 164,
    30: 114,
    31: 192,
    32: 183,
    33: 253,
    34: 147,
    35: 38,
    36: 54,
    37: 63,
    38: 247,
    39: 204,
    40: 52,
    41: 165,
    42: 229,
    43: 241,
    44: 113,
    45: 216,
    46: 49,
    47: 21,
    48: 4,
    49: 199,
    50: 35,
    51: 195,
    52: 24,
    53: 150,
    54: 5,
    55: 154,
    56: 7,
    57: 18,
    58: 128,
    59: 226,
    60: 235,
    61: 39,
    62: 178,
    63: 117,
    64: 9,
    65: 131,
    66: 44,
    67: 26,
    68: 27,
    69: 110,
    70: 90,
    71: 160,
    72: 82,
    73: 59,
    74: 214,
    75: 179,
    76: 41,
    77: 227,
    78: 47,
    79: 132,
    80: 83,
    81: 209,
    82: 0,
    83: 237,
    84: 32,
    85: 252,
    86: 177,
    87: 91,
    88: 106,
    89: 203,
    90: 190,
    91: 57,
    92: 74,
    93: 76,
    94: 88,
    95: 207,
    96: 208,
    97: 239,
    98: 170,
    99: 251,
    100: 67,
    101: 77,
    102: 51,
    103: 133,
    104: 69,
    105: 249,
    106: 2,
    107: 127,
    108: 80,
    109: 60,
    110: 159,
    111: 168,
    112: 81,
    113: 163,
    114: 64,
    115: 143,
    116: 146,
    117: 157,
    118: 56,
    119: 245,
    120: 188,
    121: 182,
    122: 218,
    123: 33,
    124: 16,
    125: 255,
    126: 243,
    127: 210,
    128: 205,
    129: 12,
    130: 19,
    131: 236,
    132: 95,
    133: 151,
    134: 68,
    135: 23,
    136: 196,
    137: 167,
    138: 126,
    139: 61,
    140: 100,
    141: 93,
    142: 25,
    143: 115,
    144: 96,
    145: 129,
    146: 79,
    147: 220,
    148: 34,
    149: 42,
    150: 144,
    151: 136,
    152: 70,
    153: 238,
    154: 184,
    155: 20,
    156: 222,
    157: 94,
    158: 11,
    159: 219,
    160: 224,
    161: 50,
    162: 58,
    163: 10,
    164: 73,
    165: 6,
    166: 36,
    167: 92,
    168: 194,
    169: 211,
    170: 172,
    171: 98,
    172: 145,
    173: 149,
    174: 228,
    175: 121,
    176: 231,
    177: 200,
    178: 55,
    179: 109,
    180: 141,
    181: 213,
    182: 78,
    183: 169,
    184: 108,
    185: 86,
    186: 244,
    187: 234,
    188: 101,
    189: 122,
    190: 174,
    191: 8,
    192: 186,
    193: 120,
    194: 37,
    195: 46,
    196: 28,
    197: 166,
    198: 180,
    199: 198,
    200: 232,
    201: 221,
    202: 116,
    203: 31,
    204: 75,
    205: 189,
    206: 139,
    207: 138,
    208: 112,
    209: 62,
    210: 181,
    211: 102,
    212: 72,
    213: 3,
    214: 246,
    215: 14,
    216: 97,
    217: 53,
    218: 87,
    219: 185,
    220: 134,
    221: 193,
    222: 29,
    223: 158,
    224: 225,
    225: 248,
    226: 152,
    227: 17,
    228: 105,
    229: 217,
    230: 142,
    231: 148,
    232: 155,
    233: 30,
    234: 135,
    235: 233,
    236: 206,
    237: 85,
    238: 40,
    239: 223,
    240: 140,
    241: 161,
    242: 137,
    243: 13,
    244: 191,
    245: 230,
    246: 66,
    247: 104,
    248: 65,
    249: 153,
    250: 45,
    251: 15,
    252: 176,
    253: 84,
    254: 187,
    255: 22,
}