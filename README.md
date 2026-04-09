# Mood Music Player

A simple desktop GUI application built with Python, Tkinter, and Pygame. Select your mood and play corresponding music! Black-themed interface with colorful mood buttons.

## Features
- **Mood-based Playback**: Buttons for Happy (green), Sad (blue), Angry (orange), Neutral (gray).
- **Stop Button**: Red button to stop music.
- **Status Updates**: Real-time feedback on playback.
- **Custom Styling**: Algerian font title, Times New Roman buttons, black background, yellow title. hello how are you 

## Demo
```
+---------------------------+
|     Mood Music Player     |
|                           |
|      [Happy]              |
|       [Sad]               |
|     [Angry]               |
|     [Neutral]             |
|     [Stop Music]          |
|                           |
| Playing happy song        |
+---------------------------+
```

## Requirements
- Python 3.x
- Pygame: `pip install pygame`

## Installation
1. Download/place the project files.
2. Ensure MP3 files (`happy.mp3`, `sad.mp3`, `angry.mp3`, `neutral.mp3`) are in the root directory.
3. Install dependencies: `pip install pygame`

## Usage
Run the app:
```
python MoodMusicPlayer/main.py
```
Click a mood button to play music. Use Stop to halt.

## Troubleshooting
- MP3 paths are relative to current working directory (root).
- If audio doesn't play, check pygame init and file permissions.
- sample.txt is a sample file, not used.

## License
MIT License - feel free to use and modify.

