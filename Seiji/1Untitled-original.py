import numpy as np
import matplotlib.pyplot as plt

# https://qiita.com/Seiji_Tanaka/items/a059090ee020a5d5c648
import QAM_modulation

# https://qiita.com/Seiji_Tanaka/items/b29d8a5a3447680370ce
import QAM_demodulation

# Qiitaのこのページの上部に記載
import channel_generation

# 送信側アンテナ数
M = 1
# 受信側アンテナ数
N = 1
# 送信ビット数
bit_num = 12 * 10 ** 5

# 計算するEbNoの範囲　freqは計測点の間隔の狭さに対応する
EbNo_min = 0
EbNo_max = 20
freq = 21
power_range = np.linspace(EbNo_min, EbNo_max, freq)

BER_QPSK = np.zeros((1, freq))
BER_16QAM = np.zeros((1, freq))
BER_64QAM = np.zeros((1, freq))
count = 0

for EbNo in power_range:
    TX_bit = np.random.randint(0, 2, (M, bit_num))

    # 変調
    TX_QPSK = QAM_modulation.bit_to_QPSK(TX_bit)
    TX_16QAM = QAM_modulation.bit_to_16QAM(TX_bit)
    TX_64QAM = QAM_modulation.bit_to_64QAM(TX_bit)

    # AWGN雑音を付加
    noise = channel_generation.AWGN_noise(EbNo, N, len(TX_QPSK[0, :]), bit_num)
    RX_QPSK = TX_QPSK + noise

    noise = channel_generation.AWGN_noise(EbNo, N, len(TX_16QAM[0, :]), bit_num)
    RX_16QAM = TX_16QAM + noise

    noise = channel_generation.AWGN_noise(EbNo, N, len(TX_64QAM[0, :]), bit_num)
    RX_64QAM = TX_64QAM + noise

    # 判定・復調
    RX_bit_QPSK = QAM_demodulation.QPSK_to_bit(RX_QPSK)
    RX_bit_16QAM = QAM_demodulation.QAM16_to_bit(RX_16QAM)
    RX_bit_64QAM = QAM_demodulation.QAM64_to_bit(RX_64QAM)

    # BERの計算
    error_sum_QPSK = np.sum(np.abs(TX_bit - RX_bit_QPSK))
    error_sum_16QAM = np.sum(np.abs(TX_bit - RX_bit_16QAM))
    error_sum_64QAM = np.sum(np.abs(TX_bit - RX_bit_64QAM))

    BER_QPSK[0, count] = error_sum_QPSK / (M * bit_num)
    BER_16QAM[0, count] = error_sum_16QAM / (M * bit_num)
    BER_64QAM[0, count] = error_sum_64QAM / (M * bit_num)
    count += 1

plt.semilogy(power_range, BER_QPSK[0,:], label="QPSK")
plt.semilogy(power_range, BER_16QAM[0,:], label='16QAM')
plt.semilogy(power_range, BER_64QAM[0,:], label="64QAM")
plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=18)
plt.ylim(10**(-5), 10**(-0))
plt.xlabel('Eb/N0 [dB]')
plt.ylabel('BER')
ax = plt.gca()
ax.set_yscale('log')
plt.grid(which="both")
plt.show()