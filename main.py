import pandas as pd
import xml.etree.ElementTree as ET


def main():
    test_work()


# тестовое задание
def test_work():
    # Получение данных из выгруженных xml файлов с курсами валют
    usd_df = get_data('dataset/usd_rub.xml')
    jpy_df = get_data('dataset/jpy_rub.xml')

    # объединение двух таблиц
    result_df = pd.concat([usd_df, jpy_df], axis=1)

    # переименование столбцов
    result_df.columns = ['Дата USD/RUB', 'Курс USD/RUB', 'Время USD/RUB', 'Дата JPY/RUB', 'Курс JPY/RUB', 'Время JPY/RUB']

    # приведение значения курса валют к типу float
    result_df['Курс USD/RUB'] = result_df['Курс USD/RUB'].astype(float)
    result_df['Курс JPY/RUB'] = result_df['Курс JPY/RUB'].astype(float)

    # вычисление столбца Результат
    result_df['Результат'] = result_df['Курс USD/RUB'] / result_df['Курс JPY/RUB']

    # выгрузка данных в Excel
    result_df.to_excel('result_data/result.xlsx', index=False)


# Чтение данных из xml файла
def get_data(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    rows = root.findall('.//row')
    rows_mas = []
    for row in rows:
        clearing = row.get('clearing')
        if clearing == 'vk':
            row_dict = {
                'tradedate': row.get('tradedate'),
                'rate': row.get('rate'),
                'tradetime': row.get('tradetime')
            }
            rows_mas.append(row_dict)

    df = pd.DataFrame(rows_mas)
    return df


# точка входа в программу
if __name__ == '__main__':
    main()
