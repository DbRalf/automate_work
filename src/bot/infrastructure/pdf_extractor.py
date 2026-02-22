import time
import os
from dotenv import find_dotenv, load_dotenv

from src.bot.application.extractors import Extractor
from unstract.llmwhisperer import LLMWhispererClientV2


class PDFMmanager(Extractor):
    def extract_pdf_table(self, file) -> str:

        env_path = find_dotenv()
        load_dotenv(env_path)
        API_KEY: str | None = os.getenv("UNSTRACT_KEY")
        if API_KEY is None:
            return ""

        client = LLMWhispererClientV2(base_url='https://llmwhisperer-api.us-central.unstract.com/api/v2',
                                      api_key= API_KEY)
        result = client.whisper(stream=file)

        print("Starting pdf extraction.")
        while True:
            status = client.whisper_status(whisper_hash=result['whisper_hash'])
            if status['status'] == 'processed':
                resultx = client.whisper_retrieve(
                    whisper_hash=result['whisper_hash']
                )
                break
            time.sleep(5)

        extract_text = resultx['extraction']['result_text']
        print("Successful extraction")

        return extract_text



