import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="China Food Additive Investment Tool", page_icon="📈", layout="wide")

st.title("📈 China Food Additive Industry – Investment Analysis Tool")
st.markdown("**Target users**: Equity analysts & investors focusing on A‑share food additive companies.")

@st.cache_data
def load_data():
    industry = pd.read_csv("data/industry_overview.csv")
    financial = pd.read_csv("data/company_financials.csv")
    segments = pd.read_csv("data/market_segments.csv")
    drivers = pd.read_csv("data/industry_drivers.csv")
    return industry, financial, segments, drivers

df_ind, df_fin, df_seg, df_drv = load_data()

st.sidebar.header("🔍 Company Analysis")
company_list = df_fin["Company"].tolist()
selected_company = st.sidebar.selectbox("Select a company", company_list)

st.sidebar.markdown("---")
st.sidebar.info("Data sources: Company annual reports (2025), Mordor Intelligence, ReportsWorld, Beizhe Consulting.")

st.header("1. Market Size Overview")
col1, col2, col3 = st.columns(3)
col1.metric("China 2025", "~2,232B CNY", help="ReportsWorld")
col2.metric("Global 2030F", "~24.6B USD", delta="CAGR 6.08%", help="Mordor Intelligence")
col3.metric("Global 2032F", "~11,516B CNY", delta="CAGR 5.05%", help="Beizhe Consulting")

china_data = df_ind[df_ind["Source"].str.contains("ReportsWorld|Beizhe", na=False)]
global_data = df_ind[df_ind["Source"].str.contains("Mordor", na=False)]

fig_mkt = make_subplots(rows=1, cols=2, subplot_titles=("China Market (CNY Billion)", "Global Market (USD Billion)"))
fig_mkt.add_trace(go.Bar(x=china_data["Year"], y=china_data["MarketSize_CNY_Billion"], name="China", marker_color="#1f77b4"), row=1, col=1)
fig_mkt.add_trace(go.Bar(x=global_data["Year"], y=global_data["MarketSize_USD_Billion"], name="Global", marker_color="#ff7f0e"), row=1, col=2)
fig_mkt.update_layout(height=400, showlegend=False)
st.plotly_chart(fig_mkt, use_container_width=True)

st.info("💡 **Key insight**: China's food additive market is driven by urbanization (66.16%) and rising demand for natural ingredients. Natural & functional additives now exceed 50% of the market.")

st.header("2. Company Financial Snapshot")
comp = df_fin[df_fin["Company"] == selected_company].iloc[0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue (2025)", f"{comp['Revenue_2025_CNY_Billion']}B CNY", delta=f"{comp['YoY_Revenue_Growth']}%")
c2.metric("Net Income", f"{comp['NetIncome_2025_CNY_Billion']}B CNY")
c3.metric("Net Margin", f"{comp['NetMargin_2025_Percent']}%")
if pd.notna(comp['ROE_2025_Percent']):
    c4.metric("ROE", f"{comp['ROE_2025_Percent']}%")
else:
    c4.metric("ROE", "N/A")

st.subheader("ROE Comparison Across Peers")
df_roe = df_fin[df_fin["ROE_2025_Percent"].notna() & (df_fin["ROE_2025_Percent"] > 0)]
if not df_roe.empty:
    fig_roe = px.bar(df_roe, x="Company", y="ROE_2025_Percent", text="ROE_2025_Percent", title="Return on Equity (2025)", color="ROE_2025_Percent")
    st.plotly_chart(fig_roe, use_container_width=True)

st.subheader("Net Margin Comparison")
df_nm = df_fin[df_fin["NetMargin_2025_Percent"].notna()]
if not df_nm.empty:
    fig_nm = px.bar(df_nm, x="Company", y="NetMargin_2025_Percent", text="NetMargin_2025_Percent", title="Net Margin (2025)", color="NetMargin_2025_Percent")
    st.plotly_chart(fig_nm, use_container_width=True)

st.header("3. Market Segment Breakdown")
fig_seg = px.pie(df_seg, values="MarketShare_Percent", names="ProductSegment", title="China Food Additive Market by Product Segment (2025)", hole=0.35)
st.plotly_chart(fig_seg, use_container_width=True)

with st.expander("See segment growth outlook"):
    for _, row in df_seg.iterrows():
        st.write(f"**{row['ProductSegment']}** ({row['MarketShare_Percent']}%): {row['GrowthOutlook']}")

st.header("4. Industry Drivers & Regulatory Updates")
st.subheader("Key Growth Drivers")
for _, row in df_drv.iterrows():
    st.markdown(f"- **{row['Driver']}**: {row['Description']}")

st.subheader("Latest Policies")
st.markdown("""
- **GB 2760-2024** – Stricter additive classification and usage limits, forcing product reformulation.
- **Food Additive Production License Review (2025)** – Higher entry barriers.
- **"Healthy China 2030"** – Sugar reduction policy boosting natural sweetener demand.
""")

st.header("5. Investment Summary")
st.markdown(f"""
**{selected_company} ({comp['StockCode']})** – Main business: {comp['MainBusiness']}

| Metric | Value | Implication |
|--------|-------|--------------|
| Revenue scale | {comp['Revenue_2025_CNY_Billion']}B CNY | {'Largest among peers' if comp['Revenue_2025_CNY_Billion'] == df_fin['Revenue_2025_CNY_Billion'].max() else 'Mid-tier'} |
| Net income | {comp['NetIncome_2025_CNY_Billion']}B CNY | {'Strong profitability' if comp['NetIncome_2025_CNY_Billion'] > 10 else 'Moderate'} |
| Net margin | {comp['NetMargin_2025_Percent']}% | {'High efficiency' if comp['NetMargin_2025_Percent'] > 15 else 'Average'} |
| Revenue growth | {comp['YoY_Revenue_Growth']}% | {'High growth' if comp['YoY_Revenue_Growth'] > 10 else 'Stable/negative'} |
""")

st.caption("⚠️ Disclaimer: This tool is for educational purposes only. Not investment advice.")