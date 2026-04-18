import streamlit as st
import requests

# بيانات التليجرام الخاصة بك (تم دمجها كما طلبت)
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_ID, "text": message, "parse_mode": "HTML"}
        requests.post(url, json=payload)
    except:
        pass

# إعدادات الواجهة
st.set_page_config(page_title="Insta Chick Pro - Admin View", page_icon="📸")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00ffcc; }
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00ffcc, #0088ff);
        color: black; font-weight: bold; border-radius: 12px; padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Insta Chick Pro: Admin Edition")

username = st.text_input("👤 أدخل اسم المستخدم المستهدف:")
is_human = st.toggle("✅ أنا لست ريبورت")

if st.button("🚀 بدء الجلب وتنبيه المسؤول"):
    if not is_human:
        st.error("⚠️ يرجى تأكيد الهوية أولاً!")
    elif username:
        user_clean = username.replace('@', '').strip()
        
        # إرسال تنبيه لك على التليجرام فوراً
        alert_msg = f"🔔 <b>تنبيه جديد!</b>\n\nقام شخص ما بالبحث عن:\n👤 المستخدم: <code>{user_clean}</code>\n🌐 المنصة: Insta Chick Pro"
        send_telegram_alert(alert_msg)
        
        # التوجيه لمحرك الجلب
        target = f"https://saveig.app/en/instagram-story-viewer/{user_clean}"
        st.success(f"جاري الجلب... تم إرسال تقرير إلى المسؤول.")
        st.markdown(f'<meta http-equiv="refresh" content="1;URL=\'{target}\'">', unsafe_allow_html=True)
    else:
        st.warning("⚠️ أدخل اسم المستخدم.")

st.info("💡 تم ربط الأداة بنظام التنبيهات الفوري الخاص بك.")