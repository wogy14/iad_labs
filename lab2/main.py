import pandas as pd
import graphics
import plotly.express as px

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # Зчитуємо дані
    df = pd.read_csv("covid19.csv", sep=",")

    df['zvit_date'] = pd.to_datetime(df['zvit_date'])
    print(df)

    # Відбираємо тільки Житомирську область
    df_by_area = df[df['registration_area'] == "Житомирська"]

    # Групуємо дані по ознаці "однакова дата" за операцією SUM
    df_grouped = df_by_area.groupby('zvit_date').sum().reset_index()

    # Будуємо графік динаміки активниx
    graphics.buildGraphic(df_grouped, 'zvit_date', 'active_confirm', 'line')

    # Будуємо графік динаміки госпіталізованих
    graphics.buildGraphic(df_grouped, 'zvit_date', 'new_susp', 'line')

    # Будуємо графік динаміки підтверджених
    graphics.buildGraphic(df_grouped, 'zvit_date', 'new_confirm', 'line')

    # Будуємо графік динаміки летальних
    graphics.buildGraphic(df_grouped, 'zvit_date', 'new_death', 'line')

    # Будуємо графік динаміки виздоровівших
    graphics.buildGraphic(df_grouped, 'zvit_date', 'new_recover', 'line')

    # Будуємо графік для порівняльного аналізу захворівших по областях
    df_grouped_by_region = df.groupby('registration_area').sum().reset_index()
    graphics.buildGraphic(df_grouped_by_region, 'registration_area', 'new_confirm', 'pie')

    #Будуємо карту
    df_for_map = pd.read_csv("covid19_actual.csv", sep=",")
    fig = px.scatter_mapbox(df_for_map, lat="registration_settlement_lat", lon="registration_settlement_lng",
                            hover_name="registration_settlement",
                            hover_data=["registration_area", "registration_region", "registration_area", "total_susp",
                                        "total_confirm", "total_death", "total_recover"],
                            color_discrete_sequence=["green"], zoom=5, height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()

    # Експортуємо дані в ексель
    with pd.ExcelWriter('output.xlsx') as writer:
        df_grouped.to_excel(writer, sheet_name='Житомирська обл.')  # Дані по Житомирській області
        df_for_map.to_excel(writer, sheet_name='Україна з локаціями')  # Дані всієї України з локацями
