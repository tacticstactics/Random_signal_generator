import numpy as np


def bit_to_QPSK(TX_bit):
    # 入力bit系列のサイズを記録
    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]

    # まずは入力bit系列をBPSK変調
    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    # 平均電力が1になるように1/np.sqrt(2)をかけて、
    # BPSK系列の奇数番目は実部に、偶数番目は虚部になるように合成
    TX_BPSK = TX_BPSK * 1 / np.sqrt(2)
    TX_QPSK = TX_BPSK[:, 0:bit_num:2] + 1j * TX_BPSK[:, 1:bit_num:2]

    return TX_QPSK


def bit_to_16QAM(TX_bit):
    # 入力bit系列のサイズを記録
    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]
    sym_num = bit_num / 4

    # まずは入力bit系列をBPSK変調
    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    # 奇数番目のシンボルの重みをもたせた上で合成
    temp = 2 * TX_BPSK[:, 0:bit_num:2] + TX_BPSK[:, 1:bit_num:2]

    # 出力結果がグレイ符号化になるように調整
    temp_copy = temp.copy()
    temp[temp_copy == 3] = 1
    temp[temp_copy == 1] = 3

    TX_16QAM = (temp[:, 0:int(sym_num * 2):2] + 1j * temp[:, 1:int(sym_num * 2):2]) * 1 / np.sqrt(10)

    return TX_16QAM


def bit_to_64QAM(TX_bit):
    # 入力bit系列のサイズを記録
    temp = TX_bit.shape
    M = temp[0]
    bit_num = temp[1]
    sym_num = bit_num / 4

    # まずは入力bit系列をBPSK変調
    TX_BPSK = np.ones((M, bit_num))
    TX_BPSK[TX_bit == 0] = -1

    # シンボルの重みをもたせた上で合成
    temp = 4 * TX_BPSK[:, 0:bit_num:3] + 2 * TX_BPSK[:, 1:bit_num:3] + TX_BPSK[:, 2:bit_num:3]

    # 出力結果がグレイ符号化になるように調整
    temp_copy = temp.copy()
    temp[temp_copy == 7] = 3
    temp[temp_copy == 5] = 1
    temp[temp_copy == 3] = 5
    temp[temp_copy == 1] = 7
    temp[temp_copy == -3] = -1
    temp[temp_copy == -1] = -3

    TX_64QAM = (temp[:, 0:int(sym_num * 3):2] + 1j * temp[:, 1:int(sym_num * 3):2]) * 1 / np.sqrt(42)

    return TX_64QAM


# 送信側アンテナ数
M = 2
# 受信側アンテナ数
N = M
# 送信ビット数
bit_num = 12 * 10 ** 2

# 送信ビット列を生成
TX_bit = np.random.randint(0, 2, (M, bit_num))

# 各種変調を実行
TX_QPSK = bit_to_QPSK(TX_bit)
TX_16QAM = bit_to_16QAM(TX_bit)
TX_64QAM = bit_to_64QAM(TX_bit)

print(TX_bit)
print(TX_QPSK)
print(TX_16QAM)
print(TX_64QAM)