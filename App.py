from textblob import TextBlob
import streamlit as st

# Page title
st.title("🤖 AI Sentiment Analyzer")
st.subheader("Type any sentence and AI will analyze it!")

# Text input box
text = st.text_area("Enter your sentence here:")

# Analyze button
if st.button("Analyze Sentiment"):
    
    if text == "":
        st.warning("⚠️ Please enter a sentence first!")
    
    else:
        blob = TextBlob(text)
        score = blob.sentiment.polarity

        if score > 0:
            st.success("✅ Positive Sentence!")
        elif score < 0:
            st.error("❌ Negative Sentence!")
        else:
            st.info("😐 Neutral Sentence!")

        st.write(f"**Confidence Score:** {score}")