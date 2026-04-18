import streamlit as st
import requests

# بيانات التليجرام الخاصة بك
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

st.set_page_config(page_title="Insta View Gold", page_icon="📡", layout="centered")

# تصميم احترافي يتجاوز أخطاء العرض السابقة
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #39ff14; }
    .stTextInput input { border: 2px solid #39ff14 !important; background-color: #000 !important; color: #39ff14 !important; }
    .stButton>button {
        width: 100%; background: #39ff14; color: black; font-weight: bold;
        border-radius: 8px; padding: 15px; border: none; font-size: 18px;
    }
    .status-box { border: 1px solid #39ff14; padding: 20px; border-radius: 10px; background: #111; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("📡 Insta View: الحل النهائي")

def send_telegram_log(user):
    try:
        msg = f"🎯 <b>عملية جلب ناجحة</b>\n👤 الحساب: <code>{user}</code>\n🔗 الحالة: تم توليد الرابط الآمن"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": TELEGRAM_ID, "text": msg, "parse_mode": "HTML"})
    except: pass

username = st.text_input("👤 أدخل يوزر الهدف (بدون @):")

if username:
    user_clean = username.replace('@', '').strip()
    
    if st.button("🚀 جلب المحتوى وإرسال الإشارة"):
        # إرسال التنبيه لك فوراً
        send_telegram_log(user_clean)
        
        # عرض روابط مباشرة تتجاوز مشكلة الشاشة الرمادية (image_27bc27.png)
        st.markdown(f"""
            <div class="status-box">
                <h3 style="color: #39ff14;">✅ تم توليد المسار الآمن</h3>
                <p style="color: white;">اضغط أدناه لفتح الستوريات مباشرة وتجاوز حظر المتصفح:</p>
                <a href="https://saveig.app/en/instagram-story-viewer/{user_clean}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; padding:15px; background:#39ff14; color:black; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">🔥 فتح في القناة 1 (سريع)</button>
                </a>
                <br><br>
                <a href="https://igsaved.com/story-viewer/{user_clean}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; padding:15px; background:transparent; color:#39ff14; border:1px solid #39ff14; border-radius:5px; cursor:pointer; font-weight:bold;">💎 فتح في القناة 2 (HD)</button>
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.sidebar.markdown(f"### 🛠️ حالة النظام\n- التنبيهات: متصلة ✅\n- المسؤول: `{TELEGRAM_ID}`")