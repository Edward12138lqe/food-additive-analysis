# China Food Additive Industry Investment Analysis Tool
https://github.com/edward12138lqe/food-additive-analysis

or

git clone https://github.com/edward12138lqe/food-additive-analysis.git

## 1. Problem & Target User

Retail investors and equity analysts lack a centralized, interactive tool to compare financial performance and market positioning of publicly listed food additive companies in China. Key information — such as revenue, profitability margins, ROE, and segment market shares — is scattered across annual reports, third‑party research, and stock exchange filings. Extracting and normalizing this data manually is time‑consuming and error‑prone, often leading to incomplete or inconsistent cross‑company comparisons.

Moreover, existing free tools (e.g., stock screeners) typically provide only basic financial ratios without industry‑specific context (e.g., regulatory impact, segment growth trends, or raw material price exposure). This gap prevents investors from making informed, data‑driven decisions.

**Target audience**:
- Individual investors seeking a quick, visual overview of 2025 financial metrics across major food additive companies.
- Equity research associates who need to benchmark companies (e.g., Fufeng Group vs. Angel Yeast) and identify outliers in profitability or growth.
- Finance and accounting students learning to apply Python (pandas, plotly, streamlit) to real‑world financial analysis.

**Value Proposition of This Tool**:
- One‑click comparison of revenue, net income, net margin, ROE, and YoY growth for six leading companies.
- Industry context – market size estimates, product segment shares, and key regulatory drivers (GB 2760‑2024, Healthy China 2030).
- Interactive & transparent – users can select any company, view its metrics, and understand the underlying data sources (links provided).
- Reproducible – all code and data are publicly available; the dashboard runs locally after cloning the repository.

## 2. Data Sources & Collection

All data are real, collected from publicly available sources in April 2026. The dataset focuses on **the year 2025** (latest reported or forecast data) due to annual report release cycles.

| Dataset | Source | Access Date | Raw Data Link | Key Variables |
|---------|--------|-------------|---------------|----------------|
| Industry market size | ReportsWorld, Mordor Intelligence, Beizhe Consulting | 2026‑04‑22 | [ReportsWorld](https://www.reportsworld.com) / [Mordor Intelligence](https://www.mordorintelligence.com) | China market size (CNY Billion), Global market size (USD Billion) |
| Company financials (2025) | 2025 annual reports (Jinhe Industrial, Angel Yeast, Bailong Chuanyuan, Fufeng Group, Huabao Flavors, Xinghu Science) | 2026‑04‑22 | [Jinhe](https://www.cninfo.com.cn) / [Angel Yeast](https://www.angelyeast.com) / [Bailong](http://www.blcy.com) | Revenue, Net Income, ROE, Gross Margin, Net Margin, YoY Growth |
| Market segments | Zhiyan Consulting industry report | 2026‑04‑22 | [Zhiyan Report](https://www.chyxx.com) | Product segment market shares |
| Industry drivers | Public policies & white papers (GB 2760‑2024, Healthy China 2030) | 2026‑04‑22 | [GB 2760‑2024](http://www.nhc.gov.cn) | Regulatory, health trend, urbanization, global expansion |

> **Note**: Some companies (e.g., Bailong Chuanyuan, Fufeng Group) did not report all financial metrics (e.g., ROE, Gross Margin) in their 2025 summaries. Missing values are treated as `NaN` in the analysis.

## 3. Methods

The analysis is implemented in Python using `pandas` for data manipulation and `plotly` for visualization. The key steps are:

- **Data loading**: `pd.read_csv("data/industry_overview.csv")` reads market size data; similarly for financials, segments, and drivers.

- **Data cleaning**:
  - Convert columns to numeric: `pd.to_numeric(..., errors='coerce')` ensures missing or malformed entries become `NaN`.
  - Drop rows with missing revenue: `df_fin.dropna(subset=['Revenue_2025_CNY_Billion'])`.

- **Data transformation**:
  - Calculate net margin if not provided: `df_fin['NetMargin_Pct'] = (df_fin['NetIncome'] / df_fin['Revenue']) * 100`.
  - Rank companies by ROE or net margin using `df.sort_values()`.

- **Analysis**:
  - Identify highest revenue company via `df_fin.loc[df_fin['Revenue'].idxmax()]`.
  - Identify largest market segment using `df_seg.loc[df_seg['MarketShare_Percent'].idxmax()]`.

- **Visualization** (using `plotly.express`):
  - Revenue bar chart: `px.bar(df_fin, x='Company', y='Revenue_2025_CNY_Billion', title='...')`.
  - ROE bar chart (if available): `px.bar(df_roe, x='Company', y='ROE_2025_Percent')`.
  - Segment pie chart: `px.pie(df_seg, values='MarketShare_Percent', names='ProductSegment')`.

- **Streamlit dashboard**:
  - Load data with `@st.cache_data` for performance.
  - Create interactive filters using `st.sidebar.selectbox()` and `st.multiselect()`.
  - Display metrics with `st.metric()` and charts with `st.plotly_chart()`.

All code is available in `app.py` and the accompanying Jupyter notebook `food_additive_analysis.ipynb`.

**Key libraries**: `pandas` (data manipulation), `plotly` (visualization), `streamlit` (interactive UI).

## 4. Key Findings (2025)

Based on the 2025 financial and industry data, the following conclusions are drawn:

### 4.1 Market Size Discrepancy Across Research Firms
- **ReportsWorld** estimates China's food additive market at **2,232.6 billion CNY** (≈18.3 billion USD) in 2025.
- **Beizhe Consulting** gives a higher figure of **2,700.9 billion CNY** (no USD equivalent provided).
- **Implication**: Investors should compare multiple sources; the true market size likely lies between these estimates. The industry remains large but methodology differences cause significant variance.

### 4.2 Revenue Concentration: Fufeng Group Dominates, Followed by Angel Yeast
- **Fufeng Group** (HK‑listed) reported the highest revenue: **278.79 billion CNY** – nearly twice that of the second‑largest company.
- **Angel Yeast** (A‑share) ranked second with **167.29 billion CNY**.
- **Jinhe Industrial** (sweeteners) had **49.11 billion CNY**, while smaller players like Bailong Chuanyuan (13.79B) and Huabao Flavors (13.38B) are niche competitors.
- **Conclusion**: The industry is highly concentrated at the top; Fufeng’s scale advantage may offer cost leadership, but investors should examine profitability alongside revenue.

### 4.3 Profitability Leaders: Bailong Chuanyuan Achieves Highest Net Margin, Angel Yeast Leads in ROE
- **Bailong Chuanyuan** (probiotics & dietary fiber) achieved an outstanding net margin of **26.76%** – the highest among all six companies. However, its ROE is missing from the 2025 report, suggesting possible data disclosure gaps.
- **Angel Yeast** reported the best ROE at **13.51%** and a solid net margin of **9.23%**, indicating efficient capital use and healthy profitability.
- **Fufeng Group**, despite its revenue leadership, had a net margin of only **8.84%** (moderate) and no ROE disclosed.
- **Jinhe Industrial** showed a net margin of **7.06%** and ROE of **4.60%** – both relatively low, reflecting competitive pressure in the sweetener segment or higher costs.
- **Key insight**: High revenue does not guarantee high profitability. Bailong’s niche focus yields superior margins, while scale leaders like Fufeng may operate on thinner margins.

### 4.4 Segment Composition: Sweeteners Remain the Largest, but Growth Outlook Favors Natural Additives
- **Sweeteners** account for **25%** of the market, driven by sugar reduction policies and rising demand for natural alternatives.
- **Flavors & Fragrances** follow at **20%**, with stable growth and domestic substitution trends.
- **Preservatives** (15%) and **Colorants** (10%) are essential but slower‑growing segments.
- **Natural additive share** has exceeded **50%** of total demand, accelerating due to consumer health awareness and regulations like GB 2760‑2024.
- **Investment implication**: Companies with exposure to natural sweeteners (e.g., Jinhe) and functional ingredients (e.g., Bailong) may benefit from long‑term tailwinds, while traditional chemical additives face slower growth.

### 4.5 Key Growth Drivers Align with Policy and Consumer Trends
- **Regulation**: The new GB 2760‑2024 standard imposes stricter limits on synthetic additives, pushing reformulation toward natural ingredients.
- **Health trend**: Over 50% of consumers now prefer clean‑label products – a structural shift.
- **Urbanization**: 66.16% urban population drives demand for packaged and convenience foods, indirectly boosting additive consumption.
- **Export expansion**: Companies like Fufeng and Jinhe are actively expanding overseas, reducing domestic market dependency.
- **Synthetic biology**: Emerging as a key technology for cost‑effective fermentation‑based additives, likely to disrupt traditional extraction methods.

### 4.6 Summary of Investment‑Relevant Conclusions
- **Scale vs. profitability**: Fufeng Group offers revenue scale but thin margins; Bailong Chuanyuan offers niche high‑margin exposure.
- **Regulatory winner**: Natural additive producers (e.g., Jinhe, Bailong) are positioned to benefit from GB 2760‑2024.
- **Market concentration**: The top two players (Fufeng, Angel Yeast) capture a large revenue share, but profitability is more dispersed.
- **Missing data risk**: Several companies did not disclose ROE or gross margin in 2025 – a limitation for cross‑comparison.

## 5. How to Run Locally (Marker Instructions)

To replicate the analysis and run the interactive dashboard on your local machine:

```bash
# Clone the repository
git clone https://github.com/edward12138lqe/food-additive-analysis.git
# Enter the project folder
cd food-additive-analysis
# Install dependencies
pip install -r requirements.txt
# Launch the Streamlit app
streamlit run app.py
Alternative: If you don't have Git installed, click the green "Code" button and select "Download ZIP".
Extract the folder, then follow the same steps above. But remember : the files' name needs to be changed to food_additive_analysis











## 6. Product Link (Primary Submission)
GitHub repository (required): https://github.com/edward12138lqe/food-additive-analysis










## 7. Limitations & Future Improvements
Limitations
Incomplete 2025 data: Several companies lack ROE or gross margin figures, limiting direct comparability.
Single‑year snapshot: No historical trends (e.g., 2020‑2024) are available; growth analysis is restricted.
Source inconsistency: Market size estimates vary across research firms – users should interpret with caution.
Limited coverage: Only six representative companies; a broader index would be more comprehensive.

Future improvements
Collect historical data (2020‑2024) to enable trend analysis and CAGR calculation.
Integrate yfinance API for real‑time stock prices and valuation metrics (PE, PB).
Add data imputation or explicit flags for missing values.
Expand company list to include more A‑share and HK‑listed food additive firms.
Disclaimer: This tool is for educational purposes only and does not constitute investment advice. Data accuracy is not guaranteed.
