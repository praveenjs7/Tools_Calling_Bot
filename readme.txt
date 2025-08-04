# Agentic AI – Tool-Calling Chatbot

## Overview
This project implements a chatbot that can:
- Perform mathematical calculations
- Retrieve current time for a given timezone
- Perform simple web searches

The chatbot uses OpenAI's GPT model and dynamically calls external tools when needed.

---

## Features
- **Calculator Tool** – safely evaluates math expressions
- **Current Time Tool** – fetches current time for specified timezones
- **Web Search Tool** – fetches basic search results using DuckDuckGo
- Handles single and multiple tool calls per user query

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- OpenAI account with API key

### Installation
1. Clone or download the repository:
   ```bash
   git clone https://github.com/praveenjs7/Agentic-AI.git
   cd Agentic-AI
   ```
2. Install required packages:
   ```bash
   pip install openai requests pytz
   ```
3. Add your OpenAI API key:
   - Open `config.py` and paste your API key:
     ```python
     OPENAI_API_KEY = "your-key-here"
     ```

### Running the Bot
```bash
python main.py
```

---

## Example Queries
- `What's 15% of 847?`
- `Calculate the square root of 144`
- `What time is it in Tokyo?`
- `Search for AI`
- `Show me the time in London and Paris`

---

## Project Structure
```
Agentic AI/
├── main.py        # Chat loop + tool calling logic
├── tools.py       # Calculator, time, and web search tools
├── config.py      # API key and model settings
├── README.md      # Setup and usage instructions
```

---

## Notes
- Ensure the OpenAI API key is valid and has access to GPT-4 or GPT-4o-mini.
- Web search tool returns limited results (DuckDuckGo API restriction).
- Project is for learning/demo purposes only.

---

## Author
Praveen Jagadishan
