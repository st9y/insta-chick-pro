import streamlit as st
import requests

# بيانات التليجرام الخاصة بك
TELEGRAM_TOKEN = "8759333224:AAHZ-Zs_f8DHrvd6YStpITAO6_BUKWQQhD8"
TELEGRAM_ID = "1412684545"

st.set_page_config(page_title="Insta Radar Gold", page_icon="📡", layout="centered")

# تصميم واجهة الهكر المحترف
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #39ff14; }
    .stTextInput input { border: 2px solid #39ff14 !important; background-color: #000 !important; color: #39ff14 !important; border-radius: 10px; }
    .stButton>button {
        width: 100%; background: linear-gradient(45deg, #111, #222);
        color: #39ff14; font-weight: bold; border: 1px solid #39ff14; padding: 15px;
        font-size: 18px; border-radius: 10px; transition: 0.3s;
    }
    .stButton>button:hover { background: #39ff14; color: black; box-shadow: 0 0 15px #39ff14; }
    .link-box { border: 1px dashed #39ff14; padding: 20px; text-align: center; border-radius: 10px; background: #111; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📡 Insta Radar: Neural Gold")
st.write("نظام الرادار يعمل الآن بنظام التوجيه الآمن وتنبيهات المسؤول الفورية.")

username = st.text_input("📡 أدخل يوزر الهدف لبدء الرادار:", placeholder="f.xzon")

def notify_admin(user):
    try:
        msg = f"🎯 <b>عملية جلب جديدة</b>\n👤 الهدف: <code>{user}</code>\n🔗 الحالة: تم توليد روابط الوصول بنجاح."
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                      json={"chat_id": TELEGRAM_ID, "text": msg, "parse_mode": "HTML"})
    except:
        pass

if username:
    user_clean = username.replace('@', '').strip()
    
    if st.button("🛰️ تفعيل محرك الجلب وإرسال الإشارة"):
        # إرسال التنبيه لك فوراً
        notify_admin(user_clean)
        
        # إظهار روابط الوصول الآمنة للمستخدم بدل التحويل التلقائي الفاشل
        st.markdown(f"""
            <div class="link-box">
                <h3 style='color: #39ff14;'>✅ تم اختراق الحماية بنجاح</h3>
                <p style='color: white;'>اختر القناة المفتوحة للوصول إلى ستوريات <b>{user_clean}</b>:</p>
                <a href="https://saveig.app/en/instagram-story-viewer/{user_clean}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; padding:15px; background:#39ff14; color:black; border:none; border-radius:5px; cursor:pointer; font-weight:bold; margin-bottom:10px;">🚀 فتح عبر قناة الصاروخ (Fast)</button>
                </a>
                <a href="https://igsaved.com/story-viewer/{user_clean}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; padding:15px; background:transparent; color:#39ff14; border:1px solid #39ff14; border-radius:5px; cursor:pointer; font-weight:bold;">💎 فتح عبر قناة الجودة (HD)</button>
                </a>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.markdown("---")
st.caption("بروتوكول التشفير نشط | جميع العمليات يتم تسجيلها في نظام الرادار الخاص بك.")