import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page
st.set_page_config(page_title="AI Support Dashboard", layout="wide")
st.title("🤖 AI-Powered Customer Support Triage")
st.markdown("This dashboard displays customer support tickets that have been automatically categorized and summarized by an AI (Llama 3.3).")

# Load the data safely
@st.cache_data
def load_data():
    # Make sure the file name matches exactly what you uploaded to GitHub!
    return pd.read_csv("enriched_tickets.csv")

try:
    df = load_data()
    
    # Top metrics
    st.sidebar.header("Overview")
    st.sidebar.metric("Total Tickets Processed", len(df))

    # Visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Issue Categories")
        fig_cat = px.pie(df, names='AI_Category', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_cat, use_container_width=True)

    with col2:
        st.subheader("Sentiment Distribution")
        fig_sent = px.bar(df, x='AI_Category', color='AI_Sentiment', 
                          color_discrete_map={'Positive':'#2ECC71', 'Neutral':'#95A5A6', 'Negative':'#E74C3C'})
        st.plotly_chart(fig_sent, use_container_width=True)

    # Data Table
    st.subheader("Recent Tickets (AI Enriched)")
    st.dataframe(df[['Ticket ID', 'AI_Category', 'AI_Sentiment', 'AI_Summary']], use_container_width=True)

except FileNotFoundError:
    st.error("Error: Could not find 'enriched_tickets.csv'. Please make sure it is uploaded to GitHub.")
