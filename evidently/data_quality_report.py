import pandas as pd
import numpy as np

from evidently import ColumnMapping

from evidently.report import Report
from evidently.metric_preset import DataQualityPreset

current_data = pd.read_csv("trip_fare3.csv",parse_dates=['pickup_datetime'])
column_mapping = ColumnMapping()
column_mapping.datetime = 'pickup_datetime'
column_mapping.numerical_features = ['passenger_count', 'fare_amount']
column_mapping.categorical_features = ['pickup_zipcode', 'dropoff_zipcode']
report = Report(metrics=[DataQualityPreset()])
report.run(current_data=current_data,reference_data=None,column_mapping=column_mapping)
report.save_html("report.html")