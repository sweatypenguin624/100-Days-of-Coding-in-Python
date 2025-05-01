from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMClient:
    def __init__(self, model, temperature, max_completion_tokens, top_p):
        """Initialize Groq client."""
        self.client = Groq(api_key="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")
        self.model = model
        self.temperature = temperature
        self.max_completion_tokens = max_completion_tokens
        self.top_p = top_p

    def generate_response(self, messages):
        """Generate a response using Groq API."""
        try:
            # Format messages for Groq API
            # prompt pending
            formatted_messages = [
                {"role": "system", "content": "You are a helpful WhatsApp chatbot."},
                {"role": "user", "content": "\n".join(messages)}
            ]

            # Make API call
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=formatted_messages,
                temperature=self.temperature,
                max_completion_tokens=self.max_completion_tokens,
                top_p=self.top_p,
                stream=True,
                stop=None,
            )

            # Collect response from stream
            response = ""
            for chunk in completion:
                content = chunk.choices[0].delta.content or ""
                response += content

            return response.strip()
        except Exception as e:
            print(f"Error generating Groq response: {e}")
            return "Sorry, I couldn't process that. Try again!"