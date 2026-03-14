from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st

st.title("🤖 AI Sentiment Analyzer")
st.subheader("Type any sentence and AI will analyze it!")

text = st.text_area("Enter your sentence here:")

if st.button("Analyze Sentiment"):
    if text == "":
        st.warning("⚠️ Please enter a sentence first!")
    else:
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)
        compound = score['compound']

        if compound >= 0.05:
            st.success("✅ Positive Sentence!")
        elif compound <= -0.05:
            st.error("❌ Negative Sentence!")
        else:
            st.info("😐 Neutral Sentence!")

        st.write(f"**Confidence Score:** {compound}")
