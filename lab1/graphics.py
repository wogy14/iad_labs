import matplotlib.pyplot as plt
import pandas as pd


def selectAndShowGraphics(df):
    availableGraphicsTypes = ['line', 'bar', 'hist', 'box', 'kde', 'scatter', 'pie']

    print('Count of graphics:')
    count = int(input())
    print("Available columns:\n" + "\n".join(list(df.columns) + ['single - put as y_axis_column']) + "\n")
    print("Available type of graphics:\n" + "\n".join(availableGraphicsTypes) + "\n")

    for i in range(count):
        print('Please select graphic in the next format: x_axis_column->y_axis_column:graphic_type')
        selection = input().split(":")
        graphic_type = selection[1]
        columns = selection[0].split("->")
        if columns[1] == 'single':
            if graphic_type == 'hist':
                df[columns[0]].hist()
            elif graphic_type == 'bar':
                df[columns[0]].value_counts().plot(kind='bar')
            elif graphic_type == 'box':
                df[columns[0]].plot.box()

            plt.xlabel(columns[0])
            plt.ylabel('Count')

            if graphic_type == 'kde':
                df[columns[0]].plot.kde()
                plt.ylabel('Value')

            if graphic_type == 'pie':
                df[columns[0]].value_counts().plot.pie(subplots=True, autopct='%1.1f%%')
                plt.ylabel('')
                plt.xlabel('')

            plt.title(columns[0] + " " + graphic_type)
        else:
            if graphic_type == 'line':
                df.plot.line(x=columns[0], y=columns[1])
            elif graphic_type == 'scatter':
                df.plot.scatter(x=columns[0], y=columns[1])
            elif graphic_type == 'kde':
                tDf = pd.DataFrame({
                    columns[0]: df[columns[0]],
                    columns[1]: df[columns[1]],
                })
                tDf.set_index(columns[0], inplace=True)
                tDf.plot.kde()
            plt.xlabel(columns[0])
            plt.ylabel(columns[1])
            plt.title(columns[0] + "-" + columns[1] + " " + graphic_type)

    plt.xticks(rotation=90)
    plt.show()
