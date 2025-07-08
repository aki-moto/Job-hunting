import datetime


# キーボードの入力内容を整数で返します
def input_int(prompt):
    while True:
        str = input(prompt)

        # 整数チェック
        if not str.isdigit():
            print('エラー!!!: 整数で入力してください')
            continue
        break

    return int(str)


# キーボードの入力内容を日付で返します
def input_date(prompt):
    while True:
        str = input(prompt)

        try:
            datetime.datetime.strptime(str, '%Y-%m-%d')
        except ValueError:
            print('エラー!!!: [YYYY-mm-dd]で入力してください')
            continue

        break

    return str


# キーボードの入力内容を日付で返します
def input_date3(prompt):
    while True:
        str = input(prompt)

        try:
            datetime.datetime.strptime(str, '%Y-%m')
        except ValueError:
            print('エラー!!!: [YYYY-mm]で入力してください')
            continue

        break

    return str


# キーボードの任意入力内容を日付で返します
def input_date2(prompt):
    while True:
        str = input(prompt)

        if len(str) == 0:
            break
        try:
            datetime.datetime.strptime(str, '%Y-%m-%d')
        except ValueError:
            print('エラー!!!: 日付で入力してください')
            continue

        break

    return str


# キーボードからのy/nの入力をTrue/Falseで返します
def input_boolean(prompt):
    while True:
        str = input(prompt).strip()
        if str.lower() == 'y':
            return True
        elif str.lower() == 'n':
            return False
        if str.lower() != 'y' or str.lower() != 'n':
            print("'y' or 'n' で入力してください")
