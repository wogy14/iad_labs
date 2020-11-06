import matplotlib.pyplot as plt
import pandas as pd


def buildGraphic(df, x_col, y_col, type):
    if y_col == 'single':
        if type == 'hist':
            df[x_col].hist()
        elif type == 'bar':
            df[x_col].value_counts().plot(kind='bar')
        elif type == 'box':
            df[x_col].plot.box()

        plt.xlabel(x_col)
        plt.ylabel('Count')

        if type == 'kde':
            df[x_col].plot.kde()
            plt.ylabel('Value')

        if type == 'pie':
            df[x_col].value_counts().plot.pie(subplots=True, autopct='%1.1f%%')
            plt.ylabel('')
            plt.xlabel('')

        plt.title(x_col + " " + type)
    else:
        if type == 'line':
            df.plot.line(x=x_col, y=y_col)
        elif type == 'scatter':
            df.plot.scatter(x=x_col, y=y_col)
        elif type == 'bar':
            df.plot.bar(x=x_col, y=y_col)
        elif type == 'kde':
            tDf = pd.DataFrame({
                x_col: df[x_col],
                y_col: df[y_col],
            })
            tDf.set_index(x_col, inplace=True)
            tDf.plot.kde()
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(x_col + "-" + y_col + " " + type)

        if type == 'pie':
            new_df = df
            new_df.set_index(x_col, inplace=True)
            new_df.plot.pie(y=y_col, legend=None, subplots=True, autopct='%1.1f%%', pctdistance=1, explode=[0.1 for i in range(len(new_df.index))])
            plt.xlabel("")
            plt.ylabel("")

    plt.xticks(rotation=90)
    plt.show()


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
        buildGraphic(df, columns[0], columns[1], graphic_type)
