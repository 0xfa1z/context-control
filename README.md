# Context Control

A simple web application that gives you full control over the LLM context window. Edit the context in real-time for each interaction with the LLM.

## Features

- Real-time context editing
- Clean, modern UI
- Docker-based deployment
- OpenAI GPT-3.5 Turbo integration

## Setup

1. Clone this repository
2. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and add your OpenAI API key

## Running the Application

Simply run:
```bash
docker compose up
```

The application will be available at `http://localhost:8000`

## Usage

1. Enter your desired context in the left panel
2. Type your message in the chat input
3. The LLM will respond using your specified context
4. You can modify the context at any time between messages

## Development

The application uses:
- FastAPI for the backend
- TailwindCSS for styling
- Docker for containerization 