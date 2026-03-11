import time
import os
from concurrent.futures.thread import ThreadPoolExecutor

from dotenv import find_dotenv, load_dotenv

from src.bot.application.extractors import Extractor
from unstract.llmwhisperer import LLMWhispererClientV2


class PDFMmanager(Extractor):
    def extract_pdf_table(self, files) -> list:
        def __init__():
            self.client = None

        env_path = find_dotenv()
        load_dotenv(env_path)
        API_KEY: str | None = os.getenv("UNSTRACT_KEY")
        if API_KEY is None:
            return ""
        self.client = LLMWhispererClientV2(base_url='https://llmwhisperer-api.us-central.unstract.com/api/v2',
                                  api_key= API_KEY)

        print("starting extraction for all files")
        with ThreadPoolExecutor (max_workers=10) as executor:
            results = list(executor.map(self.file_process, files))
        print("Successful extraction for all threads")

        return results


    def file_process(self, file)->str:
        file.seek(0)
        result = self.client.whisper(stream=file)

        while True:
            status = self.client.whisper_status(whisper_hash=result['whisper_hash'])
            if status['status'] == 'processed':
                resultx = self.client.whisper_retrieve(
                        whisper_hash=result['whisper_hash']
                    )
                break
            time.sleep(1)

        extract_text = resultx['extraction']['result_text']

        return extract_text
