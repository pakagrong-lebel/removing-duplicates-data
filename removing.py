# Python script to remove duplicates from data
import pandas as pd
def remove_duplicates(data_frame):
    cleaned_data = data_frame.drop_duplicates()
    return cleaned_data