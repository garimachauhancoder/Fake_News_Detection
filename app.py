# import spacy
# import streamlit as st
# from streamlit_option_menu import option_menu

# from preprocessing import clean_text

# st.set_page_config(
#     page_title="Fake News Detection",
#     page_icon="📰",
#     layout="wide",
#     initial_sidebar_state = "expanded"
# )

# with st.sidebar:
#     st.image("fakelogo image.jpg", width = 90)
    
#     selected = option_menu(
#         menu_title="",
#         options=["Home", "Predict News", "Dataset Analytics", "Model Comparison"],
#         icons=["house-fill","serach","pie-chart-fill","bar-chart-fill"],
#         default_index=0,
#         styles={
#             "container": {"padding":"10px", "background-color": "#f0f2f6"},
#             "icon": {"color": "orange", "font-size": "25px"},
#             "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#             "nav-link-selected": {"background-color": "#4F46E5"},
#         },

#     )

# st.title("Fake News Detection System")
# st.write("Welcome to the Fake News Detection Dashboard!")
# container = st.container()

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

# ---------- CSS ----------

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Hide Streamlit Menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Navbar */

.navbar{
background:#0F172A;
padding:18px;
border-radius:12px;
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:25px;
}

.logo{
font-size:28px;
font-weight:bold;
color:white;
}

.menu{
color:white;
font-size:18px;
}

/* Hero */

.hero{
background:linear-gradient(90deg,#EEF2FF,#F8FAFC);
padding:40px;
border-radius:18px;
margin-bottom:30px;
}

.hero-title{
font-size:42px;
font-weight:700;
color:#111827;
}

.hero-sub{
font-size:20px;
color:#6B7280;
margin-top:10px;
margin-bottom:30px;
}

.button{
background:#4F46E5;
padding:14px 35px;
border-radius:10px;
color:white;
display:inline-block;
font-weight:bold;
}

/* Cards */

.card{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0px 4px 15px rgba(0,0,0,.08);
text-align:center;
}

.metric{
font-size:34px;
font-weight:bold;
color:#4F46E5;
}

.label{
color:gray;
font-size:17px;
}

</style>
""",unsafe_allow_html=True)

# ---------------- NAVBAR ----------------

st.markdown("""
<div class="navbar">

<div class="logo">
📰 Fake News AI
</div>

<div class="menu">
Home &nbsp;&nbsp;&nbsp;
Predict News &nbsp;&nbsp;&nbsp;
Analytics &nbsp;&nbsp;&nbsp;
Models &nbsp;&nbsp;&nbsp;
About
</div>

</div>
""",unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class="hero">

<div class="hero-title">
Welcome to Fake News Detection Dashboard
</div>

<div class="hero-sub">
Analyze and detect fake news using Machine Learning,
Natural Language Processing and Artificial Intelligence.
</div>

<div class="button">
🚀 Start Prediction
</div>

</div>
""",unsafe_allow_html=True)

# ---------------- METRIC CARDS ----------------

c1,c2,c3,c4=st.columns(4)

with c1:

    st.markdown("""
    <div class="card">

    <div class="label">Accuracy</div>

    <div class="metric">98.7%</div>

    </div>
    """,unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <div class="label">Predictions</div>

    <div class="metric">12,543</div>

    </div>
    """,unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="card">

    <div class="label">Fake News</div>

    <div class="metric" style="color:#DC2626;">4321</div>

    </div>
    """,unsafe_allow_html=True)

with c4:

    st.markdown("""
    <div class="card">

    <div class="label">Real News</div>

    <div class="metric" style="color:#16A34A;">8222</div>

    </div>
    """,unsafe_allow_html=True)

st.write("")

# ---------------- CHARTS ----------------

left,right=st.columns([2,1])

with left:

    df=pd.DataFrame({

        "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Real":[820,760,930,900,1010,1100,1080],
        "Fake":[420,320,450,470,400,510,520]

    })

    fig=go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Day"],
        y=df["Real"],
        mode="lines+markers",
        name="Real News"
    ))

    fig.add_trace(go.Scatter(
        x=df["Day"],
        y=df["Fake"],
        mode="lines+markers",
        name="Fake News"
    ))

    fig.update_layout(
        title="Prediction Overview",
        height=420,
        template="plotly_white"
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    pie=px.pie(
        values=[65,35],
        names=["Real","Fake"],
        hole=.65
    )

    pie.update_layout(
        title="News Distribution",
        height=420
    )

    st.plotly_chart(pie,use_container_width=True)

# ---------------- RECENT ----------------

st.subheader("Recent Predictions")

recent=pd.DataFrame({

"Headline":[
"NASA discovers new planet",
"Government releases budget",
"Celebrity cures cancer",
"Stock Market crashes"
],

"Prediction":[
"Real",
"Real",
"Fake",
"Real"
]

})

st.dataframe(recent,use_container_width=True)

st.write("")

st.info("💡 Tip: Open **Predict News** from the navigation to classify a new article.")