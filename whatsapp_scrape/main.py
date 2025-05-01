from config.config import (
    WHATSAPP_URL, WEBDRIVER_PATH, CHAT_LIST_XPATH, MESSAGE_CONTAINER_XPATH,
    MESSAGE_TEXT_XPATH, MESSAGE_BOX_XPATH, GROQ_MODEL, TEMPERATURE,
    MAX_COMPLETION_TOKENS, TOP_P
)
from utils.browser import WhatsAppBot
from utils.llm import LLMClient
import time

def main():
    """Run the WhatsApp chatbot with Groq LLM."""
    # Initialize bot and LLM client
    bot = WhatsAppBot(webdriver_path=WEBDRIVER_PATH)
    llm = LLMClient(
        model=GROQ_MODEL,
        temperature=TEMPERATURE,
        max_completion_tokens=MAX_COMPLETION_TOKENS,
        top_p=TOP_P
    )

    try:
        # Open WhatsApp Web
        bot.open_whatsapp(WHATSAPP_URL)

        print("Chatbot running. Press Ctrl+C to stop.")
        while True:
            # Get unread or recent chats
            chats = bot.get_unread_chats(CHAT_LIST_XPATH)
            if not chats:
                print("No chats found. Waiting...")
                time.sleep(10)
                continue

            for chat in chats:
                # Extract messages
                messages = bot.extract_messages(chat, MESSAGE_CONTAINER_XPATH, MESSAGE_TEXT_XPATH)
                if messages:
                    print(f"Received messages: {messages}")
                    # Generate response using Groq LLM
                    response = llm.generate_response(messages)
                    print(f"Groq response: {response}")
                    # Send response
                    bot.send_message(response, MESSAGE_BOX_XPATH)

            time.sleep(10)  # Wait before checking again

    except KeyboardInterrupt:
        print("Chatbot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        bot.close_browser()

if __name__ == "__main__":
    main()