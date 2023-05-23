import streamlit as st

# streamlit : framework 앱 대쉬보드를 만들어주는 패키지 

# framework 는 틀 안에서 작업하면 됨. 


# st. 은 무조건 화면에 대한 조건. 

def main():
    st.title('내 앱 대시보드')
    st.text('데이터 분석 앱입니다.')
    st.text('테스트 앱입니다.')

# 앱 실행한 게 name이면 main을 실행하라.
if __name__ == '__main__': 
    main()
    
