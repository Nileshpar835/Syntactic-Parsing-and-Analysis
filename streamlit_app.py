import spacy
import streamlit as st
import spacy_streamlit

nlp = spacy.load("en_core_web_sm")

st.title("POS Tagger + Syntactic Parsing")

text = st.text_input("Enter a sentence to analyze:")

if text:
    doc = nlp(text)

    st.subheader("Part-of-Speech Tags")
    for token in doc:
        st.write(f"{token.text} → {token.pos_}")

    st.subheader("Syntactic Parsing")
    spacy_streamlit.visualize_parser(doc)
