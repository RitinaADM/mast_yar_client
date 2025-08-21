from pydantic import BaseModel, Field

class Record(BaseModel):
    text: str = Field(..., min_length=1)
    date: str
    time: str
    click_number: int = Field(..., ge=0)

class ResponseRecord(Record):
    id: int