import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

st.set_page_config(
    page_title="Spam Mail Detector",
    page_icon="SM",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(59, 130, 246, 0.20), transparent 28%),
                radial-gradient(circle at top right, rgba(16, 185, 129, 0.14), transparent 24%),
                linear-gradient(180deg, #08111f 0%, #0b1220 46%, #0f172a 100%);
            color: #e2e8f0;
        }

        .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
            max-width: 760px;
        }

        .hero {
            background: rgba(15, 23, 42, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.12);
            box-shadow: 0 24px 60px rgba(2, 6, 23, 0.45);
            border-radius: 28px;
            padding: 2rem 2rem 1.5rem;
            backdrop-filter: blur(18px);
        }

        .eyebrow {
            display: inline-block;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(59, 130, 246, 0.14);
            color: #93c5fd;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .hero h1 {
            margin: 0.8rem 0 0.4rem;
            color: #f8fafc;
            font-size: 2.4rem;
            line-height: 1.05;
        }

        .hero p {
            margin: 0;
            color: #cbd5e1;
            font-size: 1rem;
            line-height: 1.6;
        }

        .panel {
            background: rgba(15, 23, 42, 0.72);
            border: 1px solid rgba(148, 163, 184, 0.12);
            border-radius: 24px;
            padding: 1.5rem;
            box-shadow: 0 18px 40px rgba(2, 6, 23, 0.35);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.85rem;
            margin-top: 1rem;
        }

        .feature-card {
            background: linear-gradient(180deg, rgba(30, 41, 59, 0.96), rgba(15, 23, 42, 0.96));
            border: 1px solid rgba(148, 163, 184, 0.12);
            border-radius: 18px;
            padding: 0.95rem;
        }

        .feature-card strong {
            display: block;
            margin-bottom: 0.35rem;
            color: #f8fafc;
        }

        .feature-card span {
            color: #cbd5e1;
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .stTextArea label {
            color: #e2e8f0 !important;
        }

        .stTextArea textarea {
            border-radius: 18px !important;
            border: 1px solid rgba(148, 163, 184, 0.20) !important;
            padding: 1rem !important;
            background: rgba(2, 6, 23, 0.92) !important;
            color: #f8fafc !important;
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
        }

        .stTextArea textarea:focus {
            border-color: rgba(59, 130, 246, 0.78) !important;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.16) !important;
        }

        .stTextArea textarea::placeholder {
            color: #94a3b8 !important;
        }

        .stButton button {
            width: 100%;
            border: none;
            border-radius: 16px;
            padding: 0.9rem 1.25rem;
            background: linear-gradient(135deg, #38bdf8 0%, #2563eb 50%, #4f46e5 100%);
            color: white;
            font-weight: 700;
            letter-spacing: 0.01em;
            box-shadow: 0 14px 28px rgba(37, 99, 235, 0.32);
            transition: transform 160ms ease, box-shadow 160ms ease;
        }

        .stButton button:hover {
            transform: translateY(-1px);
            box-shadow: 0 18px 34px rgba(37, 99, 235, 0.40);
        }

        .result-card {
            margin-top: 1.2rem;
            padding: 1rem 1.1rem;
            border-radius: 18px;
            border: 1px solid rgba(148, 163, 184, 0.14);
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.92), rgba(2, 6, 23, 0.94));
            box-shadow: 0 14px 32px rgba(2, 6, 23, 0.32);
        }

        .result-label {
            margin: 0 0 0.35rem;
            color: #94a3b8;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .result-card h3 {
            margin: 0;
            color: #f8fafc;
            font-size: 1.35rem;
        }

        .result-safe {
            border-left: 4px solid #22c55e;
        }

        .result-spam {
            border-left: 4px solid #f97316;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    res = []

    for x in text:
        if x.isalnum():
            res.append(x)

    text = res[:]
    res.clear()

    for x in text:
        if x not in stop_words and x not in string.punctuation:
            res.append(x)

    text = res[:]
    res.clear()

    for x in text:
        res.append(ps.stem(x))

    return " ".join(res)

st.markdown(
    """
    <div class="hero">
        <span class="eyebrow">Email Security</span>
        <h1>Spam Message Classifier</h1>
        <p>Paste a message below to check whether it looks like spam. The detection logic stays the same; the interface is just cleaner and easier to use.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

left, right = st.columns([1.2, 0.8], gap="large")

submitted = False

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    with st.form("spam_check_form"):
        msg_input = st.text_area(
            "Message",
            placeholder="Paste the message you want to check...",
            height=170,
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Analyze message")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown(
        """
        <div class="panel">
            <div class="feature-grid">
                <div class="feature-card">
                    <strong>Fast checks</strong>
                    <span>Run the model on a single message with one click.</span>
                </div>
                <div class="feature-card">
                    <strong>Clear result</strong>
                    <span>See a compact verdict card with a direct status.</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

tfidf_vectorizer = pickle.load(open('model/tfid.pkl', 'rb'))
model = pickle.load(open('model/model.pkl', 'rb'))

if submitted:

    transformed_msg = text_transform(msg_input)
    X = tfidf_vectorizer.transform([transformed_msg])
    prediction = model.predict(X)[0]

    result_class = "result-safe" if prediction == 0 else "result-spam"
    result_text = "The message is not spam." if prediction == 0 else "The message is spam."

    st.markdown(
        f"""
        <div class="result-card {result_class}">
            <p class="result-label">Prediction</p>
            <h3>{result_text}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )