import streamlit as st
import requests

# إعداد واجهة المستخدم
st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")
st.title("📸 Insta Chick Pro")
st.write("عرض ستوريات إنستقرام للحسابات العامة بسرعة واستقرار")

def get_stories_v3(username):
    # استخدام محرك جلب سريع ومستقر عبر API
    api_url = f"https://browser9.com/api/instagram/stories?username={username}"
    try:
        response = requests.get(api_url, timeout=20)
        if response.status_code == 200:
            data = response.json()
            return data.get('result', [])
        return None
    except:
        return None

user_input = st.text_input("أدخل اسم المستخدم (مثال: 10ra_9):")

if st.button("عرض الستوريات الآن"):
    if user_input:
        with st.spinner("🚀 جاري الجلب..."):
            stories = get_stories_v3(user_input)
            
            if stories:
                st.success(f"✅ تم العثور على {len(stories)} عنصر")
                cols = st.columns(2)
                for idx, item in enumerate(stories):
                    with cols[idx % 2]:
                        if item.get('type') == 'video':
                            st.video(item.get('url'))
                        else:
                            st.image(item.get('url'), use_container_width=True)
            else:
                st.error("❌ لم يتم العثور على نتائج. تأكد أن الحساب عام ولديه ستوري حالياً.")
    else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم.")