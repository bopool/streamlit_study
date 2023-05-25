import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import altair

def main():
    st.title('내 앱 대시보드')
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    # sepal_length, sepal_width 의 관계를 차트로 
    # scatter

    fig = plt.figure()
    plt.scatter(data= df, x = 'sepal_length', y= 'sepal_width') # 데이터프레임에서 가져오세요!
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data= df, x = 'sepal_length', y= 'sepal_width')
    st.pyplot(fig2)

    # 데이터 상관관계분석 
    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation)

    # sepal_length로 히스토그램 그리자 
    # bin의 갯수는 20개로 
    fig3 = plt.figure()
    plt.hist(data=df, x = 'sepal_length', rwidth = 0.9, bins = 20)
    st.pyplot(fig3) 
    
    fig3_1 = plt.figure(figsize=(10, 4)) # 가로 10, 세로 4
    plt.subplot(1, 2, 1) # 이런 키워드로 검색하면 많은 것을 알 수 있다! subplot 이런 거.. 
    plt.hist(data=df, x = 'sepal_length', rwidth = 0.9, bins = 20)
    plt.subplot(1, 2, 2)
    plt.hist(data=df, x = 'sepal_length', rwidth = 0.9, bins = 10)
    st.pyplot(fig3_1) 
    
    # species 컬럼에는 종에 대한 정보가 들어있는데, 
    # 각 종별로 몇 개씩의 데이터가 있는지 
    # 차트로 나타내시오. 
    st.dataframe(df['species'].value_counts())

    fig4 = plt.figure()
    sns.countplot(data = df, x = 'species')
    st.pyplot(fig4)

    # 데이터프레임의 차트 그리는 코드도 실행 가능 
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind= 'barh')
    st.pyplot(fig5)

    # 데이터프레임 자체 plot함수는 스트림릿에서는 안된다. 
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist(rwidth = 0.9)
    st.pyplot(fig7)

 
    # https://plotly.com/python/
    # https://altair-viz.github.io/


if __name__ == '__main__': 
    main()