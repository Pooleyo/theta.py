def run(x, y, style, x_label, y_label, plot_name, file_name):

    import matplotlib.pyplot as plt
    import os

    print "Plotting..."

    if os.path.exists("output") is False:

        os.makedirs("output")

    plt.plot(x, y, style)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_name)
    plt.savefig("output/" + file_name)
    plt.close()

    return
