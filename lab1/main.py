import pandas as pd
import re
import graphics


def convertTime(data):
    data = '0' + data if data[1] == ':' else data

    if data[-2:] == "AM" and data[:2] == "12":
        return "00" + data[2:-2]
    elif data[-2:] == "AM":
        return data[:-2]
    elif data[-2:] == "PM" and data[:2] == "12":
        return data[:-2]
    else:
        return str(int(data[:2]) + 12) + data[2:-2]


def parseDataFrame(df):
    shortMonthORString = "|".join(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    for column in df.columns:
        df[column] = df[column].apply(
            lambda x: (str(x) + '.2019' if bool(re.match("^\d{1,2}\.(" + shortMonthORString + ")$", str(x))) else x))
        df[column] = df[column].apply(
            lambda x: (
                convertTime(x) if bool(re.match("^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$", str(x))) else x))
        df[column] = df[column].apply(
            lambda x: (
                int(x[:-1]) if bool(re.match("^\d{1,2}\%$", str(x))) else x))
        df[column] = df[column].apply(
            lambda x: (
                int(x.replace("mph", '').strip()) if bool(re.match("\d+\s(mph)", str(x))) else x))
        df[column] = df[column].apply(
            lambda x: (
                float(x.replace(",", '.')) if bool(re.match("^\d+(,)\d+$", str(x))) else x))

    df['dateTime'] = df['day/month'] + " " + df['Time']

    return df


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    df = pd.read_csv("DATABASE.csv", sep=";")
    df = parseDataFrame(df)
    df.set_index('day/month', inplace=True)
    print(df)
    graphics.selectAndShowGraphics(df)
