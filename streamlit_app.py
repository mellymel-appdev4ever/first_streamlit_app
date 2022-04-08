import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build Your Own Fruit Smoothie')

import pandas 
@streamlit.cache
def get_data():
    dataframe = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    return dataframe.set_index("Fruit")

    dataframe = get_data()
    smoothiefruitschosen = streamlit.multiselect(
        "Select Fruits for Your Smoothie", list(dataframe.index), ["Apple", "Banana"]
    )
        dataset = dataframe.loc[smoothiefruitschosen]
        streamlit.write("### Fruits in Smoothie", dataset.sort_index())

        dataset = dataset.T.reset_index()
        dataset = pandas.melt(dataset, id_vars=["index"]).rename(
            columns={"index": "Calories", "value": "Fruits in Smoothie"}
        )

        )

