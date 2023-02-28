from fastapi import Body, FastAPI
from pydantic import (
    BaseModel,
    Field
)
import flac
import wav
import base64

app = FastAPI()


@app.get("/flac")
async def flac_test():
    return flac.speech()


@app.get("/wav")
async def wav_test():
    return wav.speech()


class AudioSchema(BaseModel):
    audio_data: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "audio_data": "Mona Lisa"
            }
        }


@app.put("/wav_post")
async def wav_post(audio_data: AudioSchema = Body(...)):
    bytes = base64.b64decode(audio_data.audio_data)
    return wav.speech_post(bytes)


@app.put("/flac_post")
async def flac_post(audio_data: AudioSchema = Body(...)):
    bytes = base64.b64decode(audio_data.audio_data)
    return flac.speech_post(bytes)
