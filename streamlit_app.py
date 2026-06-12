import streamlit as st

# --- 데이터 초기화 ---
days = ['월', '화', '수', '목', '금']
subjects = ['정보', '수학', '과학', '영어', '국어']

st.title("학교 수행평가 및 준비물 알리미 🏫")

# --- 1. 요일별 수행평가 확인 ---
st.header("1. 오늘의 수행평가 확인")
# 오타 방지 및 편의성을 위해 text_input 대신 selectbox를 사용합니다.
today = st.selectbox('오늘의 요일을 선택하세요:', ['선택하세요'] + days)

if today != '선택하세요':
    for i in range(5):
        if today == days[i]:
            st.success(f'오늘은 **{subjects[i]}** 수행평가가 있는 날 입니다. 🎉')

st.divider() # 화면 구분선

# --- 2. 과목별 준비물 확인 ---
st.header("2. 과목별 준비물 확인")
# '0'으로 종료하는 대신, 직관적인 드롭다운 메뉴를 제공합니다.
search_options = ["선택하세요", "정보", "수학", "과학", "국어", "영어"]
search = st.selectbox('준비물이 궁금한 과목을 선택하세요:', search_options)

if search != "선택하세요":
    if search == "정보":
        st.info("💻 필기도구 챙겨서 컴퓨터실로 오세요")
    elif search == "수학":
        st.info("📐 오답노트를 꼭 챙기세요")
    elif search == "국어":
        st.info("📖 교과서와 수업 프린트를 꼭 챙기세요.")
    elif search == "과학":
        st.info("🔬 필기도구를 챙겨서 과학실로 오세요.")
    elif search == "영어":
        st.warning("등록된 준비물 안내가 없습니다.")
    else:
        st.error("잘못 입력했는지 확인하세요")
