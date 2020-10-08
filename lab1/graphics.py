import matplotlib.pyplot as plt


def selectAndShowGraphics(df):
    availableGraphicsTypes = ['line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie', 'scatter',
                              'hexbin']

    print('Count of graphics:')
    count = int(input())
    print("Available columns:\n" + "\n".join(df.columns) + "\n")
    print("Available type of graphics:\n" + "\n".join(availableGraphicsTypes) + "\n")

    for i in range(count):
        print('Please select graphic in the next format: x_axis_column->y_axis_column:graphic_type')
        selection = input().split(":")
        graphic_type = selection[1]
        columns = selection[0].split("->")
        df.plot(x=columns[0], y=columns[1], kind=graphic_type)

    plt.xticks(rotation=90)
    plt.show()
