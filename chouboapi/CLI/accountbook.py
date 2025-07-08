import accountbook_delete
import accountbook_register
import accountbook_list
import accountbook_update
import inpututil


def execute():
    print('=== 帳簿 メニュー ===')

    printmenu()

    while True:
        no = inpututil.input_int('メニューを選択してください :')
        if no == 1 or no == 2 or no == 3 or no == 4 or no == 5:
            if no == 1:
                accountbook_register.execute()     
            elif no == 2:
                accountbook_list.execute()
            elif no == 3:
                accountbook_update.execute()
            elif no == 4:
                accountbook_delete.execute()
            elif no == 5:
                print('\n終了します')
                exit()
        else:
            print('1 ~ 5で入力してください')
            continue
        

def printmenu():
    print('1. 帳簿登録')
    print('2. 帳簿一覧')
    print('3. 帳簿更新')
    print('4. 帳簿削除')
    print('5. 終了')   

if __name__ == "__main__":
    execute()