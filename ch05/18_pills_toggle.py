# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd

def main():
    st.title("Pills and Toggle Demo")
    
    tips = sns.load_dataset('tips')
    
    st.subheader("Pills Example")
    
    time_filter = st.pills("Select Time", ["All", "Lunch", "Dinner"])
    
    if time_filter is None or time_filter == "All":
        filtered_data = tips
    else:
        filtered_data = tips[tips['time'] == time_filter]
        
    st.write(f"Showing data for: {time_filter if time_filter else 'All'}")
    st.dataframe(filtered_data)
    
    st.subheader("Toggle Example")
    show_stats = st.toggle("Show Summary Statistics")
    
    if show_stats:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average Bill", f"${filtered_data['total_bill'].mean():.2f}")
            st.metric("Average Tip", f"${filtered_data['tip'].mean():.2f}")
        with col2:
            st.metric("Max Bill", f"${filtered_data['total_bill'].max():.2f}")
            st.metric("Max Tip", f"${filtered_data['tip'].max():.2f}")
            
    show_filters = st.toggle("Show Additional Filters")
    
    if show_filters:
        col1, col2 = st.columns(2)
        with col1:
            smoker = st.checkbox("Smokers Only")
        with col2:
            large_party = st.checkbox("Large Parties (>4) Only")
            
        if smoker:
            filtered_data = filtered_data[filtered_data['smoker'] == 'Yes']
        if large_party:
            filtered_data = filtered_data[filtered_data['size'] > 4]
            
        st.dataframe(filtered_data)

if __name__ == "__main__":
    main()

