import streamlit as st
import requests
import re

st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")
st.title("📸 Insta Chick Pro")
st.write("عرض ستوريات الحسابات العامة بمجهولية تامة")

def get_insta_stories(username):
    # محرك جلب متطور يستخدم وسيطاً لتجاوز الحظر
    search_url = f"https://storiesig.info/api/ig/stories/{username}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://storiesig.info/"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=20)
        if response.status_code == 200:
            data = response.json()
            # استخراج الروابط المباشرة للصور والفيديوهات
            return data.get('result', [])
        return None
    except Exception as e:
        return None

user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("عرض الستوريات الآن"):
    if user_input:
        # تنظيف اسم المستخدم من أي رموز زائدة
        clean_user = user_input.replace('@', '').strip()
        with st.spinner("🚀 جاري محاولة اختراق الحظر وجلب البيانات..."):
            stories = get_insta_stories(clean_user)
            
            if stories:
                st.success(f"✅ تم العثور على {len(stories)} عنصر")
                for url in stories:
                    if ".mp4" in url or "video" in url:
                        st.video(url)
                    else:
                        st.image(url)
            else:
                st.error("❌ تعذر الجلب. إنستقرام يفرض حظراً مؤقتاً على السيرفر، جرب مرة أخرى بعد دقيقتين أو جرب حساباً آخر.")