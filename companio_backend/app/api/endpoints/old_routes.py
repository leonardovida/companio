# from fastapi import APIRouter

# from app.schemas.requests import NoteIn
# from app.schemas.responses import Note

# router = APIRouter()


# @router.get("/notes/", response_model=list[Note])
# async def read_notes():
#     query = notes.select()
#     return await database.fetch_all(query)


# @app.post("/notes/", response_model=Note)
# async def create_note(note: NoteIn):
#     print(note)
#     query = notes.insert().values(text=note.text, completed=note.completed)
#     last_record_id = await database.execute(query)
#     return {**note.dict(), "id": last_record_id}
