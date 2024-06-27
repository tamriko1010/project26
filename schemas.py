from pydantic import BaseModel, ConfigDict

class RecordAdd(BaseModel):
    name: str
    description: str | None = None

class Record(RecordAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)



class RecordId(BaseModel):
    ok: bool = True
    record_id: int
