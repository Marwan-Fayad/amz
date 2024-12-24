import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
style = """
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    </style>
"""

st.markdown(style, unsafe_allow_html=True)

# Load the dataset
data = pd.read_csv(r"C:\Users\lenovo\Desktop\Diploma\Project_1\amazon.csv")
data['rating'] = data['rating'].str.replace('|', '3.9').astype('float64')
data['discounted_price'] = data['discounted_price'].str.replace("₹",'')
data['discounted_price'] = data['discounted_price'].str.replace(",",'')
data['discounted_price'] = data['discounted_price'].astype('float64')

data['actual_price'] = data['actual_price'].str.replace("₹",'')
data['actual_price'] = data['actual_price'].str.replace(",",'')
data['actual_price'] = data['actual_price'].astype('float64')
data['discount_percentage'] = data['discount_percentage'].str.replace('%','').astype('float64')

data['discount_percentage'] = data['discount_percentage'] / 100
data['rating_count'] = data['rating_count'].str.replace(',', '').astype('float64')
data=data.dropna()
amazon = data[['product_id', 'product_name', 'category', 'discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']].copy()
amazon.head()
catsplit = amazon['category'].str.split('|', expand=True)
catsplit = catsplit.rename(columns={0:'category_1', 1:'category_2'})
amazon['category_1'] = catsplit['category_1']
amazon['category_2'] = catsplit['category_2']

amazon.drop(columns='category', inplace=True)
amazon['category_1'] = amazon['category_1'].str.replace('&', ' & ')
amazon['category_1'] = amazon['category_1'].str.replace('OfficeProducts', 'Office Products')
amazon['category_1'] = amazon['category_1'].str.replace('MusicalInstruments', 'Musical Instruments')
amazon['category_1'] = amazon['category_1'].str.replace('HomeImprovement', 'Home Improvement')
amazon['category_2'] = amazon['category_2'].str.replace('&', ' & ')
amazon['category_2'] = amazon['category_2'].str.replace(',', ', ')
amazon['category_2'] = amazon['category_2'].str.replace('HomeAppliances', 'Home Appliances')
amazon['category_2'] = amazon['category_2'].str.replace('AirQuality', 'Air Quality')
amazon['category_2'] = amazon['category_2'].str.replace('WearableTechnology', 'Wearable Technology')
amazon['category_2'] = amazon['category_2'].str.replace('NetworkingDevices', 'Networking Devices')
amazon['category_2'] = amazon['category_2'].str.replace('OfficePaperProducts', 'Office Paper Products')
amazon['category_2'] = amazon['category_2'].str.replace('ExternalDevices', 'External Devices')
amazon['category_2'] = amazon['category_2'].str.replace('DataStorage', 'Data Storage')
amazon['category_2'] = amazon['category_2'].str.replace('HomeStorage', 'Home Storage')
amazon['category_2'] = amazon['category_2'].str.replace('HomeAudio', 'Home Audio')
amazon['category_2'] = amazon['category_2'].str.replace('GeneralPurposeBatteries', 'General Purpose Batteries')
amazon['category_2'] = amazon['category_2'].str.replace('BatteryChargers', 'Battery Chargers')
amazon['category_2'] = amazon['category_2'].str.replace('CraftMaterials', 'Craft Materials')
amazon['category_2'] = amazon['category_2'].str.replace('OfficeElectronics', 'Office Electronics')
amazon['category_2'] = amazon['category_2'].str.replace('PowerAccessories', 'Power Accessories')
amazon['category_2'] = amazon['category_2'].str.replace('CarAccessories', 'Car Accessories')
amazon['category_2'] = amazon['category_2'].str.replace('HomeMedicalSupplies', 'Home Medical Supplies')
amazon['category_2'] = amazon['category_2'].str.replace('HomeTheater', 'Home Theater')

st.title("Amazon Sales Analysis")
st.sidebar.header("Navigation")
st.sidebar.markdown("Created by [Marwan Fayad](https://www.linkedin.com/in/marwan-fayad-427314249/)")


sidebar_sel=st.sidebar.radio("Select An Option",['Introduction', 'EDA', 'Charts'])

if sidebar_sel == 'Introduction':
    st.header("Intrduction About The Dataset")
    st.write("This is a web application that allows users to explore the Amazon sales dataset.")
    st.write("The Amazon sales dataset provides data on products sold on Amazon, detailing product features, pricing, discounts, customer ratings, reviews, and user activity. This dataset enables an in-depth analysis of sales trends, product popularity, and customer engagement.")
    st.write(data.head())
    st.markdown("### Dataset Summary")
    st.write(data.describe())

    # Filtered Dataset Option inside the Introduction section
    st.markdown("### Filtered Dataset Option")
    show_filtered_data = st.checkbox("Show Filtered Dataset")

    if show_filtered_data:
        st.title("Filtered Dataset")
        st.write(amazon.head())
elif sidebar_sel=='EDA':
    st.header('Exploratory Data Analysis')
    st.subheader('Distribution of discounted prices')
    plt.figure(figsize=(12, 6))
    sns.histplot(amazon['discounted_price'], bins=50, kde=True, color='blue')
    plt.title('Distribution of Discounted Prices')
    plt.xlabel('Discounted Price (₹)')
    plt.ylabel('Frequency')
    st.pyplot(plt)
    st.subheader('Distribution of actual prices')
    plt.figure(figsize=(12, 6))
    sns.histplot(amazon['actual_price'], bins=50, kde=True, color='green')
    plt.title('Distribution of Actual Prices')
    plt.xlabel('Actual Price (₹)')
    plt.ylabel('Frequency')
    st.pyplot(plt) 
elif sidebar_sel=='Charts':
    st.header('Main Objectives Charts')
    # Most main items by category
    most_main_items = amazon['category_1'].value_counts().head(5).rename_axis('category_1').reset_index(name='counts')
    most_sub_items = amazon['category_2'].value_counts().head(10).rename_axis('category_2').reset_index(name='counts')

    # Create subplots with larger figure size
    fig, ax = plt.subplots(2, 1, figsize=(60, 60))  # Increased size to 12x12 inches
    fig.suptitle('Most Amount of Products by Main Category and Sub-Category', fontweight='heavy', size='x-large')

    # Create bar plots
    sns.barplot(ax=ax[0], data=most_main_items, x='counts', y='category_1')
    sns.barplot(ax=ax[1], data=most_sub_items, x='counts', y='category_2')

    # Set labels and titles with larger font sizes
    ax[0].set_xlabel('Count', fontweight='bold', fontsize=80)
    ax[0].set_ylabel('Product Main Category', fontweight='bold', fontsize=80)
    ax[0].set_title('Most Products by Main Category', fontweight='bold', fontsize=80)

    ax[1].set_xlabel('Count', fontweight='bold', fontsize=80)
    ax[1].set_ylabel('Product Sub-Category', fontweight='bold', fontsize=80)
    ax[1].set_title('Most Products by Sub-Category', fontweight='bold', fontsize=80)

    # Increase tick label sizes
    ax[0].tick_params(axis='both', which='major', labelsize=80)
    ax[1].tick_params(axis='both', which='major', labelsize=80)

    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.4)  # Increase space between the plots

    # Display the plots in Streamlit
    st.pyplot(fig)

    # Create a figure with a specified size
    plt.figure(figsize=(20, 16))  # Adjust the size as needed

    # Create the bar plot

    st.header('Top 5 Cheapest Products After Discount')

    # Create a DataFrame for the top 5 cheapest products
    top_5_cheapest = amazon.sort_values('discounted_price').head(5)

    # Create a bar chart using st.bar_chart
    st.bar_chart(top_5_cheapest.set_index('product_name')['discounted_price'])
    top_5_cheapest = amazon.sort_values('discounted_price').head(5)
    
    st.header('Scatter Plot of Discounted Price vs. Rating')

    # Prepare data for scatter chart
    scatter_data = amazon[['rating', 'discounted_price']]

    # Create a scatter chart using Streamlit
    st.scatter_chart(scatter_data.set_index('rating'))
    
    st.header('Relationship between Actual Price and Discounted Price (Colored by Rating)')

    # Create a scatter plot using Matplotlib
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(amazon['actual_price'], amazon['discounted_price'], c=amazon['rating'], cmap='viridis', s=100, alpha=0.8, edgecolors='w')

    # Add color bar
    plt.colorbar(scatter, label='Rating')

    # Add labels and title
    plt.xlabel('Actual Price')
    plt.ylabel('Discounted Price')
    plt.title('Relationship between Actual Price and Discounted Price (Colored by Rating)')

    # Show plot
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)