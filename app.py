import streamlit as st

# إعدادات الصفحة لتكون محاذية لليمين ودعم اللغة العربية
st.set_page_config(page_title="نظام فحص النتيجة", page_icon="📝")

# تطبيق CSS بسيط لضبط الاتجاه والخطوط
st.markdown("""
    <style>
    body, div, input, button {
        direction: rtl;
        text-align: right;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("برنامج فحص نتيجة الطالب")

# حقول الإدخال
student_name = st.text_input("اسم الطالب:")
score = st.number_input("الدرجة من 100:", min_value=0, max_value=100, value=0, step=1)

# زر الفحص والمنطق البرمجي
if st.button("فحص النتيجة"):
    if student_name.strip() == "":
        st.warning("يرجى إدخال اسم الطالب أولاً.")
    else:
        if score >= 50:
            st.success(f"النتيجة: ناجح 🎉\n\nالطالب: {student_name} - الدرجة: {score}")
        else:
            st.error(f"النتيجة: راسب ❌\n\nالطالب: {student_name} - الدرجة: {score}")
