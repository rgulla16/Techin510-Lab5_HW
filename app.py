import streamlit as st
import pandas as pd
import altair as alt

# Load data
events_df = pd.read_csv("events.csv")

# Convert date column to datetime format, ignoring invalid dates
events_df["Date"] = pd.to_datetime(events_df["Date"], format="%m/%d/%Y", errors="coerce")

# Remove rows with invalid dates (NaT values)
events_df = events_df.dropna(subset=["Date"])


# Create a bar chart for event categories
category_counts = events_df.groupby("Type")["Type"].count().reset_index(name="Count")
category_chart = alt.Chart(category_counts).mark_bar().encode(
    x="Type:N",
    y="Count:Q",
    tooltip=["Type", "Count"]
).properties(
    title="Most Common Event Categories by Type in Seattle"
)

# Create a line chart for event count by month
events_df["Month"] = events_df["Date"].dt.month
month_counts = events_df.groupby("Month")["Name"].count().reset_index(name="Count")
month_chart = alt.Chart(month_counts).mark_bar().encode(
    x=alt.X("Month:O", title="Month of Year"),
    y=alt.Y("Count:Q", title="Number of Events"),
    tooltip=["Month", "Count"]
).properties(
    title="Event Count by Month"
)

# Create a bar chart for event count by day of the week
events_df["DayOfWeek"] = events_df["Date"].dt.dayofweek
day_counts = events_df.groupby("DayOfWeek")["Name"].count().reset_index(name="Count")
day_chart = alt.Chart(day_counts).mark_bar().encode(
    x=alt.X("DayOfWeek:O", title="Day of the Week"),
    y=alt.Y("Count:Q", title="Number of Events"),
    tooltip=["DayOfWeek", "Count"]
).properties(
    title="Event Count by Day of the Week"
)

# Create a bar chart for event locations
location_counts = events_df.groupby("Location")["Name"].count().reset_index(name="Count")
location_chart = alt.Chart(location_counts).mark_bar().encode(
    x="Location:N",
    y="Count:Q",
    tooltip=["Location", "Count"]
).properties(
    title="Event Locations"
)

# Display charts
st.altair_chart(category_chart, use_container_width=True)
st.altair_chart(month_chart, use_container_width=True)
st.altair_chart(day_chart, use_container_width=True)
st.altair_chart(location_chart, use_container_width=True)


selected_category = st.selectbox("Select Event Category", events_df["Type"].unique())
filtered_events = events_df[events_df["Type"] == selected_category]
