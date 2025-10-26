# 1. IMPORT THE LIBRARIES
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout='wide',page_title='Startup Analysis')
# 2. Read the csv file into data frame
df = pd.read_csv(r'C:\Users\Adnan khalid\PycharmProjects\Indian_Startups\startup_cleaned.csv')
# 3. Check The data frame on streamlit
# st.dataframe(df)
# converting type of date column from object to datetime64
df['date'] = pd.to_datetime(df['date'])
# extracting year from date and adding new column name year in original df.
df['year'] = df['date'].dt.year
# extracting month from date and adding new column name month in original df.
df['month'] = df['date'].dt.month

# 4. general skeleton of UI.
st.sidebar.title('Startup Funding Analysis')

# 5. fetching list of investor names
lst_investors = sorted(set(df['investors'].str.split(',').sum()))

# 6. fetching list of startups names
lst_startups = sorted(df['startup'].unique().tolist())

option = st.sidebar.selectbox('Select Any One',
                     ['Investor','Startup','Overall Analysis'],index = None, placeholder='Choose One')

# -----------------------------------------------------------------------------------------------------------------
# now once user select any investor name, it must show the following details for that selected investor:
# Name
# Recent Investments: first 5 investments
# Biggest investments
# Generally invests in ...
# sector -pie
# city -> pie
# YoY investment graph
# Similar Investors
# -----------------------------------------------------------------------------------------------------------------
def load_investor_details(investor_name):
    st.header(investor_name)
    # Load 5 recent investments for selected investor_name
    recent_investments = df[df['investors'].str.contains(investor_name)].head()[['date','startup','vertical',
                                                                                'city','investors']]
    st.subheader('Most Recent Investments ')
    st.dataframe(recent_investments)

    col1,col2 = st.columns(2)
    # Load Top 5 investments of a selected investor_name
    biggest_investments = df[df['investors'].str.contains(investor_name)].groupby('startup')['amount'].sum().sort_values(
        ascending=False).head()
    # st.dataframe(biggest_investments)
    # Rather than showing biggest investments in df, i can show as in bar plot, where x axis is startups names,
    # and y axis is amount in crores
    with col1:
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(biggest_investments.index,biggest_investments.values)
        st.pyplot(fig)

    # load Generally In which sector investor invests more - draw a pie chart which only shows
    # top 5 sectors where investor usually invests
    sector_invests = df[df['investors'].str.contains(investor_name)].groupby('vertical')['amount'].sum().sort_values(ascending=False).head(5)
    # we get series where indexes are sector name and values are amounts, just use this series to draw a pie chart.

    # similarly for top 5 cities pie char which shows investments
    city_invests = df[df['investors'].str.contains(investor_name)].groupby('city')['amount'].sum().sort_values(
        ascending=False).head(5)
    # we get series where indexes are city names and values are amounts, just use this series to draw a pie chart.

    with col2:
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(sector_invests,labels = sector_invests.index,autopct = "%0.01f%%")
        st.pyplot(fig1)

    st.divider()
    col03, col04 = st.columns(2)
    with col03:
        st.subheader('Cities Invested In')
        fig2, ax2 = plt.subplots()
        ax2.pie(sector_invests,labels = city_invests.index,autopct = "%0.01f%%")
        st.pyplot(fig2)

    with col04:
        # load year on year investments made by investor by showing in line chart.
        # 1. change type of date column from object to date time and update the date column.
        df['date'] = pd.to_datetime(df['date'])
        # 2. make a new column called year by extracting year from every date and add year column in df
        df['year'] = df['date'].dt.year
        # 3. for a particular investor make a group on basis of year and get total amount invested in each year
        # by given investor.
        yoy_series = df[df['investors'].str.contains(investor_name)].groupby('year')['amount'].sum()

        st.subheader('Year On Year Investments')
        fig3, ax3 = plt.subplots()
        ax3.plot(yoy_series)
        st.pyplot(fig3)

def load_overall_analysis():
    st.title('Overall Analysis')
    st.divider()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        # total amount invested in till now
        total = round(df['amount'].sum())
        st.metric('Total Investment in Indian Startup', str(total) + ' Cr')
    with col2:
        # max amount invested/infused in a startup
        max_amount = round(df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0])
        st.metric('Max Investment in Indian Startup', str(max_amount) + ' Cr')
    with col3:
        # average investments by investors in each startup
        avg_amount = round(df.groupby('startup')['amount'].sum().mean())
        st.metric('Average investment by investors', str(avg_amount) + ' Cr')
    with col4:
        # total funded startups
        num_startups = df['startup'].nunique()
        st.metric('Total Startups', num_startups)

    # mom
    col5,col6 = st.columns(2)
    with col5:
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

        st.subheader('MoM Total amount invested')
        fig4, ax4 = plt.subplots()
        ax4.plot(temp_df['x_axis'],temp_df['amount'])

        # Rotate labels vertically
        plt.xticks(rotation=90)

        # Show every 3rd label to avoid clutter (adjust as needed)
        ax4.set_xticks(ax4.get_xticks()[::2])

        plt.tight_layout()
        st.pyplot(fig4)
    with col6:
        temp_df = df.groupby(['year','month'])['startup'].count().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

        st.subheader('MoM Total Startups Funded')
        fig5, ax5 = plt.subplots()
        ax5.plot(temp_df['x_axis'], temp_df['startup'])

        # Rotate labels vertically
        plt.xticks(rotation=90)

        # Show every 3rd label to avoid clutter (adjust as needed)
        ax5.set_xticks(ax4.get_xticks()[::2])

        plt.tight_layout()
        st.pyplot(fig5)





if option is not None:

    if option == 'Investor':
        st.title('Investor Analysis')
        st.divider() # st.markdown("---")
        # st.sidebar.selectbox('Select One Investor',['investor1','investor2','investor3'])
        # The above is just example, rather than showing investor1,investor2 we have to show actual investor names
        # of the data set, which is fetched --> see #5. point
        selected_investor = st.sidebar.selectbox('Select One Investor',lst_investors)

        # 7. once user select any investor name we have to show that selected investor details, so for that add button
        ibtn = st.sidebar.button('Find Investor Details')

        if ibtn:
            load_investor_details(selected_investor)



    elif option == 'Startup':
        st.title('Startup Analysis')
        # st.sidebar.selectbox('Select One Startup',['Startup1','Startup2','Startup3'])
        st.sidebar.selectbox('Select One Startup',lst_startups)

        # 8. once user select any startup name we have to show that selected startup details, so for that add button
        sbtn = st.sidebar.button('Find Startup Details')

    elif option == 'Overall Analysis':
        oabtn = st.sidebar.button('Show Overall Analysis')
        if oabtn:
            load_overall_analysis()




