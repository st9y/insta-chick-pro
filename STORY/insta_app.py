import streamlit as st
import requests

# بيانات التليجرام الخاصة بك (مدمجة بعمق في الكود)
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

def notify_admin(user):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        msg = f"🔔 <b>رادار Insta View:</b>\n\nيتم الآن عرض ستوريات الحساب:\n👤 <code>{user}</code>\n📍 الحالة: عرض داخلي مباشر"
        requests.post(url, json={"chat_id": TELEGRAM_ID, "text": msg, "parse_mode": "HTML"})
    except:
        pass

# إعدادات الصفحة
st.set_page_config(page_title="Insta Viewer Pro - Internal", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #fff; }
    .main-container { border: 2px solid #39ff14; border-radius: 15px; padding: 20px; background: #111; }
    iframe { border: 2px solid #333; border-radius: 15px; background: white; }
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #39ff14, #0088ff);
        color: black; font-weight: bold; border-radius: 10px; padding: 15px; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 Insta View Pro: العرض الداخلي الذكي")
st.write("---")

username = st.text_input("👤 أدخل اليوزر المطلوب لعرضه هنا:")

if username:
    user_clean = username.replace('@', '').strip()
    
    if st.button("👁️ تفعيل الرادار والعرض المباشر"):
        # 1. إرسال التنبيه الفوري لك
        notify_admin(user_clean)
        
        # 2. عرض رسالة النجاح
        st.success(f"✅ تم ربط المحرك المحدث بنجاح لليوزر: {user_clean}")
        
        # 3. المحرك المحدث (استخدام SnapInsta كمحرك وسيط للعرض الداخلي)
        # هذا الرابط مصمم ليفتح داخل الـ IFrame بدون حظر
        viewer_url = f"https://snapinsta.app/instagram-story-viewer/{user_clean}"
        
        st.markdown(f"""
            <div class="main-container">
                <h4 style='color: #39ff14; text-align: center;'>📡 بث مباشر من السيرفرات العالمية</h4>
                <iframe src="{viewer_url}" width="100%" height="900px"></iframe>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.sidebar.markdown("### 🛠️ حالة النظام")
st.sidebar.success("التنبيهات: متصلة ✅")
st.sidebar.info(f"ID المسؤول: {TELEGRAM_ID}")