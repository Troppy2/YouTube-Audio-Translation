# YouTube Audio Translator

## Overview

**YouTube Audio Translator** is a web-based application designed to reduce language barriers when consuming YouTube content. The project aims to translate spoken audio from YouTube videos into a target language, enabling users to understand valuable information that would otherwise be inaccessible due to language differences.

This project was developed as a personal learning initiative in full-stack web development, API integration, and backend system design. While the application is not fully complete, it represents a significant hands-on exploration of real-world engineering challenges.

## Motivation

When watching YouTube videos in unfamiliar languages, users often abandon potentially useful content. This project was created to address that problem by:

- Extracting spoken content from YouTube videos
- Translating that content into a user-selected language
- Converting translated text back into audio for playback

The long-term vision is to provide a seamless way to consume global content regardless of language.

## Features (Current)

- User input for YouTube video URLs
- Backend processing using Flask
- Integration with multiple Google APIs:
  - YouTube Transcript API (speech-to-text)
  - Google Translate API (language translation)
  - Google Text-to-Speech API (translated audio output)
- Frontend-to-backend communication via HTTP requests

## Technology Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- Flask

**APIs**
- YouTube Transcript API
- Google Translate API
- Google Text-to-Speech API

## System Architecture

1. User submits a YouTube URL via the frontend.
2. The backend extracts the video ID from the URL.
3. The YouTube Transcript API attempts to fetch the video transcript.
4. The transcript is translated into the target language.
5. The translated text is converted into audio using text-to-speech.
6. The output is returned to the frontend for playback.

## Known Issues & Limitations

- **Video ID extraction bug**  
  The `set_videoid` function intermittently fails to correctly extract the YouTube video ID from user-submitted URLs. This causes transcript retrieval to fail and results in an error stating that the transcript is unavailable.

- **Transcript availability**  
  Some videos do not have transcripts enabled or accessible via the API, which limits functionality.

- **Video download bug**  
  Currently, the video is not actually downloaded for processing. This can cause failures when trying to generate the transcript or audio output.

- **Incomplete frontend logic**  
  Error handling and user feedback on the frontend are minimal and need improvement.

## Lessons Learned

- Backend development with Flask and API orchestration
- Debugging issues related to user input and data extraction
- Understanding API limitations and error states
- Full-stack application flow from frontend to backend
- Handling multimedia data and asynchronous workflows

This project significantly strengthened my understanding of system design and reinforced my interest in building accessibility-focused tools.

## Future Improvements

- Robust YouTube URL parsing (supporting all URL formats)
- Improve video download and transcript processing
- Enhanced error handling and user feedback
- Support for multiple target languages
- Caching translated transcripts to reduce API calls
- Improved frontend UI/UX
- Scalable backend architecture
- Optional subtitle-based translation alongside audio

## Project Status

**In Progress (Paused)**  
Development is currently paused while foundational backend and JavaScript skills are being strengthened. The project is intended to be revisited and expanded in the future.

## Author

**Inah James**  
Personal Project — July 2025 to Present
