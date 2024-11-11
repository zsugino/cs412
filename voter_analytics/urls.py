from django.urls import path
from . import views 
urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', views.VotersListView.as_view(), name='home'),
    path(r'results', views.VotersListView.as_view(), name='voters_list'),
    path(r'voter/<int:pk>', views.VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphListView.as_view(), name="graph")

]