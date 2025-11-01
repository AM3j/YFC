import streamlit as st
import pandas as pd
import altair as alt


st.title("Indicators of KSA")
st.text("This page presents forecasts for several key indicators in Saudi Arabia."
        " data for additional indicators is available and will be added soon.")

@st.cache_data
def load_data(path):
    """To load data from path"""
    df = pd.read_pickle(path)
    return df


# Simulate ggplot style from matplotlib
@alt.theme.register('ggplot_custom', enable=True)
def ggplot_custom():
    return alt.theme.ThemeConfig({
        "config": {
            "background": "white",
            "view": {
                "stroke": "transparent",
                "fill": "#E5E5E5",  # gray area only between axes

            },
            "axis": {
                "domain": True,
                "grid": True,
                "gridColor": "white",
                "tickColor": "black",
                "labelColor": "black",
                "titleColor": "black",
            },
            "title": {
                "anchor": "middle",  # center title
                "fontSize": 16,
                "font": "Arial",
                "color": "black",
            },
            "legend": {
                "titleColor": "black",
                "labelColor": "black",
                "titleFontWeight": "bold"
            }
        }
    })

@st.cache_data
def plot_series_altair(df, preds, xlabel="Date", ylabel="y", title=None):
    """To plot time series with predictions and intervals"""

    # Historical data to plot
    historical_line = alt.Chart(df).transform_calculate(
        category='"Actual"'
    ).mark_line(strokeWidth=2).encode(
        x=alt.X('ds:T', title=xlabel, scale=alt.Scale(nice={"interval": 'year', 'step': 2})),
        y=alt.Y('y:Q', title=f'{ylabel}'),
        color=alt.Color('category:N',
                        scale=alt.Scale(domain=["Actual"], range=["black"]),
                        legend=alt.Legend(title="")),
        tooltip=[
            alt.Tooltip('year:N', title=xlabel),
            alt.Tooltip('y:Q', title=ylabel, format='.2f')
        ]
    )


    # Forecasting data
    prediction_line = alt.Chart(preds).transform_calculate(
        category='"Prediction"'
    ).mark_line(strokeWidth=3).encode(
        x='ds:T',
        y='model:Q',
        color=alt.Color('category:N',
                        scale=alt.Scale(domain=["Prediction"], range=["#ff4800"]),
                        legend=alt.Legend(title="")),
        tooltip=[alt.Tooltip('year:N', title=xlabel),
                 alt.Tooltip('model:Q', title='Prediction', format='.2f'),
                 alt.Tooltip('model-lo-95:Q', title='Lower 95%', format='.2f'),
                 alt.Tooltip('model-lo-80:Q', title='Lower 80%', format='.2f'),
                 alt.Tooltip('model-hi-80:Q', title='Upper 80%', format='.2f'),
                 alt.Tooltip('model-hi-95:Q', title='Upper 95%', format='.2f')
                 ]
    )

    # 95 prediction interval
    band_95 = alt.Chart(preds).transform_calculate(
        category='"95% Prediction Interval"'
    ).mark_area(opacity=0.4).encode(
        x='ds:T',
        y='model-lo-95:Q',
        y2='model-hi-95:Q',
        color=alt.Color('category:N',
                        scale=alt.Scale(domain=["95% Prediction Interval"],
                                        range=["#ffaa00"]),
                        legend=alt.Legend(title="Legend")),
        tooltip=[]
    )

    # 80 prediction interval
    band_80 = alt.Chart(preds).transform_calculate(
        category='"80% Prediction Interval"'
    ).mark_area(opacity=0.4).encode(
        x='ds:T',
        y='model-lo-80:Q',
        y2='model-hi-80:Q',
        color=alt.Color('category:N',
                        scale=alt.Scale(domain=["80% Prediction Interval"],
                                        range=["#ff6d00"]),
                        legend=alt.Legend(title="")),
        tooltip=[]

    )

    # Combine charts and show legend
    chart = alt.layer(band_95, band_80, historical_line, prediction_line).resolve_scale(
        color='independent'  # keep colors distinct
    ).properties(
        title={
            'text': title,
            "anchor": "middle",  # center title
            "fontSize": 16,
            "font": "Arial",
            "color": "black",
        },
    )
    return chart



# Container to contain GDP & Real GDP in two tabs
with st.container(border=True):
    tab1, tab2 = st.tabs(['Nominal', 'Real'])

    with tab1:
        # GDP Dataset
        gdp = load_data("data/gdp.pkl")
        preds_gdp = load_data("data/preds_gdp.pkl")

        st.altair_chart(plot_series_altair(gdp, preds_gdp, xlabel="Year", ylabel="GDP (Billions $)",
                                           title="GDP"), use_container_width=True)

    with tab2:
        # Real GDP Dataset
        real_gdp = load_data("data/real_gdp.pkl")
        real_preds_gdp = load_data("data/real_preds_gdp.pkl")

        st.altair_chart(plot_series_altair(real_gdp, real_preds_gdp,
                                   xlabel="Year", ylabel='GDP (Billions $)',
                                   title='Real GDP (Chain-linked, 2023=100)'), use_container_width=True)

st.divider()

# Container to contain GDP Per Capita & Real GDP Per Capita in two tabs
with st.container(border=True):
    tab1, tab2 = st.tabs(['Nominal', 'Real'])
    with tab1:
        # GDP Per Capita Dataset
        gdp_perC = load_data("data/gdp_perC.pkl")
        preds_gdp_perC = load_data("data/preds_gdp_perC.pkl")

        st.altair_chart(plot_series_altair(gdp_perC, preds_gdp_perC,
                                           xlabel='Year', ylabel='GDP Per Capita $',
                                           title='GDP Per Capita'), use_container_width=True)

    with tab2:
        # Real GDP Per Capita Dataset
        real_gdp_perC = load_data("data/real_gdp_perC.pkl")
        real_preds_gdp_perC = load_data("data/real_preds_gdp_perC.pkl")

        st.altair_chart(plot_series_altair(real_gdp_perC, real_preds_gdp_perC,
                                           xlabel="Year", ylabel="GDP Per Capita $",
                                           title='Real GDP Per Capita (Chain-linked, 2023=100)'),
                                           use_container_width=True)


st.divider()

# Population
# Population dataset
preds_pop = load_data("data/preds_population.pkl")
population = load_data("data/population.pkl")

# Container to contain population
with st.container(border=True):
    st.altair_chart(plot_series_altair(population, preds_pop,
                                       xlabel="Year", ylabel="Population (Millions)",
                                       title="Population"), use_container_width=True)


