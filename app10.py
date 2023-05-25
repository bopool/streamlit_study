import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


def main():
    st.title('내 앱 대시보드')
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    st.write(df1.shape)
    lang_list = df1.columns[1: ]
    choice_list = st.multiselect('언어를 선택하세요.', lang_list)
    # 유저가 아무것도 선택 안 했을 때 처리
    # if의 조건을 충족못하면 그냥 내려감. 
    if len(choice_list) > 0:
        choice_df = df1[choice_list]
        st.dataframe(choice_df)
    
        # 스트림릿이 제공하는 라인차트
        st.line_chart(choice_df)
        st.area_chart(choice_df)
        
    df2 = pd.read_csv('data/iris.csv')

    # 스트림릿이 제공하는 바 차트 
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)

    # Altair 
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length', 
        y = 'petal_width',
        color = 'species'
    )
    st.altair_chart(chart)

    # 스트림릿의 map차트
    df4 = pd.read_csv('data/location.csv', index_col = 0)
    print(df4)
    st.map(df4)

    df5 = pd.read_csv('data/prog_languages_data.csv', index_col = 0)
    print(df5)
    st.dataframe(df5)

    # plotly의 pie차트 (파이차트는 비율을 보고 싶을 때)
    fig1 = px.pie(df5, 'lang')
    st.plotly_chart(fig1)

    # plotly의 bar 차트 
    df6 = df5.sort_values('Sum', ascending=False)
    fig2 = px.bar(df6, x='lang', y='Sum')
    st.plotly_chart(fig2)



if __name__ == '__main__': 
    main()
    