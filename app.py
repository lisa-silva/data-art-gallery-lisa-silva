# app.py – The Art of Data (2025 Aesthetic Edition)
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="The Art of Data", layout="wide", page_icon="🎨")
st.title("The Art of Data — 2025 Aesthetic Collection")
st.markdown("Nine different chart masterpieces — all live, interactive, and beautiful.")

df = px.data.gapminder().query("year==2007")
sales = pd.DataFrame({
    "month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "2024": np.random.randint(80, 300, 12),
    "2025": np.random.randint(100, 350, 12)
})

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("3D Globe Population")
    fig = px.scatter_geo(df, locations="iso_alpha", size="pop", color="continent",
                         hover_name="country", projection="orthographic",
                         color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_layout(height=400, margin=dict(l=0,r=0,b=0,t=0))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Spiral Galaxy Chart")
    theta = np.linspace(0, 10*np.pi, 1000)
    r = theta**2
    fig = go.Figure(go.Scatterpolar(r=r, theta=np.degrees(theta), mode='lines',
                                    line=dict(color='#FF4B4B', width=3)))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False),
                                 angularaxis=dict(direction="clockwise")),
                      showlegend=False, height=400, paper_bgcolor="black", plot_bgcolor="black")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Liquid Fill Gauge")
    fig = go.Figure(go.Indicator(mode="gauge+number", value=87,
                                 gauge={'axis': {'range': [0,100]},
                                        'bar': {'color': "#00d4ff"},
                                        'bgcolor': "rgba(0,0,0,0)",
                                        'borderwidth': 2,
                                        'bordercolor': "#00d4ff"},
                                 title={'text': "Success Rate"}))
    fig.update_layout(height=300, paper_bgcolor="black", font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Moon Phase Sankey")
    fig = go.Figure(go.Sankey(
        node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5),
                  label=["Leads", "MQL", "SQL", "Won", "Lost"],
                  color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57"]),
        link=dict(source=[0,0,1,1,2], target=[1,2,3,4,3],
                  value=[65,35,45,20,40],
                  color=["rgba(255,107,107,0.4)", "rgba(78,205,196,0.4)",
                         "rgba(69,183,209,0.4)", "rgba(254,202,87,0.4)",
                         "rgba(150,206,180,0.4)"])
    ))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Radar Constellation")
    categories = ['Speed','Reliability','Cost','UX','AI','Scalability']
    fig = go.Figure()
    for i in range(5):
        fig.add_trace(go.Scatterpolar(r=np.random.randint(70,100,6), theta=categories,
                                      fill='toself', name=f"Model {i+1}"))
    fig.update_layout(polar=dict(radialaxis=dict(visible=False)),
                      showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Bullseye Accuracy")
    fig = go.Figure(go.Scatter(x=np.random.randn(200), y=np.random.randn(200),
                               mode='markers', marker=dict(color=np.random.randn(200),
                                                           colorscale='Viridis', size=12)))
    fig.update_layout(shapes=[dict(type="circle", xref="x", yref="y",
                                   x0=-3, y0=-3, x1=3, y1=3, line_color="white")],
                      height=400, paper_bgcolor="black", plot_bgcolor="black")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.subheader("Cherry Blossom Tree Map")
    fig = px.treemap(df, path=['continent', 'country'], values='pop',
                     color='lifeExp', hover_data=['iso_alpha'],
                     color_continuous_scale='Oranges')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Particle Flow Field")
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    U = -Y; V = X
    fig = go.Figure(go.Streamline(x=x, y=y, u=U, v=V, density=30,
                                   arrow_scale=0.2, line=dict(color='cyan')))
    fig.update_layout(height=400, paper_bgcolor="black", plot_bgcolor="black")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Orbital Donut Galaxy")
    fig = px.pie(values=[30,20,15,35], names=["Q1","Q2","Q3","Q4"],
                 hole=0.7, color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("All charts built with Plotly • Deployed instantly on Streamlit • 2025 aesthetic")
