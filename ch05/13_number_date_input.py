# -*- coding:utf-8 -*-
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import yfinance as yf


def main():
    st.sidebar.title("Stock Chart")

    ticker = st.sidebar.text_input("Enter a ticker (e.g. AAPL)", value="AAPL")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')
    start_date = st.sidebar.date_input("Start date", value=pd.to_datetime('2023-01-01'))
    end_date = st.sidebar.date_input("End date", value=pd.to_datetime('today'))

    # yfinance 주식 데이터를 가져오는 코드
    data = yf.download(ticker, start=start_date, end=end_date)
    data.columns = data.columns.droplevel(1)
    
    # radio 차트 선택
    chart_type = st.sidebar.radio("Select chart type", ("Candlestick", "Line"))

    # Plotly Graph Objects 방식으로 차트 그리그
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])

    # Plotly Graph Objects 방식으로 차트 그리그
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')

    if chart_type == "Candlestick":
        fig = go.Figure(candlestick)
    elif chart_type == "Line":
        fig = go.Figure(line)
    else:
        pass

    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")

    # Plot the figure
    st.plotly_chart(fig)
    st.markdown("<hr>", unsafe_allow_html=True)

    # 데이터프라임 출력
    num_row = st.sidebar.number_input('Number of Rows', min_value=1, max_value=len(data))
    
    # - 기호는 역으로 출력
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index('Date'), use_container_width=True)


if __name__ == "__main__":
    main()