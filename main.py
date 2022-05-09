import matplotlib.pyplot as plt
import os
import functions


def main():
    functions.set_rc_params()

    plot1 = PlotData("plot1")
    plot1.set_data("data1", [0, 1, 2], [4, 5, 6])
    plot1.set_labels("XLabel", "YLabel")
    plot1.set_limits([0, 2], [0, 6])

    fig1 = plt.figure(figsize=(6, 4))
    ax1 = fig1.add_subplot(111)
    for i in range(plot1.N_data):
        ax1.scatter(plot1.x[i], plot1.y[i], label=plot1.data_label[i])
        # ax1.plot(plot1.x[i], plot1.y[i], label=plot1.data_label[i])
    ax1.set_xlabel(plot1.x_label)
    ax1.set_ylabel(plot1.y_label)
    ax1.set_xlim(plot1.x_limit)
    ax1.set_ylim(plot1.y_limit)
    # ax1.semilogy()
    ax1.legend(bbox_to_anchor=(1, 0.95), loc='upper right', borderaxespad=0.5, fontsize=18)
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


