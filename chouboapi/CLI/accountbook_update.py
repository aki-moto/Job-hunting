import accountbook
import requests
import json
import inpututil

def execute():
    print('*** 帳簿更新 ***')
    id = inpututil.input_int('IDを入力してください : ')

    url = f"http://localhost:8000/accountbook/{id}/"
    response1 = requests.get(url)

    jsons = response1.json()

    print("以下の帳簿を更新します\n")
    print("ID 年月日    種別 内訳    金額")
    print(f"-------------------------------------")
    
    if jsons != ['Not Found'] :
        for list in [jsons['list']]:
            print(f"{list['id']} {list['day']}",end=' ')
            if list['type'] == 1:
                print('収入',end=' ')
            elif list['type'] == 2:
                print('支出',end=' ')
            print(f"{list['title']}",end=' ')
            print ("¥{:,d}".format(list['money']))
    else:
        print('そのIDは登録されていません\n')
        accountbook.execute()

    while True:
        type = inpututil.input_int('\n収入(1) or 支出(2)を入力してください : ')
        if type == 1 or type == 2:
            break
        print('1 or 2 を入力してください')

    day = inpututil.input_date('日付を入力してださい [%Y-%m-%d] : ')
    title = input('内訳を入力してください : ')
    money = inpututil.input_int('金額を入力してください : ')


    data = {
        "day" : day,
        "type" : type,
        "title" : title,
        "money" : money
    }

    json_data = json.dumps(data)

    headers = {"Content-Type":"application/json"}

    response = requests.put(url, data=json_data, headers=headers)

    if response.status_code == 204:
        print('\n更新しました\n')
    else:
        print('\n更新に失敗しました\n')
        
    accountbook.execute()

if __name__ == "__main__":
    execute()