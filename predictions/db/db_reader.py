

from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from predictions.models import Predictions
from django.http import HttpResponse

def get_all_predictions():
    # cluster = Cluster(['127.0.0.1'])
    # session = cluster.connect()
    # session.set_keyspace('presto')

    predictions = Predictions.all()
    # cluster.shutdown()
    return list(predictions)
