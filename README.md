# My First FastAPI App

学習目的で作る、**最小構成の FastAPI プロジェクト**です。  
Python / FastAPI / Docker / GitHub Actions / OpenAI API をまとめて体験できます。

## このプロジェクトで学べること

- FastAPI で API を作る
- Docker でローカル実行する
- `.env` で API キーを管理する
- GitHub Actions で自動テストする
- OpenAI API を呼び出す

## ディレクトリ構成

```bash
.
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── config.py
│   ├── main.py
│   └── schemas.py
├── tests/
│   └── test_app.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## アプリの内容

この API には 3 つのエンドポイントがあります。

- `GET /` : 起動確認
- `GET /health` : ヘルスチェック
- `POST /api/notes/generate` : OpenAI API で学習メモを生成

## 1. 事前準備

以下が必要です。

- Docker
- Docker Compose
- OpenAI API キー

## 2. 環境変数を準備する

`.env.example` をコピーして `.env` を作成します。

```bash
cp .env.example .env
```

`.env` を開いて、自分の API キーを設定してください。

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

## 3. Docker で起動する

```bash
docker compose up --build
```

起動したら以下にアクセスします。

- アプリ: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## 4. API を試す

### 起動確認

```bash
curl http://localhost:8000/
```

### ヘルスチェック

```bash
curl http://localhost:8000/health
```

### メモ生成

```bash
curl -X POST http://localhost:8000/api/notes/generate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "FastAPIの基本",
    "audience": "Python初心者",
    "tone": "やさしく",
    "bullets": 3
  }'
```

## 5. ローカルでテストする

Docker を使わずに試したい場合です。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

テストの実行:

```bash
pytest
```

## GitHub Actions

`.github/workflows/ci.yml` では、以下を自動実行します。

- Python 3.11 をセットアップ
- 依存関係をインストール
- `pytest` を実行

GitHub に push すると、CI の基本的な流れを学べます。

## Dockerfile のポイント

- `python:3.11-slim` を使って軽量化
- `requirements.txt` を先にコピーしてビルドを効率化
- `uvicorn` で FastAPI を起動

## 初心者向けの次の一歩

- 生成したメモをファイル保存する
- SQLite を追加する
- フロントエンドを追加する
- GitHub Actions で lint も実行する
- エラーハンドリングを改善する

## 補足

この構成は、**まず動かすことを優先した最小構成**です。  
本番運用では以下も検討してください。

- 認証
- ログ出力
- 入力バリデーションの強化
- レート制限
- 監視
