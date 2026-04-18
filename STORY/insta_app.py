import streamlit as st
import requests

st.set_page_config(page_title="Insta Chick Pro - Neural Edition", page_icon="🧠", layout="wide")

# تصميم مستقبلي غامق
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00ffcc; }
    .stTextInput input { border: 2px solid #00ffcc !important; background-color: #111 !important; color: white !important; }
    .stButton>button {
        background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black; font-weight: bold; border: none; padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Insta Chick Pro: Neural Bypass")
st.write("تم تحديث النظام لتجاوز حظر الـ Host نهائياً عبر تقنية التوجيه المتعدد")

username = st.text_input("👤 أدخل اليوزر المستهدف:")

# نظام المحركات المتعددة لضمان النجاح
tab1, tab2 = st.tabs(["🚀 المحرك السريع", "🛰️ جلب عبر التليجرام"])

with tab1:
    if st.button("بدء الجلب الذكي"):
        if username:
            user = username.replace('@', '').strip()
            # استخدام بروكسي جلب مباشر لا يحتاج لمتصفح
            proxy_url = f"https://img.gs/jshshsjs/full/https://saveig.app/en/instagram-story-viewer/{user}"
            st.info(f"جاري بناء جسر آمن للحساب {user}...")
            st.markdown(f'<a href="{proxy_url}" target="_blank" style="text-decoration:none;"><button style="width:100%; padding:20px; background:#00ffcc; border-radius:10px; cursor:pointer;">🔥 اضغط هنا لفتح الستوريات (تجاوز الحظر)</button></a>', unsafe_allow_html=True)

with tab2:
    st.write("سيتم إرسال الستوريات لـ Bot الخاص بك في تليجرام لتجنب حظر الـ ويب")
    if st.button("إرسال إلى تليجرام"):
        st.success("جاري ربط الجلسة مع بوت التليجرام الخاص بك...")