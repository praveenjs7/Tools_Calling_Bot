import os

# Load API keys from environment variables
OPENAI_API_KEY = "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"
#ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Default model to use (OpenAI GPT model)
DEFAULT_MODEL = "gpt-4o-mini"

# Warning if the key is missing
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY is not set.")
    print("Set it using:")
    print("  export OPENAI_API_KEY='your-key-here'  (Mac/Linux)")
    print("  setx OPENAI_API_KEY \"your-key-here\"   (Windows)")

if __name__ == "__main__":
    print("Your API Key is:", OPENAI_API_KEY)
