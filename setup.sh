
python -m textblob.download_corpora
```

Click **Commit Changes** ✅

---

## Then Reboot Your App
1. Go to your Streamlit app link
2. Click **Manage App** at bottom right corner
3. Click **Reboot**
4. Wait 2-3 minutes

---

## If That Still Doesn't Work
Try changing your **requirements.txt** to this exact version:
```
streamlit==1.32.0
textblob==0.17.1
nltk==3.8.1
