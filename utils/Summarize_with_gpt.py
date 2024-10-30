import os
import openai
from dotenv import load_dotenv
class SummarizeWithGPT:
   def __init__(self):
        # Load environment variables
        load_dotenv()
        # Initialize environment variables
        self.api_type = os.getenv('OPEN_AI_TYPE')
        self.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')  # API base URL
        self.api_version = "2024-06-01"
        self.api_key = os.getenv('OPENAI_API_KEY')  # API key
        self.deployment_name = os.getenv('OPEN_AI_DEPLOYMENT_NAME')  # Deployment name

        # Set OpenAI API credentials
        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        openai.api_key = self.api_key

        # Initialize the AzureOpenAI client
        self.client = openai.AzureOpenAI(api_key=self.api_key,api_version = self.api_version)
   def summarize(self, content):
        response = self.client.chat.completions.create(
                    model='gpt-4o-mini-model',
                    messages=[
                        {"role": "system", "content": "Your task is to summarize the following content in detail while adding the url of the sources and numbers, dates and prices are important"},
                        {"role": "user", "content": content}
                    ],
                    max_tokens=4096,
                    temperature=0,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
        answer = response.choices[0].message.content
        return answer