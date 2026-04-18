import streamlit as st

# إعدادات واجهة المستخدم الاحترافية
st.set_page_config(page_title="Insta Chick Pro - Gold Edition", page_icon="🔥", layout="centered")

# إضافة لمسات تصميم فاخرة (CSS)
st.markdown("""
    <style>
    .main { background: #000000; color: #ffffff; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #f9ce34, #ee2a7b, #6228d7);
        color: white; border: none; padding: 20px;
        font-size: 20px; border-radius: 15px; font-weight: bold;
        transition: 0.3s; box-shadow: 0 4px 15px rgba(238, 42, 123, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 6px 20px rgba(238, 42, 123, 0.6); }
    input { border-radius: 10px !important; }
    .success-text { color: #00ffcc; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Insta Chick Pro: Gold Edition")
st.write("---")

# واجهة إدخال البيانات
username = st.text_input("👤 أدخل اسم المستخدم المستهدف (بدون @):", placeholder="مثال: an.or.8")

st.markdown("### 🛠️ اختر محرك الجلب الذكي:")
col1, col2 = st.columns(2)

with col1:
    engine_1 = st.button("🚀 محرك الصاروخ (Fast)")
with col2:
    engine_2 = st.button("💎 محرك الجودة (HD)")

# تفعيل التحقق البشري لزيادة الأمان (أنا لست ريبورت)
is_human = st.toggle("✅ أنا لست ريبورت - تأكيد الهوية")

if username:
    user_clean = username.replace('@', '').strip()
    
    if is_human:
        if engine_1:
            # توجيه ذكي يتجاوز حظر الـ IFrame
            target = f"https://saveig.app/en/instagram-story-viewer/{user_clean}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{target}\'">', unsafe_allow_html=True)
            st.success(f"جاري تحويلك لمحرك الصاروخ لجلب ستوريات {user_clean}...")
            st.balloons()

        if engine_2:
            target = f"https://igsaved.com/story-viewer/{user_clean}"
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{target}\'">', unsafe_allow_html=True)
            st.success(f"جاري تحويلك لمحرك الجودة لجلب ستوريات {user_clean}...")
            st.snow()
    elif (engine_1 or engine_2):
        st.error("⚠️ من فضلك فعل خيار 'أنا لست ريبورت' أولاً!")

st.markdown("---")
st.info("💡 **لماذا هذا التحديث؟** هذا النظام يضمن تجاوز حظر IPs السيرفرات تماماً ويمنحك وصولاً مباشراً للمحركات العالمية دون أخطاء برمجية.")