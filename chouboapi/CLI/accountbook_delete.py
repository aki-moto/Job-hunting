import accountbook
import json
import inpututil
import requests
import pprint

def execute():
    
    print('*** 帳簿削除 ***')
    id = inpututil.input_int('IDを入力してください : ')
    print('以下の帳簿を削除します\n')
    url = f"http://localhost:8000/accountbook/{id}/"

    response1 = requests.get(url)

    json = response1.json()
    if json != ['Not Found']:
        for lists in [json['list']]:
            print(f"{lists['id']} {lists['day']}",end=' ')
            if lists['type'] == 1:
                print('収入',end=' ')
            elif lists['type'] == 2:
                print('支出',end=' ')
            print(f"{lists['title']}",end=' ')
            print ("¥{:,d}".format(lists['money']))
    else:
        print('そのIDは登録されていません\n')
        accountbook.execute()

    kakunin = inpututil.input_boolean('\n本当に削除してもよろしいですか？(y/n) : ')

    if kakunin:
        response = requests.delete(url)

        if response.status_code == 204:
            print('\n帳簿を削除しました\n')
        else:
            print('\n削除に失敗しました\n')
    else:
        print('\n削除をキャンセルしました\n')
        accountbook.execute()
    accountbook.execute()

if __name__ == "__main__":
    execute()