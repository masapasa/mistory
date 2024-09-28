import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# OpenAI API key
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MISTRAL_MODEL = "mistral-large-latest"

# Define story sizes
# Size in tokens: 100 tokens ~= 75 words
from enum import Enum
class StorySize(Enum):
    HAIKU = 10
    SUMMARY = 30
    VERY_SHORT = 200
    SHORT_STORY = 350
    FULL_STORY = 500

story_size_mapper = {
    0: StorySize.HAIKU,
    1: StorySize.SUMMARY,
    2: StorySize.VERY_SHORT,
    3: StorySize.SHORT_STORY,
    4: StorySize.FULL_STORY,
}