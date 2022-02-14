import matplotlib.pyplot as plt
import os
import functions


def main():
    functions.set_rc_params()

    traffic_rate = [i * 20 for i in range(6)]
    fig1 = plt.figure(figsize=(6, 4))
    ax1 = fig1.add_subplot(111)
    ook = [2.00, 2.28, 1.89, 2.18, 3.12, 8.06]
    css = [0.00, 0.00, 0.40, 0.51, 2.75, 9.38]
    lora = [0.20, 29.47, 56.22, 80.69, 89.47, 89.13]
    ax1.scatter(traffic_rate, ook, label="OOK-APCMA", marker="o")
    ax1.scatter(traffic_rate, css, label="CSS-APCMA", marker="+")
    ax1.scatter(traffic_rate, lora, label="LoRa", marker="D")
    ax1.set_xlabel('Traffic Rate[%]')
    ax1.set_ylabel('Loss Probability[%]')
    plt.legend()
    fig1.tight_layout()

    fig2 = plt.figure(figsize=(6, 4))
    ax2 = fig2.add_subplot(111)
    ook = [0.97, 2.09, 4.38, 6.13, 12.88, 24.69]
    css = [0.13, 0.13, 2.71, 5.75, 17.32, 31.17]
    ax2.scatter(traffic_rate, ook, label="OOK-APCMA", marker="o")
    ax2.scatter(traffic_rate, css, label="CSS-APCMA", marker="+")
    ax2.set_xlabel('Traffic Rate[%]')
    ax2.set_ylabel('Misdetection Probability[%]')
    plt.legend()
    fig2.tight_layout()

    fig3 = plt.figure(figsize=(6, 4))
    ax3 = fig3.add_subplot(111)
    snr = [-10.21993926, -8.688797219, -7.387544304, -6.525426692, -4.357749023, -1.993225644, 0.279394807, 1.66285089, 3.904747908, 5.818213772, 8.124981203, 9.94590615]
    ook = [100 * 1.00, 100 * 1.00, 100 * 1.00, 100 * 1.00, 100 * 0.8493333333333333, 100 * 0.18333333333333332, 100 * 0.009666666666666667, 100 * 0.0036666666666666627, 100 * 0.0033333333333333435, 100 * 0.002666666666666662, 100 * 0.001666666666666683, 100 * 0.003666666666666685]
    css = [100 * 1.000, 100 * 0.9690000000000001, 100 * 0.632, 100 * 0.15833333333333333, 100 * 0.009333333333333327, 100 * 0.01499999999999999, 100 * 0.002666666666666684, 100 * 0.015666666666666672, 100 * 0.014333333333333332, 100 * 0.021666666666666678, 100 * 0.018000000000000016, 100 * 0.008000000000000007]
    ax3.scatter(snr, ook, label="OOK-APCMA", marker="o")
    ax3.scatter(snr, css, label="CSS-APCMA", marker="+")
    ax3.set_xlabel('SNR[dB]')
    ax3.set_ylabel('Loss Probability[%]')
    ax3.legend()
    ax3.set_xlim([-11, 5])
    fig3.tight_layout()

    plt.show()
    # os.chdir("D:\\Documents\\MyPaper\\GraduationThesis\\figure\\result")
    # fig1.savefig("1_mp.svg")
    # fig2.savefig("1_lp.svg")
    # fig3.savefig("2_lp.svg")


if __name__ == '__main__':
    main()


