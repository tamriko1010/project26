from sqlalchemy import select
from database import RecordOrm, new_session
from schemas import RecordAdd, Record

class RecordRepository:
    @classmethod
    async def add_one(cls, data: RecordAdd) -> int:
        async with new_session() as session:
            record_dict = data.model_dump()
            record = RecordOrm(**record_dict)
            session.add(record)
            await session.flush()
            await session.commit()
            return record.id

    @classmethod
    async def find_all(cls) -> list[Record]:
        async with new_session() as session:
            query = select(RecordOrm)
            result = await session.execute(query)
            record_models = result.scalars().all()
            records = [Record.model_validate(record_model) for record_model in record_models]
            return records
