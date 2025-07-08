import accountbook
import requests
import json
import inpututil


def execute():
    print('*** 帳簿登録 ***')
    while True:
        type = inpututil.input_int('収入(1) or 支出(2)を入力してください : ')
        if type == 1 or type == 2:
            break
        print('1 or 2 を入力してください')    
    day = inpututil.input_date('日付を入力してださい [%Y-%m-%d] : ')
    title = input('内訳を入力してください : ')
    money = inpututil.input_int('金額を入力してください : ')

    url = 'http://localhost:8000/accountbook/'



    data = {
        "day" : day,
        "type" : type,
        "title" : title,
        "money" : money
    }

    json_data = json.dumps(data)

    headers = {"Content-Type":"application/json"}

    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 201:
        print('\n帳簿を登録しました\n')
    else:
        print('\n登録に失敗しました\n')

    accountbook.execute()

if __name__ == "__main__":
    execute()
