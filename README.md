# Youtube Downloader

A simple and efficient YouTube downloader built with Python. This project allows users to download videos from YouTube in various formats and resolutions directly to their local machine.

## Features

- Download YouTube videos using a URL
- Support for multiple video resolutions
- Download audio-only files (MP3)
- User-friendly command-line interface
- Supports batch downloads
- Lightweight and fast

## Technologies Used

- **Python**: Core programming language
- **pytube**: Library for downloading YouTube videos
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prathameshatkare/Youtube-downloader.git
   cd Youtube-downloader
   ```

2. **Install dependencies:**
   Make sure you have Python 3.x installed.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the downloader from the command line:

```bash
python downloader.py
```

You will be prompted to enter the YouTube video URL and select the desired format and resolution.

### Example

```bash
$ python downloader.py
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Select format:
1. Video (MP4)
2. Audio (MP3)
Your choice: 1
Select resolution:
1. 1080p
2. 720p
3. 480p
Your choice: 2
Downloading...
Download complete!
```

## Configuration

- You can adjust output directories and default settings in the `config.py` file.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is intended for educational purposes only. Please respect YouTube's Terms of Service and copyright laws when downloading content.

## Author

Made with ❤️ by [prathameshatkare](https://github.com/prathameshatkare)
