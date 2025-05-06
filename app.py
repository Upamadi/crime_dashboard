import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Crime and No-Crime Dashboard",
    page_icon="🔍",
    layout="wide"
)

# Set the title of the dashboard
st.title("Crime and No-Crime Dashboard (2011/12)")
st.markdown("*An interactive visualization of crime data and no-crime records*")

# Load the cleaned dataset
# Using a relative path instead of absolute path for better portability
try:
    # Try loading from the current directory first
    df = pd.read_csv('no-crime-201112-cleaned.csv')
except FileNotFoundError:
    # Try looking in a data subdirectory
    try:
        df = pd.read_csv('./data/no-crime-201112-cleaned.csv')
    except FileNotFoundError:
        st.error("Error: Dataset file not found. Please place the 'no-crime-201112-cleaned.csv' file in the same directory as this script or in a 'data' subdirectory.")
        st.stop()

# Sidebar Filters
with st.sidebar:
    st.header("Filter the Data")
    st.markdown("---")
    
    # Add a logo or image if available
    # st.image("logo.png", width=150)
    
    forces = st.multiselect(
        "Select Police Forces",
        options=sorted(df['Force_Name'].unique()),
        default=df['Force_Name'].unique()
    )
    
    offences = st.multiselect(
        "Select Offence Groups",
        options=sorted(df['Offence_Group'].unique()),
        default=df['Offence_Group'].unique()
    )
    
    st.markdown("---")
    st.info("This dashboard displays crime data and no-crime records for police forces across England and Wales for the year 2011/12.")

# Apply Filters
filtered_df = df[
    (df['Force_Name'].isin(forces)) & 
    (df['Offence_Group'].isin(offences))
]

# Main content
# Show the filtered data
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df, height=200)

# Show summary metrics
st.subheader("Offences vs No-Crimes Summary")
total_offences = filtered_df['Force_Offences'].sum()
total_no_crimes = filtered_df['Force_No_Crimes'].sum()

# Use columns for metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Offences", f"{total_offences:,}")
with col2:
    st.metric("Total No-Crimes", f"{total_no_crimes:,}")

# Calculate and display No-Crime %
no_crime_percentage = (total_no_crimes / total_offences) * 100 if total_offences else 0
with col3:
    st.metric("No-Crime Percentage", f"{no_crime_percentage:.2f}%")

# Create two columns for charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    # Bar Chart: Total Offences by Police Force
    st.subheader("Total Offences by Police Force")
    offence_by_force = filtered_df.groupby('Force_Name')['Force_Offences'].sum().sort_values(ascending=False)

    # Limit to top 10 forces for readability if there are many
    if len(offence_by_force) > 10:
        offence_by_force = offence_by_force.head(10)
        st.caption("Showing top 10 forces by number of offences")

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    offence_by_force.plot(kind='bar', ax=ax1, color='steelblue')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Number of Offences')
    plt.tight_layout()
    st.pyplot(fig1)

with chart_col2:
    # Pie Chart: Distribution of Offence Types
    st.subheader("Distribution of Offence Types")
    offence_group_counts = filtered_df.groupby('Offence_Group')['Force_Offences'].sum()

    fig2, ax2 = plt.subplots(figsize=(8, 8))
    colors = plt.cm.tab10.colors
    wedges, texts, autotexts = ax2.pie(
        offence_group_counts, 
        labels=offence_group_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors
    )
    plt.setp(autotexts, size=8, weight="bold")
    plt.setp(texts, size=9)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    st.pyplot(fig2)

# Add another section for more insights
st.subheader("No-Crime Ratio by Police Force")
no_crime_ratio = filtered_df.groupby('Force_Name').apply(
    lambda x: (x['Force_No_Crimes'].sum() / x['Force_Offences'].sum() * 100) if x['Force_Offences'].sum() > 0 else 0
).sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(12, 6))
no_crime_ratio.plot(kind='bar', ax=ax3, color='indianred')
plt.xticks(rotation=45, ha='right')
plt.ylabel('No-Crime Ratio (%)')
plt.tight_layout()
st.pyplot(fig3)

# Add download capability
st.subheader("Download Filtered Data")
st.download_button(
    label="Download as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_crime_data.csv',
    mime='text/csv',
)

# Footer
st.write("---")
st.markdown("*Dashboard created for 5DATA004W Coursework - University of Westminster*")
st.caption("Data source: Crime and No-Crime Records 2011/12")