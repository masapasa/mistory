import logging
import streamlit as st
from constants import StorySize, story_size_mapper

from services import (
    summarizeStory,
    createStories,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def count_words(text):
    # Remove punctuation from the text and count words
    text = text.lower()
    text = "".join(char for char in text if char.isalnum() or char.isspace())
    word_count = len(text.split())
    return word_count

def write():
    logger.info("Received request for /write endpoint")
    try:
        promptText = st.text_input("Enter prompt text")
        samples = st.number_input("Enter number of samples", value=3)
        temperature = st.slider("Select temperature", min_value=0.1, max_value=1.0, value=0.7, step=0.1)
        story_size = st.selectbox("Select story size", options=[1, 2, 3], format_func=lambda x: story_size_mapper[x].name)
        parameter3 = st.text_input("Enter parameter3")
        switch1 = st.checkbox("Switch 1")
        tone = st.text_input("Enter tone")
        audience = st.text_input("Enter audience")
        genre = st.text_input("Enter genre")
        language = st.text_input("Enter language")

        stories = createStories(
            promptText,
            samples,
            temperature,
            number_words=int(story_size_mapper[story_size].value * 0.6),
            genre=genre,
            language=language,
        )

        stories_with_summaries = []
        for story in stories:
            summary = summarizeStory(
                story, int(StorySize.SUMMARY.value * 0.6), language
            )
            if language != "english":
                summary_en = summarizeStory(
                    story, int(StorySize.SUMMARY.value * 0.6), "english"
                )
                image = generateStoryImage(summary_en)
            else:
                image = generateStoryImage(summary)
            stories_with_summaries.append(
                {
                    "story": story,
                    "summary": summary,
                    "total_words": count_words(story),
                    "promptText": promptText,
                    "samples": samples,
                    "temperature": temperature * 10,
                    "story_size": story_size,
                    "parameter3": parameter3,
                    "switch1": switch1,
                    "tone": tone,
                    "audience": audience,
                    "genre": genre,
                    "image": image,
                    "language": language,
                }
            )

        st.json({"data": {"stories": stories_with_summaries}})
    except Exception as e:
        logger.error(f"Error processing the request for /write: {e}")
        st.json({"error": "Error processing the request for /write"})

if __name__ == "__main__":
    write()