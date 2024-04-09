from gtts import gTTS
from io import BytesIO


def to_voice(msg, language='ru'):
    tts = gTTS(text=msg, lang=language)
    voice_msg = BytesIO()
    tts.write_to_fp(voice_msg)
    voice_msg.seek(0)
    return voice_msg
