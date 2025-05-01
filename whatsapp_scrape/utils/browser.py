from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WhatsAppBot:
    def __init__(self, webdriver_path=None):
        """Initialize Chrome WebDriver."""
        options = webdriver.ChromeOptions()
        if webdriver_path:
            self.driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 30)

    def open_whatsapp(self, url):
        """Open WhatsApp Web and wait for QR code scan."""
        self.driver.get(url)
        print("Please scan the QR code to log in.")
        input("Press Enter after scanning the QR code...")

    def get_unread_chats(self, chat_list_xpath):
        """Get list of unread chats."""
        try:
            chats = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, chat_list_xpath))
            )
            return chats
        except Exception as e:
            print(f"Error finding chats: {e}")
            return []

    def extract_messages(self, chat, message_container_xpath, message_text_xpath):
        """Extract incoming messages from a chat."""
        try:
            # Click chat to open it
            chat.click()
            time.sleep(2)  

            # Find incoming messages
            messages = self.driver.find_elements(By.XPATH, message_container_xpath)
            extracted_messages = []
            for msg in messages[-5:]:  # Limit to last 5 messages
                try:
                    text = msg.find_element(By.XPATH, message_text_xpath).text
                    extracted_messages.append(text)
                except:
                    continue
            return extracted_messages
        except Exception as e:
            print(f"Error extracting messages: {e}")
            return []

    def send_message(self, message, message_box_xpath):
        """Send a message in the current chat."""
        try:
            message_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, message_box_xpath))
            )
            message_box.click()
            message_box.send_keys(message)
            message_box.send_keys(Keys.ENTER)
            time.sleep(1)  # Ensure message is sent
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error sending message: {e}")

    def close_browser(self):
        """Close the browser."""
        self.driver.quit()