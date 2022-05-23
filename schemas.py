from fastapi import Form, File, UploadFile
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class AwesomeForm(BaseModel):
    name: str
    category: str
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        name: str = Form(...),
        category: str = Form(...),
        file: UploadFile = File(...)
    ):
        return cls(
            name=name,
            category=category,
            file=file
        )
