# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd

def main():
    st.title("Popover Demo")
    
    tips = sns.load_dataset('tips')

    with st.popover("Show Dataset Info"):
        st.write("This dataset contains restaurant tips data")
        st.write(f"Number of records: {len(tips)}")
        st.write(f"Number of columns: {len(tips.columns)}")
        st.write("Columns:", tips.columns.tolist())

    with st.popover("Show Statistics"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average Bill", f"${tips['total_bill'].mean():.2f}")
            st.metric("Average Tip", f"${tips['tip'].mean():.2f}")
        with col2:
            st.metric("Max Bill", f"${tips['total_bill'].max():.2f}")
            st.metric("Max Tip", f"${tips['tip'].max():.2f}")
    
    st.dataframe(tips)

if __name__ == "__main__":
    main()
