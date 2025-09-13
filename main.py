import streamlit as st
import random

st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚", layout="centered")

# 제목
st.title("📖 MBTI별 ✨맞춤 공부법 추천✨")
st.markdown("공부할 때도 성격이 반영된다구요! 🤓 MBTI를 선택하고 자신에게 맞는 공부법을 찾아보세요 🚀")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 공부법 데이터
study_tips = {
    "INTJ": "계획형 📅 | 구체적인 학습 목표를 세우고 차근차근 실행하면 효과 최고! 🚀",
    "INTP": "탐구형 🔍 | 스스로 질문을 만들고 답을 찾으며 깊이 있는 공부가 잘 맞아요! 🧠",
    "ENTJ": "리더형 👑 | 스터디 그룹을 만들어 리드하면서 배울 때 흡수력이 올라가요! 🤝",
    "ENTP": "도전형 ⚡ | 토론하고 말하면서 배우면 기억에 쏙쏙 들어와요! 🎤",
    "INFJ": "통찰형 🌌 | 의미와 가치를 찾으며 공부할 때 집중력이 오래가요! ✨",
    "INFP": "감성형 🎨 | 공부를 자기만의 이야기나 이미지로 바꾸면 흥미가 높아져요! 💭",
    "ENFJ": "격려형 💕 | 친구와 함께 가르쳐주며 공부할 때 가장 잘 배워요! 👩‍🏫",
    "ENFP": "아이디어형 💡 | 다양한 자료와 색깔펜을 활용하면 창의적으로 공부 가능! 🌈",
    "ISTJ": "체계형 📊 | 교재 순서대로 정리하고 암기하면 안정적으로 습득! 📝",
    "ISFJ": "헌신형 🕊️ | 조용히 반복 학습하고 플래너에 체크하면서 성취감 얻기 👍",
    "ESTJ": "관리형 🛠️ | 규칙적인 시간표를 만들어 꾸준히 따라가면 성과 확실! ⏰",
    "ESFJ": "사교형 🎶 | 친구와 함께 문제를 풀고 대화로 학습하면 효과 만점! 💬",
    "ISTP": "실험형 🔧 | 직접 해보면서 배우는 체험식 공부가 딱 맞아요! 🛠️",
    "ISFP": "자유형 🌿 | 음악 🎵을 들으며 분위기 있게 공부하면 몰입 가능! 🎧",
    "ESTP": "모험형 🏃 | 실전 문제풀이로 빠르게 적용하며 배우면 성과 Good! 🏆",
    "ESFP": "에너지형 🎉 | 게임처럼 즐기면서 공부해야 오래 집중 가능! 🎮"
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 골라주세요 👇", mbti_types)

if selected_mbti:
    tip = study_tips[selected_mbti]
    st.subheader(f"✨ {selected_mbti} 유형을 위한 추천 공부법 ✨")
    st.success(tip)

    # 랜덤 재미 요소: 풍선 또는 눈 내리기
    effect = random.choice(["balloons", "snow"])
    if effect == "balloons":
        st.balloons()
    else:
        st.snow()

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ and lots of ☕ by ChatGPT")
