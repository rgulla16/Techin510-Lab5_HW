import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from db import get_db_conn

# Function to fetch data from the 'events' table
def fetch_data_from_db():
    conn = get_db_conn()
    query = "SELECT * FROM events"
    events_df = pd.read_sql(query, conn)
    conn.close()
    return events_df

# Load data from the PostgreSQL database
events_df = fetch_data_from_db()

# Convert date column to datetime format, ignoring invalid dates
events_df["date"] = pd.to_datetime(events_df["date"], format="%m/%d/%Y", errors="coerce")

# Remove rows with invalid dates (NaT values)
events_df = events_df.dropna(subset=["date"])

# Default values for filters
default_category = "All Categories"
default_date_range = [events_df["date"].min(), events_df["date"].max()]
default_location = "All Locations"

# Sidebar controls
st.sidebar.title("Filter Data")

# Dropdown for filtering by event category
selected_category = st.sidebar.selectbox("Select Event Category", ["All Categories"] + list(events_df["event_type"].unique()), index=0, key="category")

# Dropdown for filtering by event location
selected_location = st.sidebar.selectbox("Select Event Location", ["All Locations"] + list(events_df["location"].unique()), index=0, key="location")

# Filter events based on the selected category and location
filtered_events = events_df.copy()
if selected_category != "All Categories":
    filtered_events = filtered_events[filtered_events["event_type"] == selected_category]
if selected_location != "All Locations":
    filtered_events = filtered_events[filtered_events["location"] == selected_location]

# Date input for filtering by start date
start_date = pd.Timestamp(st.sidebar.date_input("Select Start Date", default_date_range[0], key="start_date"))

# Date input for filtering by end date
end_date = pd.Timestamp(st.sidebar.date_input("Select End Date", default_date_range[1], key="end_date"))

# Filter events based on the selected date range
filtered_events = filtered_events[(filtered_events["date"] >= start_date) & (filtered_events["date"] <= end_date)]

# Create a bar chart for event categories
category_counts = filtered_events.groupby("event_type")["event_type"].count().reset_index(name="Count")
category_chart = alt.Chart(category_counts).mark_bar().encode(
    x="event_type:N",
    y="Count:Q",
    tooltip=["event_type", "Count"]
).properties(
    title="Most Common Event Categories by Type"
)

# Create a line chart for event count by month
filtered_events["Month"] = filtered_events["date"].dt.month
month_counts = filtered_events.groupby("Month")["name"].count().reset_index(name="Count")
month_chart = alt.Chart(month_counts).mark_bar().encode(
    x=alt.X("Month:O", title="Month of Year"),
    y=alt.Y("Count:Q", title="Number of Events"),
    tooltip=["Month", "Count"]
).properties(
    title="Event Count by Month"
)

# Create a bar chart for event count by day of the week
filtered_events["DayOfWeek"] = filtered_events["date"].dt.dayofweek
day_counts = filtered_events.groupby("DayOfWeek")["name"].count().reset_index(name="Count")
day_chart = alt.Chart(day_counts).mark_bar().encode(
    x=alt.X("DayOfWeek:O", title="Day of the Week"),
    y=alt.Y("Count:Q", title="Number of Events"),
    tooltip=["DayOfWeek", "Count"]
).properties(
    title="Event Count by Day of the Week"
)

# Create a bar chart for event locations
location_counts = filtered_events.groupby("location")["name"].count().reset_index(name="Count")
location_chart = alt.Chart(location_counts).mark_bar().encode(
    x="location:N",
    y="Count:Q",
    tooltip=["location", "Count"]
).properties(
    title="Event Locations"
)

# Display charts
st.altair_chart(category_chart, use_container_width=True)
st.altair_chart(month_chart, use_container_width=True)
st.altair_chart(day_chart, use_container_width=True)
st.altair_chart(location_chart, use_container_width=True)
