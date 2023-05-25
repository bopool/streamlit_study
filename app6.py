import streamlit as st


def main():
    st.title('내 앱 대시보드')
    name = st.text_input('이름을 입력하세요.', max_chars=10)
    st.text('입력하신 이름은 ' + name + '입니다.')
    
    message = st.text_area('메시지를 입력하세요.', height=10) # 10줄까지 입력된다는. 
    st.text(message)
    
    number = st.number_input('숫자 입력하세요.', 1, 100)
    st.text(number * 3)

    number2 = st.number_input('숫자 입력하세요.', 1.0, 100.0)
    st.text(number2 * 3)

    my_date = st.date_input('약속 날짜를 입력하세요.')
    st.text(my_date)
    print(my_date)

    my_time = st.time_input('시간 선택', )
    print(type(my_time))
    st.text(my_time)
    
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    color = st.color_picker('색을 선택하세요') # 헥사코드 RGB행렬 0~25 ff가 25 숫자 넘파이행렬







if __name__ == '__main__': 
    main()