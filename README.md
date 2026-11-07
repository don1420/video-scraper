# Video Scraper

A simple Streamlit application that extracts video URLs from a playlist page and generates ready-to-use **FFmpeg** commands for downloading the videos.

## Features

* Enter a playlist URL.
* Automatically extract all video pages using Selenium.
* Parse video sources with BeautifulSoup.
* Generate FFmpeg commands for each video.
* Display progress while processing.
* Copy the generated commands directly from the application.

## Project Structure

```text
project/
│
├── app.py          # Streamlit user interface
├── scraper.py      # Selenium scraping logic
├── ffmpeg.py       # FFmpeg command generation
├── config.py       # CSS selectors and constants
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10+
* Google Chrome
* ChromeDriver compatible with your Chrome version

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

### Windows

Open PowerShell or Command Prompt and run:

```bash
python --version
```

If the python command is not recognized, try:

```bash
py --version
```

If py works but python does not, Python is installed, but its executable may not be configured in the Windows PATH environment variable.
You can use py instead of python in the commands below.
If Python is not installed, download it from:
https://www.python.org/downloads/
During installation, enable Add Python to PATH.

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m streamlit run app.py
```

Then open the local URL displayed in the terminal (typically http://localhost:8501).

## How It Works

1. Open the provided playlist URL.
2. Scroll to the playlist section.
3. Extract all `data-file` URLs.
4. Visit each video page.
5. Find the `<video>` element.
6. Extract the `src` attribute.
7. Generate an FFmpeg command for each video.

Example output:

```bash
ffmpeg -i "https://example.com/video1.mp4" -c copy -bsf:a aac_adtstoasc 1.mp4;
ffmpeg -i "https://example.com/video2.mp4" -c copy -bsf:a aac_adtstoasc 2.mp4;
```

## Technologies

* Streamlit
* Selenium
* BeautifulSoup4
* Chrome WebDriver
* FFmpeg

## Notes

* The target website must allow access through Selenium.
* ChromeDriver must match your installed version of Google Chrome.
* The application currently runs Chrome in headless mode.

## License

This project is provided for educational and personal use. Ensure you have permission to download and use any content processed with this tool.
