from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(
    pydantic_object=Movie
)

model = ChatMistralAI(
    model="mistral-small-2506"
)

prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
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

st.set_page_config(
    page_title="🎬 Movie Extractor",
    page_icon="🎬"
)

st.title("🎬 Movie Information Extractor")

movie_para = st.text_area(
    "Enter Movie Paragraph",
    height=250
)

if st.button("🔍 Extract Movie Information", use_container_width=True):

    if movie_para.strip():

        with st.spinner("Extracting information..."):

            final_prompt = prompt_template.invoke(
                {
                    "movie_paragraph": movie_para,
                    "format_instructions": parser.get_format_instructions()
                }
            )

            response = model.invoke(final_prompt)

            movie_data = parser.parse(
                response.content
            )

        st.success("Extraction Complete ✅")

        st.divider()

        st.subheader("🎬 Movie Details")

        st.write("**Title:**", movie_data.title)
        st.write("**Release Year:**", movie_data.release_year)
        st.write("**Director:**", movie_data.director)
        st.write("**Rating:**", movie_data.rating)

        st.write("**Genres:**")
        st.write(", ".join(movie_data.genre))

        st.write("**Cast:**")
        st.write(", ".join(movie_data.cast))

        st.subheader("📝 Summary")

        st.info(movie_data.summary)

        with st.expander("📋 View Raw JSON Output"):
            st.json(movie_data.model_dump())

    else:
        st.warning("Please enter a movie paragraph.")