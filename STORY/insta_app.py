import streamlit as st
import requests

# بيانات التليجرام الخاصة بك
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

st.set_page_config(page_title="Insta Mobile Pro", page_icon="📱", layout="centered")

# تصميم مخصص للموبايل (Buttons كبيرة وسهلة اللمس)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #39ff14; }
    .mobile-card {
        border: 2px solid #39ff14;
        border-radius: 20px;
        padding: 25px;
        background: #111;
        text-align: center;
        box-shadow: 0 0 20px #39ff14;
    }
    .stButton>button {
        width: 100%;
        height: 70px;
        background: linear-gradient(90deg, #39ff14, #00ccff);
        color: black;
        font-weight: bold;
        font-size: 22px;
        border-radius: 15px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📱 Insta Mobile: نظام الرادار المتنقل")

def send_alert(user):
    try:
        msg = f"📱 <b>تنبيه موبايل جديد!</b>\nالهدف: <code>{user}</code>\nالنظام: جلب عبر المتصفح المباشر"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": TELEGRAM_ID, "text": msg, "parse_mode": "HTML"})
    except: pass

username = st.text_input("📡 أدخل يوزر الهدف (بدون @):", placeholder="f.xzon")

if username:
    user_clean = username.replace('@', '').strip()
    
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    if st.button("🚀 عرض الستوريات الآن"):
        send_alert(user_clean)
        
        # استراتيجية الفتح المباشر (تتجاوز حظر الـ iFrame تماماً)
        # سيقوم المتصفح بفتح تبويب جديد نظيف يعرض الستوري فوراً
        target_link = f"https://saveig.app/en/instagram-story-viewer/{user_clean}"
        
        st.success(f"✅ تم تجهيز الرابط لـ {user_clean}")
        st.markdown(f'''
            <a href="{target_link}" target="_blank" style="text-decoration:none;">
                <div style="background:#39ff14; color:black; padding:20px; border-radius:10px; font-weight:bold; font-size:20px;">
                    إضغط هنا لفتح العرض (تجاوز الحظر) 🔓
                </div>
            </a>
            <p style="color:gray; font-size:12px; margin-top:10px;">سيفتح العرض في نافذة مؤمنة لتجنب حظر الـ IP</p>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.info(f"نظام المراقبة متصل بـ ID: {TELEGRAM_ID}")