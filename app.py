import streamlit as st
import time

st.set_page_config(page_title="دقيقة واحدة!", layout="centered")

# ======================
# بيانات اللعبة
# ======================
scenes = [
    {
        "title": "🏠 حريق في المطبخ",
        "story": "🔥 النار بدأت تكبر، والغاز قريب.",
        "choices": [
            ("🧯 أطفئ النار", -50, "سيطرتِ على النار بسرعة."),
            ("🔌 افصل الكهرباء", -20, "قللتِ خطر إضافي."),
            ("🏃‍♀️ اخرج", +15, "أنقذتِ نفسك لكن الخطر باقي."),
        ],
        "wisdom": "السلامة أولًا."
    },
    {
        "title": "🏫 طالب مغمى عليه",
        "story": "طلاب متجمعون وصوتهم عالي.",
        "choices": [
            ("📣 أبعدي الطلاب", -30, "رتّبتِ المكان."),
            ("🧑‍🏫 نادِي المعلم", -25, "طلبتِ دعم مناسب."),
            ("📸 تصوير", +20, "زادت الفوضى."),
        ],
        "wisdom": "التأني وقت الخطر نجاة."
    },
    {
        "title": "🚦 سيارة متعطلة",
        "story": "السيارات تمر بسرعة.",
        "choices": [
            ("🚧 مثلث تحذير", -35, "نبهتِ السائقين."),
            ("👥 أبعدي الناس", -30, "قللتِ خطر الإصابات."),
            ("🚗 ادفعي السيارة", +25, "قرار خطير."),
        ],
        "wisdom": "العجلة ما تمنع الخطأ."
    },
]

# ======================
# الحالة
# ======================
if "stage" not in st.session_state:
    st.session_state.stage = "menu"
    st.session_state.scene = 0
    st.session_state.danger = 100
    st.session_state.score = 0
    st.session_state.feedback = ""

# ======================
# شاشة البداية
# ======================
if st.session_state.stage == "menu":
    st.title("⏱️ دقيقة واحدة!")
    st.subheader("أنتِ قائدة السلامة 🚨")
    st.write("اتخذي قرارات سريعة في مواقف حقيقية.")
    if st.button("▶️ ابدأي المهمة"):
        st.session_state.stage = "play"

# ======================
# شاشة اللعب
# ======================
elif st.session_state.stage == "play":
    scene = scenes[st.session_state.scene]

    # إحساس ضغط
    if st.session_state.danger > 70:
        st.warning("⏳ الوقت يضغط عليك!")
    elif st.session_state.danger > 40:
        st.info("⚠️ الوضع متوتر")
    else:
        st.success("🟢 تحت السيطرة")

    st.subheader(scene["title"])
    st.write(scene["story"])
    st.progress(st.session_state.danger)

    for label, effect, text in scene["choices"]:
        if st.button(label):
            st.session_state.danger += effect
            st.session_state.feedback = text
            st.session_state.stage = "result"

# ======================
# شاشة النتيجة
# ======================
elif st.session_state.stage == "result":
    scene = scenes[st.session_state.scene]

    st.subheader("🔎 نتيجة القرار")
    st.write(st.session_state.feedback)

    if st.session_state.danger <= 30:
        st.success("✔️ الخطر انخفض كثير")
        st.session_state.score += 2
    elif st.session_state.danger <= 60:
        st.warning("⚠️ الخطر خف")
        st.session_state.score += 1
    else:
        st.error("❌ الخطر ما زال عالي")

    st.caption(f"🧠 حكمة: {scene['wisdom']}")

    if st.button("➡️ الموقف التالي"):
        st.session_state.scene += 1
        if st.session_state.scene >= len(scenes):
            st.session_state.stage = "end"
        else:
            st.session_state.stage = "play"

# ======================
# شاشة النهاية
# ======================
elif st.session_state.stage == "end":
    st.title("🏁 انتهت المهمة")

    if st.session_state.score >= 5:
        st.success("🏆 قائدة سلامة ممتازة")
    elif st.session_state.score >= 3:
        st.warning("👍 قائدة جيدة لكن تقدرين أفضل")
    else:
        st.error("⚠️ قراراتك كانت مترددة")

    if st.button("🔁 إعادة اللعب"):
        st.session_state.stage = "menu"
        st.session_state.scene = 0
        st.session_state.danger = 100
        st.session_state.score = 0
