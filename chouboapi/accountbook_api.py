from fastapi import FastAPI, Response, status # 追加
from pydantic import BaseModel
import mysql.connector # 追加
import datetime

app = FastAPI()

class Memo(BaseModel):
    day: datetime.date
    type: int
    title: str
    money: int

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='accountbook'
)

#登録用api
@app.post("/accountbook/", status_code=201)
def register(lists: Memo):
    sql = 'INSERT INTO list (day, type, title, money) VALUES (%s, %s, %s,%s)'
    data = [lists.day, lists.type, lists.title, lists.money]

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, data)
    mydb.commit()

    return {'Created'}

#list一覧表示用api
@app.get("/accountbook/")
def all_find(): 
    sql = "SELECT * FROM list ORDER BY day"

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()

    return {'list': result}

#年月でselect表示用api
@app.get("/accountbook/{date}", status_code=200)
def find_date(date, response:Response):
    ndate = date + "-01"
    sql = "SELECT * FROM list WHERE day between %s and LAST_DAY(%s) ORDER BY day"
    data = [ndate, ndate]

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, data)
    result = cursor.fetchall()

    if result != None:
        return{'list' : result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}

#IDでselect表示用api
@app.get("/accountbook/{id}/")
def find_by_id(id:int, response:Response):
    sql = "select * from list where id = %s"
    data = [id]

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, data)
    result = cursor.fetchone()

    if result != None:
        return {'list': result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Not Found'}

#更新用api
@app.put("/accountbook/{id}/", status_code=204)
def update(id:int, lists:Memo, response:Response): #追加

    # IDの存在チェック
    if is_list_id_exists(id):
        sql = 'UPDATE list SET day = %s, type = %s, title = %s, money = %s WHERE id = %s'
        data = [lists.day, lists.type, lists.title, lists.money, id]

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, data)
        mydb.commit()

        return {'Updated'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Not Found'}

#削除用api
@app.delete("/accountbook/{id}/", status_code=204)
def delete(id:int, response: Response):  # 追加
    # IDの存在チェック
    if is_list_id_exists(id):
        sql = 'DELETE FROM list WHERE id = %s'
        data = [id]

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, data)
        mydb.commit()
        return {'Deleted'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Not Found'}


def is_list_id_exists(id):
    sql = "SELECT * FROM list WHERE id = %s"
    data = [id]

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, data)
    result = cursor.fetchone()

    return result != None