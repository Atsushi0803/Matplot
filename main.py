import matplotlib.pyplot as plt
import os
import functions


def main():
    functions.set_rc_params()

    # plot1 = PlotData("css-apcma_sf7_lp")
    # plot1.set_data("BW:250kHz", list(range(1, 7)), [0, 0, 0, 0.005025538, 0.00568108, 0.009944424])
    # plot1.set_data("BW:1000kHz",  list(range(1, 7)), [0, 0, 0, 9.40E-05, 0.00123092, 0.00020896])
    # plot1.set_labels("Number of TX", "Loss Probability")

    plot1 = PlotData("css-apcma_sf7_mp")
    plot1.set_data("BW:250kHz", list(range(1, 7)), [0, 0.000373878, 0.006335054, 0.034897312, 0.058296079, 0.076776499])
    plot1.set_data("BW:1000kHz",  list(range(1, 7)), [0, 0.000435974, 0.00066313, 0.006583393, 0.007315115, 0.008506859])
    plot1.set_labels("Number of TX", "Misdetection Probability")

    # plot1 = PlotData("lora_sf7_lp")
    # plot1.set_data("BW:250kHz", list(range(1, 7)), [0.008, 0.0085, 0.005, 0.0035, 0.0566, 0.1241])
    # plot1.set_data("BW:1000kHz", list(range(1, 7)), [0.001, 0.0025, 0.3063, 0.0695, 0.0036, 0.2151])
    # plot1.set_labels("Number of TX", "Loss Probability")

    fig1 = plt.figure(figsize=(6, 4))
    ax1 = fig1.add_subplot(111)
    for i in range(plot1.N_data):
        ax1.scatter(plot1.x[i], plot1.y[i], label=plot1.data_label[i], marker=plot1.markers[i])
        # ax1.plot(plot1.x[i], plot1.y[i], label=plot1.data_label[i])
    ax1.set_xlabel(plot1.x_label)
    ax1.set_ylabel(plot1.y_label)
    ax1.set_xlim(plot1.x_limit)
    ax1.set_ylim(plot1.y_limit)
    # ax1.semilogy()
    ax1.legend(bbox_to_anchor=(0, 0.8), loc='upper left', borderaxespad=0.5, fontsize=18)
    fig1.tight_layout()

    plt.show()
    os.chdir("C:\\Users\\Atsushi.N\\Desktop")
    fig1.savefig(plot1.plot_name)
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

        self.markers = ["o", "x"]

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


