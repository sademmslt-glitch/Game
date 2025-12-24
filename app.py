import streamlit as st

st.set_page_config(page_title="دقيقة واحدة!", layout="centered")

st.title("⏱️ دقيقة واحدة!")
st.subheader("موقف: حريق في المطبخ")

st.write("🔥 فيه نار صغيرة قريبة من الموقد. الوقت يضغط عليك.")

if "danger" not in st.session_state:
    st.session_state.danger = 100
    st.session_state.done = False
    st.session_state.msg = ""

if not st.session_state.done:
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🧯 أطفئ النار"):
            st.session_state.danger -= 60
            st.session_state.msg = "تصرفت بسرعة 👍 لكن انتبه للغاز."
            st.session_state.done = True
    with c2:
        if st.button("🚪 افتح النافذة"):
            st.session_state.danger -= 30
            st.session_state.msg = "خففت الخطر شوي، لكن النار لازالت."
            st.session_state.done = True
    with c3:
        if st.button("🏃‍♂️ اخرج"):
            st.session_state.danger += 10
            st.session_state.msg = "حميت نفسك، لكن تركت الخطر."
            st.session_state.done = True
else:
    st.write("### 🔎 النتيجة")
    st.write(st.session_state.msg)
    st.write(f"🚨 مستوى الخطر: {st.session_state.danger}")
    if st.session_state.danger <= 20:
        st.success("✔️ الخطر تحت السيطرة")
    elif st.session_state.danger <= 60:
        st.warning("⚠️ الخطر خف لكنه موجود")
    else:
        st.error("❌ الخطر عالي")
    if st.button("🔁 أعد المحاولة"):
        st.session_state.danger = 100
        st.session_state.done = False
        st.session_state.msg = ""
