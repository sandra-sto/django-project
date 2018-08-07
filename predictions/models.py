from django.db import models

# Create your models here.
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns


class Predictions(Model):
    device= columns.Text(primary_key=True)
    timestamp_for_prediction = columns.Text(primary_key=True, clustering_order="ASC", db_field="timestamp")
    timestamp_created= columns.Text()

    parameter = columns.Text()
    value = columns.Double()
    prediction_error = columns.Double()
    # accuracy_estimated = columns.Double()

class Devices(Model):
    id = columns.Integer(primary_key=True)
    device_id = columns.Text(primary_key=True, clustering_order="ASC")
    device_type = columns.Text(primary_key=True, clustering_order="ASC")

class PredictionModel(Model):
    device = columns.Text(primary_key=True)
    timestamp_created= columns.Text(primary_key=True, clustering_order="ASC")
    average_error = columns.Double()
    lag_order = columns.Integer()
    # steps = columns.List(columns.Text)
    # conf_parameters = columns.Map(columns.Text, columns.Text)
    __table_name__ = "model"


class Data(Model):
    device_id = columns.Text(primary_key=True)
    parameter_name = columns.Text(primary_key=True, clustering_order="ASC")
    parameter_value= columns.Double()
    bucket = columns.Text(primary_key=True)
    ts_offset = columns.Integer(primary_key=True, clustering_order="ASC")

