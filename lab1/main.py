import pandas as pd
import re
import graphics


def convert12to24(str1):
    str1 = '0' + str1 if str1[1] == ':' else str1

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "AM":
        return str1[:-2]

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:-2]


def parseDataFrame(df):
    shortMonthORString = "|".join(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    for column in df.columns:
        df[column] = df[column].apply(
            lambda x: (str(x) + '.2019' if bool(re.match("^\d{1,2}\.(" + shortMonthORString + ")$", str(x))) else x))
        df[column] = df[column].apply(
            lambda x: (
                convert12to24(x) if bool(re.match("^((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))$", str(x))) else x))
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
    df = pd.read_csv("DATABASE.csv", sep=";")
    df = parseDataFrame(df)
    df.set_index('day/month', inplace=True)

    graphics.selectAndShowGraphics(df)
