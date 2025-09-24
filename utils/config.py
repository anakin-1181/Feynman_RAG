from dotenv import load_dotenv
import  os

load_dotenv()

api_key = os.getenv('OPENAI_KEY')

print(api_key)