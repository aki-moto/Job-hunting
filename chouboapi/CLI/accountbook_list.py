import accountbook
import requests
import inpututil
import datetime

def execute():
    date = inpututil.input_date3('年月を入力してください[%Y-%m] : ')

    url = f"http://localhost:8000/accountbook/{date}"


    response = requests.get(url)

    json = response.json()
    lists = json['list']


    type1,type2 = [],[]
    
    print('*** 帳簿一覧 ***')

    day = datetime.datetime.strptime(date, '%Y-%m')
    print(f"\n-- {day.year}年{day.month}月 --\n")
    print("ID 年月日    種別 内訳    金額")
    print(f"-------------------------------------")
    for list in lists:
        print(f"{list['id']} {list['day']}",end=' ')
        if list['type'] == 1:
            type1.append(list['money'])
            print('収入',end=' ')
        elif list['type'] == 2:
            type2.append(list['money'])
            print('支出',end=' ')
        print(f"{list['title']}",end=' ')
        print ("¥{:,d}".format(list['money']))
    
    print('\n収入: ¥{:,d}'.format(sum(type1)))
    print('支出: ¥{:,d}'.format(sum(type2)))
    print('合計: ¥{:,d}\n'.format(sum(type1)-sum(type2)))

    accountbook.execute()

if __name__ == "__main__":
    execute()