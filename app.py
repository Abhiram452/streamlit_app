import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Set page configuration
st.set_page_config(page_title="Executive Summary Dashboard", layout="wide")

# Add custom CSS styles
st.markdown("""
    <style>
        .header {
            font-size: 26px;
            font-weight: bold;
            color: #4A4A4A;
        }
        .sub-header {
            font-size: 22px;
            font-weight: bold;
            color: #4A4A4A;
        }
        .metric {
            font-size: 20px;
            font-weight: bold;
        }
        .metric-label {
            font-size: 16px;
            color: #6B6B6B;
        }
        .container {
            padding: 10px;
            border: 1px solid #E5E5E5;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .selectbox {
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #E5E5E5;
            margin-bottom: 10px;
        }
        .sidebar .selectbox {
            padding: 10px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and tabs
st.markdown('<div class="header">Executive Summary</div>', unsafe_allow_html=True)
tabs = ["Descriptive", "Diagnostics", "Predictive & Prescriptive"]
selected_tab = st.selectbox("Select a tab", tabs, key="main_tabs", format_func=lambda x: f"<div class='selectbox'>{x}</div>")

# Sub-tabs for Descriptive tab
if selected_tab == "Descriptive":
    sub_tabs = ["Executive Summary", "Category Summary", "Regional Summary"]
    selected_sub_tab = st.selectbox("Select a sub-tab", sub_tabs, key="sub_tabs", format_func=lambda x: f"<div class='selectbox'>{x}</div>")

    if selected_sub_tab == "Executive Summary":
        st.markdown('<div class="sub-header">Executive Summary</div>', unsafe_allow_html=True)
        st.markdown("### Key Metrics")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown('<div class="container"><div class="metric">423K</div><div class="metric-label">Sell out Volume</div><div class="metric-label">24% YOY</div></div>', unsafe_allow_html=True)
        col2.markdown('<div class="container"><div class="metric">R$57.168K</div><div class="metric-label">Sell out Value</div><div class="metric-label">38% YOY</div></div>', unsafe_allow_html=True)
        col3.markdown('<div class="container"><div class="metric">4.536K</div><div class="metric-label">Sell out Units</div><div class="metric-label">4% YOY</div></div>', unsafe_allow_html=True)
        col4.markdown('<div class="container"><div class="metric">R$12.60</div><div class="metric-label">Avg Price Per Unit</div><div class="metric-label">32% YOY</div></div>', unsafe_allow_html=True)
        
        col1.markdown('<div class="container"><div class="metric">259K</div><div class="metric-label">Sell out Volume (Own Brand)</div><div class="metric-label">5% YOY</div></div>', unsafe_allow_html=True)
        col2.markdown('<div class="container"><div class="metric">R$36.072K</div><div class="metric-label">Sell out Value (Own Brand)</div><div class="metric-label">19% YOY</div></div>', unsafe_allow_html=True)
        col3.markdown('<div class="container"><div class="metric">3.442K</div><div class="metric-label">Sell out Units (Own Brand)</div><div class="metric-label">-2% YOY</div></div>', unsafe_allow_html=True)
        col4.markdown('<div class="container"><div class="metric">R$10.48</div><div class="metric-label">Avg Price Per Unit (Own Brand)</div><div class="metric-label">10% YOY</div></div>', unsafe_allow_html=True)
        
        # Charts
        st.markdown('<div class="sub-header">Volume Market Share</div>', unsafe_allow_html=True)
        volume_market_share_data = pd.DataFrame({
            'Month': pd.date_range(start='1/1/2022', periods=12, freq='M'),
            'Manufacturer 1': np.random.rand(12) * 4 + 2,
            'Manufacturer 2': np.random.rand(12) * 3 + 1,
            'Manufacturer 3': np.random.rand(12) * 2
        })
        st.line_chart(volume_market_share_data.set_index('Month'))
        
        st.markdown('<div class="sub-header">Value Sales - Quarter Analysis</div>', unsafe_allow_html=True)
        quarter_analysis_data = pd.DataFrame({
            'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
            'Manufacturer 1': [5000000, 10000000, 15000000, 20000000],
            'Manufacturer 2': [3000000, 7000000, 11000000, 15000000],
            'Manufacturer 3': [2000000, 4000000, 6000000, 8000000]
        })
        st.bar_chart(quarter_analysis_data.set_index('Quarter'))
        
        st.markdown('<div class="sub-header">Value Sales - Region wise</div>', unsafe_allow_html=True)
        region_data = pd.DataFrame({
            'Region': ['AREA 1', 'AREA 2', 'AREA 3'],
            'Value': [41, 29, 30]
        })
        region_pie_chart = alt.Chart(region_data).mark_arc().encode(
            theta=alt.Theta(field="Value", type="quantitative"),
            color=alt.Color(field="Region", type="nominal"),
            tooltip=['Region', 'Value']
        )
        st.altair_chart(region_pie_chart, use_container_width=True)
        
        st.markdown('<div class="sub-header">Value Sales - Channel wise</div>', unsafe_allow_html=True)
        channel_data = pd.DataFrame({
            'Channel': ['ECom', 'GT', 'MT'],
            'Value': [18, 24, 58]
        })
        channel_pie_chart = alt.Chart(channel_data).mark_arc().encode(
            theta=alt.Theta(field="Value", type="quantitative"),
            color=alt.Color(field="Channel", type="nominal"),
            tooltip=['Channel', 'Value']
        )
        st.altair_chart(channel_pie_chart, use_container_width=True)
        
        st.markdown('<div class="sub-header">Value Sales - Performance over time</div>', unsafe_allow_html=True)
        performance_data = pd.DataFrame({
            'Month': pd.date_range(start='1/1/2022', periods=12, freq='M'),
            'Manufacturer 1': np.random.rand(12) * 4 + 2,
            'Manufacturer 2': np.random.rand(12) * 3 + 1,
            'Manufacturer 3': np.random.rand(12) * 2
        })
        st.line_chart(performance_data.set_index('Month'))

# Filters
st.sidebar.header("Filters")
st.sidebar.selectbox("Year", [2022, 2023], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Quarter", ["All", "Q1", "Q2", "Q3", "Q4"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Month", ["All", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Country", ["All", "Country 1", "Country 2", "Country 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Region", ["All", "Region 1", "Region 2", "Region 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Channel", ["All", "Channel 1", "Channel 2", "Channel 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Manufacturer", ["All", "Manufacturer 1", "Manufacturer 2", "Manufacturer 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Division", ["All", "Division 1", "Division 2", "Division 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Brand", ["All", "Brand 1", "Brand 2", "Brand 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Category", ["All", "Category 1", "Category 2", "Category 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
st.sidebar.selectbox("Segment", ["All", "Segment 1", "Segment 2", "Segment 3"], format_func=lambda x: f"<div class='selectbox'>{x}</div>")
