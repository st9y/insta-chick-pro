import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="Insta Chick Pro - Ultimate", page_icon="📸", layout="wide")

# تصميم واجهة تشبه المنصات العالمية
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTextInput>div>div>input { background-color: #262730; color: white; border-radius: 10px; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        color: white; border: none; padding: 15px; font-weight: bold; border-radius: 10px;
    }
    iframe { border-radius: 15px; border: 2px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("📸 Insta Chick Pro: Ultimate Edition")
st.markdown("### المحرك الجديد لتجاوز الحظر العالمي 🚀")

# خيارات المحركات (تجاوز جذري)
engine = st.selectbox("اختر محرك الجلب (في حال فشل واحد جرب الآخر):", 
                     ["Engine 1 (Fast)", "Engine 2 (HD)", "Engine 3 (Backup)"])

user_input = st.text_input("أدخل اسم المستخدم المراد مراقبته:", placeholder="an.or.8")

if st.button("فتح محرك الجلب الآن"):
    if user_input:
        username = user_input.replace('@', '').strip()
        
        # اختيار الرابط بناءً على المحرك المختار
        if "Engine 1" in engine:
            target_url = f"https://saveig.app/en/instagram-story-viewer/{username}"
        elif "Engine 2" in engine:
            target_url = f"https://igsaved.com/story-viewer/{username}"
        else:
            target_url = f"https://snapinsta.app/instagram-story-viewer/{username}"

        st.success(f"✅ تم تفعيل المحرك للحساب: {username}")
        
        # إضافة خاصية "أنا لست ريبورت" البصرية
        st.write("🔔 إذا ظهرت رسالة التحقق، أكملها داخل النافذة أدناه:")
        
        # تضمين الموقع داخل التطبيق (الحل الجذري)
        st.components.v1.iframe(target_url, height=800, scrolling=True)
    else:
        st.warning("⚠️ يرجى كتابة اسم المستخدم أولاً.")

st.sidebar.markdown("---")
st.sidebar.write("⚙️ **إرشادات الاستخدام:**")
st.sidebar.info("هذا النظام يستخدم تقنية IFrame لتجاوز حظر IP السيرفرات، مما يمنحك وصولاً مباشراً دون قيود.")