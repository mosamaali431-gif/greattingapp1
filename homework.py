import streamlit as st

st.title("🌈 رادار المشاعر المصور 🌈")

gender = st.radio("هل أنت:", ("ولد", "بنت"))
status = st.selectbox("بماذا تشعر الآن؟", ("سعيد", "حزين", "بردان"))

if st.button("إكتشف شكلك!"):
    if status == "سعيد":
        st.balloons()  # احتفال بالبالونات
        st.success("أيا له من يوم رائع!")

    elif status == "حزين":
        st.info("لا تحزن، غداً سيكون أفضل")

    elif status == "بردان":
        st.snow()  # تأثير الثلج السحري