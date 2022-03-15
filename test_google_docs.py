# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')


print('5')

# sql = f"""INSERT INTO "{sheet_url}" VALUES ("Vasia", "dog")"""
# conn.cursor().execute(f"""INSERT INTO "{sheet_url}" (name_, pet) VALUES ("Vasia", "dog")""")
# conn.commit()


# Print results.
for row in rows:
    st.write(f"{row.name_} has a :{row.pet}:")

# import pygsheets
# import pandas as pd
# #authorization
# gc = pygsheets.authorize(service_file='./.streamlit/cred4.json')
#
# # Create empty dataframe
# df = pd.DataFrame()
#
# # Create a column
# a = ['Kira', 'dog']
#
# #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
# sh = gc.open('new')
#
# #select the first sheet
# wks = sh[1]
# #rows = wks.get_values(majdim='ROWS')
# #print((wks.get_all_values()))
# # for row in rows:
# #     print(row)
#
# #update the first sheet with df, starting at cell B2.
# #wks.set_dataframe(df,(1,1))
#
# count_row = wks.rows
#
# #wks.delete_rows(5, number=995)
#
# print('4')
#
# wks.append_table(a, start='A'+str(count_row-1), end=None, dimension='ROWS', overwrite=False)

