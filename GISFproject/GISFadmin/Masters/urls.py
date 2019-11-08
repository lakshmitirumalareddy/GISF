from django.urls import path

from .views import (ProductsMaster,ProductRisk,AgentMasterView,AgentCommision,VehicleMasterView,VehicleDepriciationMasterView,
                    XxgenNcbMasterView,ClaimStatusMasterView,ClaimsSurveyorMasterView,ClaimStatusListView)

app_name = 'Masters'
urlpatterns = [
    path('productmaster/', ProductsMaster, name='productmaster'),
    path('productriskmaster/', ProductRisk, name='productriskmaster'),
    path('agentmaster/', AgentMasterView, name='agentmaster'),
    path('agentcomission/',AgentCommision,name='agentcomission'),
    path('vehiclemaster/',VehicleMasterView,name='VehicleMasterView'),
    path('vehicledepriciation/',VehicleDepriciationMasterView,name='vehicledepriciation'),
    path('noclaimbonus/',XxgenNcbMasterView,name='noclaimbonus'),
    path('claimstatus/',ClaimStatusMasterView,name='claimstatus'),
    path('createsurveyor/',ClaimsSurveyorMasterView,name='createsurveyor'),
    path('ClaimList/',ClaimStatusListView.as_view(),name='ClaimList')

]
