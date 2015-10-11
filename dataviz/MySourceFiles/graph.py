from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import parse

def visualize_days():
    """Visualize data by day of the week"""

    #grab the data that was parsed in the first portion of this tutorial
    data_file = parse.parse(parse.MY_FILE, ",")

    # make a variable, 'counter', from iterating through each line of data
    # in the parsed data, then count the number of incidents happen each
    # day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the data that will be on the x-axis (day of the week) from
    # the 'counter' variable from the y-axis data (number of
    # incidents per day)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # assign the y-axis data to a matplotlib plot instance
    plt.plot(data_list)

    # create the amount of ticks needed to represent the x-axis data and
    # assign the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save the plotted data
    plt.savefig("Days.png")

    # then close the plot file
    plt.clf()

def visualize_type():
    """Visualize data by type in a bar graph"""

    #grab the data that was parsed in the first portion of this tutorial
    data_file = parse.parse(parse.MY_FILE, ",")

    # make a variable, 'counter', from iterating through each line of data
    # in the parsed data, then count how many incidents happen each category
    counter = Counter(item["Category"] for item in data_file)

    # set labels which come from the results of the counter, order isn't important
    # so we can just put them into counter.keys()
    labels = tuple(counter.keys())

    # set label placement on x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # define the width of the graph's bars for the plotted data
    width = 0.5
    # actually apply the data to the bar plot (like plt.plot() above)
    plt.bar(xlocations, counter.values(), width=width)

    # assign labels and tick marks to the x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # pad space around the x-axis for the labels
    plt.subplots_adjust(bottom=0.4)

    # enlarge the size of the graph
    plt.rcParams['figure.figsize'] = 12, 8

    # save graph
    plt.savefig("Type.png")

    # close the plot figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()
