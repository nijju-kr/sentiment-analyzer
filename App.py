import streamlit as st

st.title("🤖 AI Sentiment Analyzer")
st.subheader("Type any sentence and AI will analyze it!")

# Built-in word lists - no external library needed!
positive_words = ["love","great","awesome","happy","excellent","good",
"amazing","wonderful","fantastic","best","joy","beautiful","nice",
"superb","brilliant","excited","proud","perfect","glad","enjoy"]

negative_words = ["hate","bad","terrible","awful","worst","sad","poor",
"horrible","ugly","boring","angry","disgusting","painful","stupid",
"useless","annoying","wrong","fail","broken","difficult"]

text = st.text_area("Enter your sentence here:")

if st.button("Analyze Sentiment"):
    if text == "":
        st.warning("⚠️ Please enter a sentence first!")
    else:
        words = text.lower().split()
        pos = sum(1 for w in words if w in positive_words)
        neg = sum(1 for w in words if w in negative_words)
        score = (pos - neg) / max(len(words), 1)

        if pos > neg:
            st.success("✅ Positive Sentence!")
        elif neg > pos:
            st.error("❌ Negative Sentence!")
        else:
            st.info("😐 Neutral Sentence!")

        st.write(f"**Positive words found:** {pos}")
        st.write(f"**Negative words found:** {neg}")
        st.write(f"**Confidence Score:** {round(score, 2)}")
```

---

## Also Update requirements.txt to ONLY this:
```
streamlit
