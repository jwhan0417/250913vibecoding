import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("🌍 MBTI 유형별 국가 Top 10 분석")

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    file_name = "countriesMBTI_16types.csv"
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    return None

# 기본적으로 같은 폴더에서 데이터 시도
df = load_data()

# 파일 업로드 옵션
if df is None:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

if df is not None:
    # MBTI 유형 리스트 (Country 제외)
    mbti_types = [col for col in df.columns if col != "Country"]

    # 유저가 MBTI 유형 선택
    selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

    # 선택한 유형 기준으로 Top 10 추출
    top10 = df.nlargest(10, selected_mbti)[["Country", selected_mbti]]

    # 데이터 표시
    st.subheader(f"🌟 {selected_mbti} 유형 비율이 가장 높은 국가 Top 10")
    st.dataframe(top10)

    # Altair 그래프
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(f"{selected_mbti}:Q", title="비율"),
            y=alt.Y("Country:N", sort="-x", title="국가"),
            tooltip=["Country", selected_mbti]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("⚠️ 데이터 파일이 없으니 CSV 파일을 업로드해주세요.")
