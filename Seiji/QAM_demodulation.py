import numpy as np

def QPSK_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 2

    odd_bit = np.real(RX_symbol)
    odd_bit[odd_bit > 0] = 1
    odd_bit[odd_bit < 0] = 0

    even_bit = np.imag(RX_symbol)
    even_bit[even_bit > 0] = 1
    even_bit[even_bit < 0] = 0

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:2] = odd_bit
    RX_bit[:, 1:bit_num:2] = even_bit

    return RX_bit


def QAM16_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 4

    # 整数に直す
    RX_symbol = RX_symbol * np.sqrt(10)

    # 複素数を一旦分離する
    RX_symbol_real = np.real(RX_symbol)
    RX_symbol_imag = np.imag(RX_symbol)

    # 最も近いシンボルの値に丸め込み
    real_copy = RX_symbol_real.copy()
    imag_copy = RX_symbol_imag.copy()

    RX_symbol_real[real_copy > 2] = 3
    RX_symbol_real[2 > real_copy] = 1
    RX_symbol_real[0 > real_copy] = -1
    RX_symbol_real[-2 > real_copy] = -3

    RX_symbol_imag[imag_copy > 2] = 3
    RX_symbol_imag[2 > imag_copy] = 1
    RX_symbol_imag[0 > imag_copy] = -1
    RX_symbol_imag[-2 > imag_copy] = -3

    # 再び結合し、もろもろの操作
    temp = np.zeros((N, sym_num * 2))
    temp[:, 0:sym_num*2:2] = RX_symbol_real
    temp[:, 1:sym_num*2:2] = RX_symbol_imag

    temp2 = np.zeros((N, sym_num * 2)) + 1j * np.zeros((N, sym_num * 2))
    temp2[temp == 3] = 1 - 0j
    temp2[temp == 1] = 1 + 1j
    temp2[temp == -1] = - 0 + 1j
    temp2[temp == -3] = - 0 - 0j

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:2] = np.real(temp2)
    RX_bit[:, 1:bit_num:2] = np.imag(temp2)

    return RX_bit

def QAM64_to_bit(RX_symbol):
    temp = RX_symbol.shape
    N = temp[0]
    sym_num = temp[1]
    bit_num = sym_num * 6

    # 整数に直す
    RX_symbol = RX_symbol * np.sqrt(42)

    # 複素数を一旦分離する
    RX_symbol_real = np.real(RX_symbol)
    RX_symbol_imag = np.imag(RX_symbol)

    # 最も近いシンボルの値に丸め込み
    real_copy = RX_symbol_real.copy()
    imag_copy = RX_symbol_imag.copy()

    RX_symbol_real[real_copy > 6] = 7
    RX_symbol_real[6 > real_copy] = 5
    RX_symbol_real[4 > real_copy] = 3
    RX_symbol_real[2 > real_copy] = 1
    RX_symbol_real[0 > real_copy] = -1
    RX_symbol_real[-2 > real_copy] = -3
    RX_symbol_real[-4 > real_copy] = -5
    RX_symbol_real[-6 > real_copy] = -7

    RX_symbol_imag[imag_copy > 6] = 7
    RX_symbol_imag[6 > imag_copy] = 5
    RX_symbol_imag[4 > imag_copy] = 3
    RX_symbol_imag[2 > imag_copy] = 1
    RX_symbol_imag[0 > imag_copy] = -1
    RX_symbol_imag[-2 > imag_copy] = -3
    RX_symbol_imag[-4 > imag_copy] = -5
    RX_symbol_imag[-6 > imag_copy] = -7

    # 再び結合し、もろもろの操作
    temp = np.zeros((N, sym_num * 2))
    temp[:, 0:sym_num*2:2] = RX_symbol_real
    temp[:, 1:sym_num*2:2] = RX_symbol_imag

    RX_bit_first = np.zeros((N, int(bit_num/3)))
    RX_bit_first[temp > 0] = 1
    RX_bit_first[temp < 0] = 0

    RX_bit_second = np.zeros((N, int(bit_num / 3)))
    RX_bit_second[temp == 7] = 0
    RX_bit_second[temp == 5] = 0
    RX_bit_second[temp == 3] = 1
    RX_bit_second[temp == 1] = 1
    RX_bit_second[temp == -1] = 1
    RX_bit_second[temp == -3] = 1
    RX_bit_second[temp == -5] = 0
    RX_bit_second[temp == -7] = 0

    RX_bit_third = np.zeros((N, int(bit_num / 3)))
    RX_bit_third[temp == 7] = 0
    RX_bit_third[temp == 5] = 1
    RX_bit_third[temp == 3] = 1
    RX_bit_third[temp == 1] = 0
    RX_bit_third[temp == -1] = 0
    RX_bit_third[temp == -3] = 1
    RX_bit_third[temp == -5] = 1
    RX_bit_third[temp == -7] = 0

    RX_bit = np.zeros((N, bit_num))
    RX_bit[:, 0:bit_num:3] = RX_bit_first
    RX_bit[:, 1:bit_num:3] = RX_bit_second
    RX_bit[:, 2:bit_num:3] = RX_bit_third

    return RX_bit