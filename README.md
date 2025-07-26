# YouTube Downloader - `youtube` Module

This folder contains the core logic for downloading videos from YouTube as part of the [Youtube-downloader](https://github.com/prathameshatkare/Youtube-downloader) project.

## Overview

The `youtube` module is responsible for handling YouTube video downloads. It provides functionalities to fetch video metadata, select formats, and save videos locally. This module is designed to be integrated with the main Youtube-downloader application, and can also be used independently as a library for YouTube video downloading tasks.

## Features

- Download videos from YouTube by URL
- Support for multiple formats and resolutions
- Fetch video metadata (title, author, length, etc.)
- Progress tracking and error handling

## Folder Structure

```
youtube/
├── __init__.py
├── downloader.py
├── utils.py
└── ...
```
- `downloader.py`: Main logic for downloading YouTube videos.
- `utils.py`: Utility functions used for processing YouTube URLs, formats, and metadata.
- `__init__.py`: Makes the folder a Python package.

## Usage

### As Part of the Main Application

The main application imports and uses the `youtube` module for all YouTube-related download operations.

### As a Library

You can use this module in your own Python project:
```python
from youtube.downloader import download_video

url = "https://www.youtube.com/watch?v=example"
download_video(url, output_path="downloads/")
```

## Requirements

- Python 3.7+
- [pytube](https://github.com/pytube/pytube) or similar package for handling YouTube streams

Install dependencies:
```bash
pip install pytube
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Author

- [Prathamesh Atkare](https://github.com/prathameshatkare)

---

Feel free to open issues or pull requests for improvements!
