import streamlit as st

st.title("🤖 AI Sentiment Analyzer")
st.subheader("Type any sentence and AI will analyze it!")

positive_words = ["love","great","awesome","happy","excellent","good",
"amazing","wonderful","fantastic","best","joy","beautiful","nice",
"superb","brilliant","excited","proud","perfect","glad","enjoy",
"fun","pleased","grateful","delighted","cheerful","positive","smile",
"hope","kind","sweet","cool","impressive","fabulous","outstanding"]

negative_words = ["hate","bad","terrible","awful","worst","sad","poor",
"horrible","ugly","boring","angry","disgusting","painful","stupid",
"useless","annoying","wrong","fail","broken","difficult","miserable",
"depressed","upset","frustrated","negative","awful","dull","harsh",
"cruel","fear","stress","tired","exhausted","worried","regret"]

text = st.text_area("Enter your sentence here:")

if st.button("Analyze Sentiment"):
    if text == "":
        st.warning("⚠️ Please enter a sentence first!")
    else:
        words = text.lower().split()
        pos = sum(1 for w in words if w in positive_words)
        neg = sum(1 for w in words if w in negative_words)

        # Find which words were detected
        found_pos = [w for w in words if w in positive_words]
        found_neg = [w for w in words if w in negative_words]
        unknown = [w for w in words if w not in positive_words 
                   and w not in negative_words]

        if pos > neg:
            st.success("✅ Positive Sentence!")
        elif neg > pos:
            st.error("❌ Negative Sentence!")
        else:
            st.info("😐 Neutral / Unknown Sentence!")
            if unknown:
                st.warning(f"⚠️ These words were not recognized: "
                          f"{', '.join(unknown)}")

        # Show breakdown
        if found_pos:
            st.write(f"**Positive words detected:** {', '.join(found_pos)}")
        if found_neg:
            st.write(f"**Negative words detected:** {', '.join(found_neg)}")
        if unknown:
            st.write(f"**Unrecognized words:** {', '.join(unknown)}")
