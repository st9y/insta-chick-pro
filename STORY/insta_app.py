import streamlit as st
import asyncio
import sys
import nest_asyncio
from playwright.async_api import async_playwright

# إعدادات التوافق
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
nest_asyncio.apply()

st.set_page_config(page_title="Insta Chick Pro", page_icon="📸")

# محرك جلب الستوريات
async def get_stories(username):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        try:
            await page.goto(f"https://www.save-free.com/ar/insta-stories-viewer/", timeout=60000)
            await page.fill('input#username', username)
            await page.click('button#btn-view')
            await asyncio.sleep(10) # انتظار التحميل
            
            elements = await page.query_selector_all('div.story-item img, div.story-item video source')
            urls = []
            for el in elements:
                src = await el.get_attribute('src')
                if src: urls.append(src)
            await browser.close()
            return urls
        except Exception as e:
            await browser.close()
            return f"Error: {e}"

# واجهة المستخدم
st.title("📸 Insta Chick Pro")
user_input = st.text_input("أدخل اسم المستخدم:")

if st.button("عرض الستوريات"):
    if user_input:
        with st.spinner("جاري جلب البيانات..."):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results = loop.run_until_complete(get_stories(user_input))
            if isinstance(results, list) and results:
                for link in results:
                    st.image(link) if ".jpg" in link else st.video(link)
            else:
                st.error("فشل الجلب، تأكد أن الحساب عام.")