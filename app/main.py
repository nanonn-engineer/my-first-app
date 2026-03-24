from fastapi import FastAPI, HTTPException
from openai import OpenAI

from app.config import settings
from app.schemas import NoteRequest, NoteResponse

app = FastAPI(
    title="My First FastAPI App",
    description="FastAPI + Docker + GitHub Actions + OpenAI API の最小構成サンプル",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "FastAPI sample is running.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/notes/generate", response_model=NoteResponse)
def generate_note(payload: NoteRequest) -> NoteResponse:
    if not settings.openai_api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY が未設定です。.env を作成してください。",
        )

    client = OpenAI(api_key=settings.openai_api_key)

    prompt = f"""
以下の条件で、学習用の短いメモを日本語で作成してください。

テーマ: {payload.topic}
想定読者: {payload.audience}
文体: {payload.tone}
箇条書き数: {payload.bullets}

要件:
- 最初に1文で概要を書く
- その後に箇条書きで要点を書く
- 最後に1つだけ次の学習アクションを書く
""".strip()

    response = client.responses.create(
        model=settings.openai_model,
        input=prompt,
    )

    return NoteResponse(
        topic=payload.topic,
        model=settings.openai_model,
        note=response.output_text,
    )
