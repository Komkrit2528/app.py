import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Swiftlet Farm Monitor", layout="wide")

# ส่วนหัวของ Dashboard
st.title("ระบบตรวจติดตามบ้านนกนางแอ่นอัจฉริยะ 🐦")
st.markdown("---")

# --- ส่วนของการจำลองข้อมูล (Mock Data) ---
# ในการใช้งานจริง คุณจะดึงข้อมูลนี้มาจาก Database หรือ API ของกล้อง AI
current_birds = 55
current_nests = 24
temp = 28.5
humidity = 82

# สร้างข้อมูลกราฟย้อนหลัง 24 ชม.
chart_data = pd.DataFrame({
    'time': pd.date_range(start=datetime.now().replace(hour=0), periods=24, freq='H'),
    'อุณหภูมิ (°C)': np.random.uniform(27, 30, 24),
    'ความชื้น (%)': np.random.uniform(75, 85, 24)
})

# --- ส่วนการแสดงผล (Layout) ---

# 1. แถวบน: ข้อมูลสรุป (Metrics)
col1, col2, col3, col4 = st.columns(4)
col1.metric("จำนวนนกที่ตรวจพบ", f"{current_birds} ตัว", "↑ 5")
col2.metric("จำนวนรังนกสะสม", f"{current_nests} รัง", "↑ 2")
col3.metric("อุณหภูมิปัจจุบัน", f"{temp} °C", "ปกติ")
col4.metric("ความชื้นสัมพัทธ์", f"{humidity} %", "-1%")

st.markdown("---")

# 2. แถวกลาง: กราฟและวิดีโอ/ภาพ
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("📸 ภาพการตรวจจับล่าสุด")
    # จำลองภาพจากกล้อง (ในที่นี้คือภาพที่คุณอัปโหลดมา)
    st.image("https://example.com/your_detected_image.jpg", caption="AI Detection: Birds 55 detected", use_column_width=True)
    st.info("อัปเดตล่าสุด: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with right_col:
    st.subheader("📈 แนวโน้มสภาวะแวดล้อม (24 ชม.)")
    fig = px.line(chart_data, x='time', y=['อุณหภูมิ (°C)', 'ความชื้น (%)'], 
                  title='กราฟอุณหภูมิและความชื้น', color_discrete_sequence=['#ff4b4b', '#0068c9'])
    st.plotly_chart(fig, use_container_width=True)

# 3. ส่วนการแจ้งเตือน (Alerts)
st.subheader("🔔 รายงานสถานะ")
if humidity < 75:
    st.warning("⚠️ คำเตือน: ความชื้นต่ำกว่าเกณฑ์ที่กำหนด (ต่ำกว่า 75%)")
else:
    st.success("✅ สภาพแวดล้อมอยู่ในเกณฑ์ที่เหมาะสมสำหรับการทำรัง")
