from pydantic import BaseModel, Field


class NoteRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=100, description="学習したいテーマ")
    audience: str = Field("初心者", min_length=1, max_length=50, description="想定読者")
    tone: str = Field("やさしく", min_length=1, max_length=50, description="文体")
    bullets: int = Field(3, ge=1, le=8, description="箇条書きの数")


class NoteResponse(BaseModel):
    topic: str
    model: str
    note: str
