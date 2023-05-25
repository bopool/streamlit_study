import streamlit as st
from datetime import datetime

from app_utils import save_uploaded_file


def run_app_image():
    st.subheader('이미지 파일 업로드')
    img_file = st.file_uploader('이미지를 업로드하세요.', type=['png', 'jpg', 'jpeg'])
    if img_file is not None : 

        # 유저가 올린 파일을 
        # 서버에서 유니크하게 처리하기 위해서 
        # 파일명을 현재시간 조합으로 다시 만든다. 
        current_time = datetime.now() # 서버의 현재시간 
        filename = current_time.isoformat().replace(':', '_') # 날짜 변환 메소드 isoformat()
        img_file.name = filename # 파일명에 위에서 만든 날짜변환이름으로 바꾸세용
        save_uploaded_file('image', img_file) # 'image' 폴더를 만들어서 img_file을 넣으세요. 
        st.image('image/'+ filename) # image/imgfile을 이미지로 화면에 출력해 주세요. 

