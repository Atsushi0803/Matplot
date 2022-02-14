import matplotlib.pyplot as plt


def set_rc_params():
    # フォントの種類とサイズを設定する。
    plt.rcParams['font.size'] = 20
    plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # 方向に目盛り線を描くかどうか
    plt.rcParams["xtick.top"] = True
    plt.rcParams["xtick.bottom"] = True
    plt.rcParams["ytick.left"] = True
    plt.rcParams["ytick.right"] = True

    # 目盛りのフォントサイズ
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14


def plot(x, y):
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    for i in range(len(x)):
        ax.plot(x[i], y[i])
        # ax.scatter(x[i], y[i])
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Power')
    # plt.legend()
    fig.tight_layout()
