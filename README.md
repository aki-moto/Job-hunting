
---

## 使用技術

- **言語:** Python 3.x
- **フレームワーク:** FastAPI（REST API）、Requests（HTTPクライアント）
- **データベース:** MySQL
- **ライブラリ:**  
  - `fastapi`
  - `pydantic`
  - `requests`
  - `mysql-connector-python`
  - `datetime`

---

## APIエンドポイント

- **POST** `/accountbook/` – 帳簿の新規登録
- **GET** `/accountbook/` – 全件取得
- **GET** `/accountbook/{date}` – 指定年月（例：2025-07）の帳簿取得
- **GET** `/accountbook/{id}/` – ID指定で取得
- **PUT** `/accountbook/{id}/` – ID指定で更新
- **DELETE** `/accountbook/{id}/` – ID指定で削除

---

## 実行方法

### 1. APIサーバー起動

```bash
uvicorn accountbook_api:app --reload

 
