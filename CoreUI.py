from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Model
model = ChatMistralAI(model="mistral-small-2506")

# Page Config
st.set_page_config(
    page_title="🎬 Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Information Extractor")
st.markdown("Paste a movie paragraph and extract structured information.")

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your Task:
Extract all useful structured information from the provided movie paragraph and present it in the exact format below.

Rules:
- Do NOT add explanations.
- Do NOT add extra commentary.
- Follow the exact format.
- If information is missing, write NULL.
- Do NOT guess unknown facts.
- Extract only information explicitly mentioned.
- Keep the summary short (2-3 lines maximum).

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Producer:
Writer:
Main Cast:
Supporting Cast:
Language:
Country:
Runtime:
Production Company:

Plot Summary:

Main Theme:
Sub Theme:

Protagonist:
Antagonist:

Setting:

Conflict:

Climax:

Resolution:

Target Audience:

Emotional Tone:

Awards:

IMDb Rating:

Box Office Collection:

Key Highlights:
- Highlight 1
- Highlight 2
- Highlight 3

Final Summary:
"""
    ),
    (
        "human",
        """
Movie Paragraph:

{movie_paragraph}
"""
    )
])

# Text Area
movie_para = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste movie description here..."
)

# Button
if st.button("🔍 Extract Information"):

    if movie_para.strip():

        with st.spinner("Extracting Information..."):

            final_prompt = prompt_template.invoke(
                {"movie_paragraph": movie_para}
            )

            response = model.invoke(final_prompt)

        st.subheader("📄 Extracted Information")

        st.text_area(
            "Result",
            value=response.content,
            height=500
        )

    else:
        st.warning("Please enter a movie paragraph.")