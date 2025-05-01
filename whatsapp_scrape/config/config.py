# WhatsApp Web settings
WHATSAPP_URL = "https://web.whatsapp.com/"
WEBDRIVER_PATH = None  

# XPath/CSS selectors
SEARCH_BOX_XPATH = '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]'
CHAT_LIST_XPATH = '//*[@id="pane-side"]/div[1]/div/div'  # Chat list items
MESSAGE_CONTAINER_XPATH = '//div[contains(@class, "message-in")]'  # Incoming messages
MESSAGE_TEXT_XPATH = './/div[contains(@class, "copyable-text")]'  # Message text
MESSAGE_BOX_XPATH = '//div[@title="Type a message"]'

# Groq LLM settings
GROQ_MODEL = "deepseek-r1-distill-llama-70b"  
TEMPERATURE = 0.6
MAX_COMPLETION_TOKENS = 4096
TOP_P = 0.95