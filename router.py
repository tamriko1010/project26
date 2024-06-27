from typing import Annotated
from fastapi import APIRouter, Depends
from repository import RecordRepository
from schemas import Record, RecordAdd, RecordId


router = APIRouter(
   prefix="/records",
   tags=["Путевые заметки"],
)

@router.post("")
async def add_record(record: Annotated[RecordAdd, Depends()],) -> RecordId:
   record_id = await RecordRepository.add_one(record)
   return {"ok": True, "record_id": record_id}

@router.get("")
async def get_records() -> list[Record]:
   records = await RecordRepository.find_all()
   return records
