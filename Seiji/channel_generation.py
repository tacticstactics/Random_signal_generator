
import numpy as np

def AWGN_noise(EbNo, N, sym_num, bit_num):
    """
    EbNo : 発生させたい雑音の強度を決める
    N : 受信機側アンテナの数
    sym_num : 送信シンボル系列長
    bit_num : 送信ビット系列長
    """

    #変調多値数を求める　QSPK : 2, 16QAM : 4, 64QAM : 6となる値
    QAM_order = int(bit_num / sym_num)
    SNR = QAM_order * 10 ** (EbNo / 10)
    No = 1 / SNR

    noise = np.random.normal(0, np.sqrt(No / 2), (N, sym_num)) \
            + 1j * np.random.normal(0, np.sqrt(No / 2), (N, sym_num))

    return noise
