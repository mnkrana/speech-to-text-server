def speech():
    from google.cloud import speech
    import io

    # Instantiates a client
    client = speech.SpeechClient()

    with io.open("flac.flac", "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    import datetime
    now = datetime.datetime.now()
    print(now)

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

    now = datetime.datetime.now()
    print(now)

    return result.alternatives[0].transcript


def speech_post(content):
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    import datetime
    now = datetime.datetime.now()
    print(now)

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

    now = datetime.datetime.now()
    print(now)

    return result.alternatives[0].transcript
