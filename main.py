import matplotlib.pyplot as plt
import os
import functions


def main():
    functions.set_rc_params()

    # plot1 = PlotData("duty_changed")
    # plot1.set_data("LoRa", [1.67, 3.33, 5.00, 6.67, 8.33, 10.00], list(range(6)))
    # plot1.set_data("CSS-APCMA", [1.67, 3.33, 5.00, 6.67, 8.33, 10.00], list(range(6)))
    # plot1.set_labels(r'Duty Cycle[%]', "packet error rate[%]")
    # plot1.markers = ["o", "x"]
    # plot1.colors = ["tab:blue", "tab:orange"]

    # plot1 = PlotData("ntx_changed")
    # plot1.set_data("LoRa", list(range(1, 7)), list(range(6)))
    # plot1.set_data("CSS-APCMA", list(range(1, 7)), list(range(6)))
    # plot1.set_labels(r'Number of Transmitters', "packet error rate[%]")
    # plot1.markers = ["o", "x"]
    # plot1.colors = ["tab:blue", "tab:orange"]

    # plot1 = PlotData("SignalGain_changed")
    # plot1.set_data("OOK-APCMA", list(range(1, 7)), list(range(6)))
    # plot1.set_data("CSS-APCMA", list(range(1, 7)), list(range(6)))
    # plot1.set_labels(r'SNR[dB]', "packet error rate[%]")
    # plot1.markers = ["o", "x"]
    # plot1.colors = ["tab:green", "tab:orange"]

    # plot1 = PlotData("NoiseGain_changed")
    # plot1.set_data("OOK-APCMA", list(range(1, 7)), list(range(6)))
    # plot1.set_data("CSS-APCMA", list(range(1, 7)), list(range(6)))
    # plot1.set_labels(r'SNR[dB]', "packet error rate[%]")
    # plot1.markers = ["o", "x"]
    # plot1.colors = ["tab:green", "tab:orange"]

    fig1 = plt.figure(figsize=(6, 4))
    ax1 = fig1.add_subplot(111)
    for i in range(plot1.N_data):
        ax1.scatter(plot1.x[i], plot1.y[i], label=plot1.data_label[i], marker=plot1.markers[i], color=plot1.colors[i])
        ax1.plot(plot1.x[i], plot1.y[i], color=plot1.colors[i])
    ax1.set_xlabel(plot1.x_label, fontname="MS Gothic", fontsize=18)
    ax1.set_ylabel(plot1.y_label, fontname="MS Gothic", fontsize=18)
    # ax1.set_xlim(plot1.x_limit)
    # ax1.set_ylim(plot1.y_limit)
    # ax1.semilogy()
    # ax1.legend(bbox_to_anchor=(0.15, 1), loc='lower left', borderaxespad=0.2, fontsize=18)
    ax1.legend()
    fig1.tight_layout()


    plt.show()
    os.chdir("C:\\Users\\Atsushi.N\\Desktop")
    fig1.savefig(plot1.plot_name+".pdf")
    plt.close()


class PlotData:
    def __init__(self, name):
        self.N_data = 0
        self.plot_name = name
        self.x_label = None
        self.y_label = None
        self.x_limit = None
        self.y_limit = None

        self.data_label = []
        self.x = []
        self.y = []
        self.markers = None
        self.colors = None

    def set_data(self, label, x, y):
        self.N_data += 1
        self.data_label.append(label)
        self.x.append(x)
        self.y.append(y)

    def set_labels(self, x_label, y_label):
        self.x_label = x_label
        self.y_label = y_label

    def set_limits(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit


if __name__ == '__main__':
    main()


