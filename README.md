# Virtual-Personal-Assistance
Project Report – Voice Assistant (Jarvis)
🔹 Overview

This project is a desktop voice assistant named Jarvis.
It listens to user voice commands through the microphone, processes them, and performs various tasks like searching online, opening apps, sending emails/WhatsApp messages, managing tasks, and giving notifications.
It also responds using text-to-speech (TTS).

🔹 Key Libraries Used

pyttsx3 – Text-to-speech conversion.

speech_recognition – Converts spoken voice input to text.

wikipedia – Fetches summaries from Wikipedia.

webbrowser – Opens websites like Google, YouTube, Stack Overflow.

os – Opens local applications (e.g., VS Code).

smtplib – Sends emails.

plyer.notification – Shows system notifications.

pyautogui – Automates key presses and typing.

pywhatkit – Sends WhatsApp messages.

random – Selects random YouTube music links.

🔹 Features Implemented

Greetings (wishme)

Greets user depending on time of day (Morning, Afternoon, Evening).

Speech Input (takeCommand)

Listens via microphone.

Converts Hindi/English voice to text using Google Speech Recognition.

Wikipedia Search

Fetches 2-sentence summary of any topic.

Google Search & Web Navigation

Opens Google, YouTube, Stack Overflow, or any custom search.

Music Playback

Opens random YouTube music video.

Time Announcement

Speaks current system time.

App Launcher

Opens VS Code or any program by name using pyautogui.

To-do List Management

Add new tasks (new task).

Read saved tasks (read task list).

Show notifications for pending tasks.

Messaging

Sends WhatsApp messages using pywhatkit.

Sends emails with SMTP.

🔹 Workflow

Start program → wishme() greets user.

Continuous loop → listens for commands via takeCommand().

Based on keywords in the command → executes matching function.

Responds with speech feedback using speak().

🔹 Limitations

Email function requires correct Gmail credentials (stored in user_pass.py).

WhatsApp scheduling requires exact time inputs.

No natural conversation handling → relies only on keyword matching.

Currently translation (Hindi → English) is not working because mtranslate is outdated.

🔹 Possible Improvements

Replace mtranslate with deep-translator for robust translation.

Add exit/quit voice command to stop the assistant.

Integrate AI chatbot (like ChatGPT API) for natural conversation.

Add speech-to-Hindi + Hindi TTS for bilingual support.

Save task list in a database (SQLite) instead of plain text.

⚡ In short:
This program is a basic AI-powered desktop assistant that can speak, listen, search, send emails/WhatsApp, manage tasks, and open apps/websites.
