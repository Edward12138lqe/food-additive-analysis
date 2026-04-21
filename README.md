\# China Food Additive Industry Investment Analysis Tool



\## 1. Problem \& User

Equity analysts and retail investors need a quick, interactive way to compare the latest financial metrics of A-share and HK-listed food additive companies, as well as to understand the overall industry market size and growth drivers. This tool provides an interactive dashboard focusing on the most recent available data (2025) and future market forecasts.



\*\*Target users\*\*: Individual investors, equity research associates, and students learning financial analysis.



\## 2. Data

All data are real and collected from publicly available sources. Due to the availability of annual reports, the current dataset focuses on the year 2025 (latest reported or forecast data) and industry projections.



| Dataset | Source | Access Date | Key Fields |

|---------|--------|-------------|-------------|

| Company financials (2025) | Company annual reports (Jinhe Industrial, Angel Yeast, Bailong Chuanyuan, Fufeng Group, Huabao Flavors, Xinghu Science) | 2026-04-22 | Revenue (CNY Billion), Net Income, ROE, Gross Margin, Net Margin, YoY Revenue Growth, Main Business |

| Industry market size | ReportsWorld, Mordor Intelligence, Beizhe Consulting | 2026-04-22 | China market size (CNY Billion) for 2025, Global market size (USD Billion) for 2025, 2030, 2032 |

| Market segments | Industry research (Zhiyan Consulting) | 2026-04-22 | Product segment shares (Sweeteners 25%, Flavors 20%, Preservatives 15%, Colorants 10%, Others 30%) |

| Industry drivers | Public industry reports | 2026-04-22 | Regulation (GB 2760-2024), health trends, urbanization, global expansion, synthetic biology |



All CSV files are stored in the `data/` folder.



\## 3. Methods

The analysis follows a standard data workflow:



1\. \*\*Data Collection\*\*: CSV files were manually compiled from annual reports and industry research.

2\. \*\*Data Cleaning\*\*: Python pandas was used to handle missing values (e.g., empty ROE cells) and ensure correct data types.

3\. \*\*Data Transformation\*\*: No additional derived metrics were needed for this snapshot analysis.

4\. \*\*Analysis\*\*: Side-by-side comparison of company financials, market size trends, and segment shares.

5\. \*\*Visualization\*\*: Interactive charts (bar charts, pie charts) created with Plotly.

6\. \*\*Dashboard\*\*: Streamlit provides a web-based interactive interface for users to select companies and view key metrics.



Key Python libraries used:

\- `pandas` – data manipulation

\- `plotly` – interactive visualizations

\- `streamlit` – web application framework



\## 4. Key Findings

\- \*\*Market size\*\*: China food additive market reached approximately 2,232B CNY in 2025, with global market at $18.3B USD (ReportsWorld). Other sources estimate China market at 2,701B CNY (Beizhe Consulting).

\- \*\*Global forecast\*\*: Mordor Intelligence projects global market to reach $24.6B USD by 2030 and $27.9B USD by 2035.

\- \*\*Revenue leaders\*\*: Among the six companies, Fufeng Group has the largest revenue (278.79B CNY), followed by Angel Yeast (167.29B CNY).

\- \*\*Profitability leaders\*\*: Bailong Chuanyuan shows the highest net margin (26.76%), while Angel Yeast has the highest ROE (13.51%).

\- \*\*Segment dominance\*\*: Sweeteners (25%) and Flavors \& Fragrances (20%) are the largest market segments.



\## 5. How to Run Locally

To run this tool on your own computer, follow these steps:



```bash

\# 1. Clone the repository

git clone https://github.com/edward12138lqe/food-additive-analysis.git



\# 2. Navigate into the project folder

cd food-additive-analysis



\# 3. Install required dependencies

pip install -r requirements.txt



\# 4. Run the Streamlit app

streamlit run app.py

