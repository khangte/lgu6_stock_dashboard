# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd

def main():
    st.title("Column Configuration Demo")
    
    # Load tips dataset
    tips = sns.load_dataset('tips')
    
    tips_display = tips.copy()
    tips_display['tip_percent'] = (tips_display['tip'] / tips_display['total_bill'] * 100).round(1)
    
    # Configure the columns
    column_config = {
        'total_bill': st.column_config.NumberColumn(
            'Bill Amount',
            help='Total bill amount in dollars',
            format='$%.2f'
        ),
        'tip': st.column_config.NumberColumn(
            'Tip Amount',
            help='Tip amount in dollars', 
            format='$%.2f'
        ),
        'tip_percent': st.column_config.NumberColumn(
            'Tip %',
            help='Tip as percentage of bill',
            format='%.1f%%'
        ),
        'sex': st.column_config.SelectboxColumn(
            'Gender',
            help='Customer gender',
            width='small',
            options=['Male', 'Female']
        ),
        'smoker': st.column_config.CheckboxColumn(
            'Smoker',
            help='Whether the customer is a smoker'
        ),
        'day': st.column_config.SelectboxColumn(
            'Day',
            help='Day of the week',
            width='small',
            options=['Sun', 'Sat', 'Fri', 'Thur']
        ),
        'time': st.column_config.SelectboxColumn(
            'Time',
            help='Time of day',
            width='small',
            options=['Lunch', 'Dinner']
        ),
        'size': st.column_config.NumberColumn(
            'Party Size',
            help='Number of people in the dining party',
            min_value=1,
            max_value=6
        )
    }

    st.dataframe(
        tips_display,
        column_config=column_config,
        hide_index=True
    )

    st.markdown("### Daily Tips Data Visualization")
    
    # Create simple visualization dataframe with 4 days

    viz_data = pd.DataFrame({
        'day': ['Thur', 'Fri', 'Sat', 'Sun'],
        'area_data': [
            tips_display[tips_display['day'] == 'Thur']['total_bill'].tolist(),
            tips_display[tips_display['day'] == 'Fri']['total_bill'].tolist(),
            tips_display[tips_display['day'] == 'Sat']['total_bill'].tolist(),
            tips_display[tips_display['day'] == 'Sun']['total_bill'].tolist()
        ],
        'line_data': [
            tips_display[tips_display['day'] == 'Thur']['tip'].tolist(),
            tips_display[tips_display['day'] == 'Fri']['tip'].tolist(),
            tips_display[tips_display['day'] == 'Sat']['tip'].tolist(),
            tips_display[tips_display['day'] == 'Sun']['tip'].tolist()
        ],
        'bar_data': [
            tips_display[tips_display['day'] == 'Thur']['size'].tolist(),
            tips_display[tips_display['day'] == 'Fri']['size'].tolist(),
            tips_display[tips_display['day'] == 'Sat']['size'].tolist(),
            tips_display[tips_display['day'] == 'Sun']['size'].tolist()
        ]
    })
    # Set observed=False to retain current behavior for pandas operations
    st.dataframe(viz_data)
    pd.options.mode.copy_on_write = False

    # Calculate progress as percentage (0-100%)
    max_bill = max(tips_display['total_bill'])
    viz_data['progress'] = viz_data['area_data'].apply(lambda x: (sum(x)/len(x) / max_bill) * 100)

    # Configure visualization columns
    viz_config = {
        'area_data': st.column_config.AreaChartColumn(
            'Bills Distribution',
            y_min=0,
            y_max=max(tips_display['total_bill'])
        ),
        'line_data': st.column_config.LineChartColumn(
            'Tips Distribution',
            y_min=0,
            y_max=max(tips_display['tip'])
        ),
        'bar_data': st.column_config.BarChartColumn(
            'Party Sizes'
        ),
        'progress': st.column_config.ProgressColumn(
            'Avg Bill Progress',
            help='Average bill as percentage of maximum bill',
            format='%.1f%%',
            min_value=0,
            max_value=100
        )
    }

    st.dataframe(
        viz_data,
        column_config=viz_config,
        hide_index=True
    )
    

if __name__ == "__main__":
    main()
