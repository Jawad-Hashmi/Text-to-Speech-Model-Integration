# TTS Generator

A simple Python-based text-to-speech generator that converts a long script into audio files using the OpenAI Speech API.

This project is designed to:
- read text from an input file
- split large text into safe API-sized chunks
- generate speech audio for each chunk
- save all output files in a timestamped folder

It is useful for creating narration, promotional voiceovers, and long-form spoken content such as the Acadimyst demo script.

---

## Features

- Uses OpenAI TTS API
- Automatically splits long text into chunks
- Saves output as multiple audio parts
- Creates a new output folder for every run
- Clean modular structure
- Easy to configure with `.env`

---

## Project Structure

```bash
project/
│
├── app/
│   ├── config.py
│   ├── file_utils.py
│   ├── text_utils.py
│   └── tts_service.py
│
├── input/
│   └── script.txt
│
├── output/
│   └── FolderName_YYYYMMDD_HHMMSS/
│       ├── part_01.mp3
│       ├── part_02.mp3
│       └── ...
│
├── main.py
├── .env
└── README.md
```


## How It Works
Loads the text from input/script.txt
Normalizes and splits the text into smaller chunks
Sends each chunk to OpenAI TTS API
Generates audio files one by one
Saves them inside a timestamped folder under output/


## Requirements
Python 3.10+
OpenAI API key
Required Python packages:
openai
python-dotenv

## Future Improvements

### Possible enhancements:

merge all audio chunks into one final file
support multiple voices
add CLI arguments
allow custom input/output paths
add retry handling for API failures
generate subtitles/transcripts alongside audio
create a web UI or desktop app
License

This project is available for personal and commercial use based on your needs.
You can add your preferred license here, such as MIT.

Author
Jawad Mehmood