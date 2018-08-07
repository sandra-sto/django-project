from django.urls import path

from . import views

urlpatterns = [
    path('devices_types', views.get_devices_types, name='devices types'),
    path('devices', views.get_devices, name='devices'),
    path('predictions', views.get_predictions_for_device, name='predictions'),
    path('model', views.get_prediction_models_for_devices, name='model'),
    path('data', views.get_data_for_device_and_parameter, name='data')
]