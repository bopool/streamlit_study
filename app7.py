import streamlit as st
from datetime import datetime
import os
import pandas as pd


# 디렉토리 이름과, 파일을 주면, 
# 해당 디렉토리에 파일을 저장해주는 함수 
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인하고, 없으면 디렉토리를 먼저 만든다. 유닉스 리눅스에서는 폴더를 디렉토리라고 함. 
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일 저장 
    with open(os.path.join(directory, file.name), 'wb') as f : # 파이썬 문법으로..
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')


 
def main():
    st.title('내 앱 대시보드')

    menu = ['이미지 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)
    print(choice)
    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')
        img_file = st.file_uploader('이미지를 업로드하세요.', type=['png', 'jpg', 'jpeg'])
        if img_file is not None : 
            print(type(img_file))

            print(img_file.name)
            print(img_file.size)
            print(img_file.type)

            # 유저가 올린 파일을 
            # 서버에서 유니크하게 처리하기 위해서 
            # 파일명을 현재시간 조합으로 다시 만든다. 
            current_time = datetime.now() # 서버의 현재시간 
            print(current_time)
            print(current_time.isoformat().replace(':', '_'))

            filename = current_time.isoformat().replace(':', '_')
            img_file.name = filename
            save_uploaded_file('image', img_file)
            st.image('image/'+img_file)


    elif choice == menu[1]:
        csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])
        if csv_file is not None:
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':', '_')
            csv_file.name = filename
            save_uploaded_file('csv', csv_file)
            df = pd.read_csv('csv/'+filename)
            st.dataframe(df)

    else:
        st.subheader('이 대시보드 설명')

if __name__ == '__main__': 
    main()