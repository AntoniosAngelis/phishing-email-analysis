# Phishing Email Analysis

A simple Python tool that analyzes email content to detect potential phishing attempts using keyword and pattern recognition.

## Features
- Detects suspicious keywords (e.g. "urgent", "verify your account")
- Identifies links in emails
- Flags emails written in ALL CAPS
- Provides basic phishing warnings

## How it works
The script scans the input email text and checks for:
- Common phishing keywords
- Presence of URLs (http/https)
- Suspicious formatting (e.g. all uppercase text)

## Usage

Run the script:

```bash
python3 analyzer.py
