import streamlit as st
import pandas as pd

def main():
    st.title('앱 대쉬보드')
    df = pd.read_csv('data/iris.csv')

    # 버튼 
    if st.button('데이터 보기'):
        st.dataframe(df)
    
    name = 'Mike'
    # 대문자 버튼을 누르면, 대문자로 표시하고 소문자 버튼을 누르면, 소문자로 나오게 하자 
    if st.button('대문자'):
        st.text(name.lower())
    
    if st.button('소문자'):
        st.text(name.upper())

    st.dataframe(df)
        # petal_length 컬럼을 정렬하고 싶다. 
        # 오름차순 정렬, 내림차순 정렬 두가지 옵션 선택하도록 
    status = st.radio('정렬을 선택하세요.', ['오름차순', '내림차순'])
    # print(status)

    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length'))

    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')

    # 여러 개 중 1개를 선택
    language = ['Python', 'Java', 'C', 'GO', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('클래스가 좀 어렵지')
    elif selected_lang == 'C':
        st.text('C가 기본이지')
    elif selected_lang == 'GO':
        st.text('x')
    elif selected_lang == 'PHP':
        st.text('o')
    
    # 데이터프레임의 컬럼 이름을 보여주고, 
    # 유저가 컬럼을 선택하면 
    # 해당 컬러만 가져와서 
    # 데이터프레임을 보여주고 싶다. 
    column_list = st.multiselect('컬럼을 선택하세요.', df.columns)
    print(column_list)
    st.dataframe(df[column_list])
        
    age = st.slider('나이', min_value = 10, max_value= 110, step = 1)
    st.text('나이는 ' + str(age) + '세 입니다.')

    with st.expander('hello'):
        st.text('안녕하세요.')


# VSCode는 웹 대쉬보드만들 때 쓰는 거고. 
# 백엔드개발자는 많지만 데이터분석할 줄 아는 사람은 많지 않다. 





if __name__ == '__main__':
    main()

