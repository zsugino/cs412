from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
import plotly
import plotly.graph_objs as go
from collections import Counter


# Create your views here.
class VotersListView(ListView):
    '''View to display voters'''
    template_name = 'voter_analytics/voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        '''
        Provide context variables for use in template
        '''
        context = super().get_context_data(**kwargs)
        context['years'] = range(1900,2025)
        context['scores'] = range(0,6)
        return context

    def get_queryset(self):
        # start with entire queryset
        qs = super().get_queryset().order_by('voter_score')
        # filter results by these field(s):
        if 'party_affiliation' in self.request.GET:
            party_affiliation = self.request.GET.get("party_affiliation", "")
            if party_affiliation:
                qs = qs.filter(party_affiliation=party_affiliation)

        minimum = self.request.GET.get("minimum", "")
        if minimum.isdigit():
            qs = qs.filter(date_of_birth__year__gte=int(minimum))


        maximum = self.request.GET.get("maximum", "")
        if maximum.isdigit():
            qs = qs.filter(date_of_birth__year__lte=int(maximum))


        v_score = self.request.GET.get("v_score", "")
        if v_score.isdigit():
             qs = qs.filter(voter_score=int(v_score))

        if self.request.GET.get("v20state") == "on":
            qs = qs.filter(v20state=True)
        if self.request.GET.get("v21town") == "on":
            qs = qs.filter(v21town=True)
        if self.request.GET.get("v21primary") == "on":
            qs = qs.filter(v21primary=True)
        if self.request.GET.get("v22general") == "on":
            qs = qs.filter(v22general=True)
        if self.request.GET.get("v23town") == "on":
            qs = qs.filter(v23town=True)
        
        return qs


class VoterDetailView(DetailView):
    '''View to show detail page for one voter.'''
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'v'


class GraphListView(ListView):
    '''View to show graph page'''
    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'v'
    def get_context_data(self, **kwargs) :
        '''
        Provide context variables for use in template
        '''
        # start with superclass context
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()

        # create bar chart for birth distribution
        dict_year = {}
        for v in qs:
            year = v.date_of_birth.year
            if year in dict_year:
                dict_year[year] +=1
            else:
                dict_year[year] = 1

        all_year = sorted(dict_year.keys())
        birth_count = [dict_year[year] for year in all_year]
        
        fig = go.Bar(x=all_year, y=birth_count)
        title_text = f"Voter Distribution by Year of Birth"
        birth = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, auto_open=False, output_type="div",
                                         
                                         ) 
        context['birth'] = birth

        
        # create pie chart for party affiliation
        party_affiliation = [v.party_affiliation for v in qs]

        num_party = {}
        for v in qs:
            party = v.party_affiliation
            if party in num_party:
                num_party[party] +=1
            else:
                num_party[party] = 1

        x = list(num_party.keys())
        y= list(num_party.values())

        fig = go.Pie(labels=x, values=y) 
        title_text = f"Voter distribution by Party Affiliation"
        # obtain the graph as an HTML div"
        pie_party_affiliation = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, 
                                         auto_open=False, 
                                         output_type="div")
        # send div as template context variable
        context['pie_party_affiliation'] = pie_party_affiliation

        # Create chart representing count for election
        election_type = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        election_count = [qs.filter(v20state=True).count(), qs.filter(v21town=True).count(),qs.filter(v21primary=True).count(),qs.filter(v22general=True).count(),qs.filter(v23town=True).count()]
        
        fig = go.Bar(x=election_type, y=election_count)
        title_text = f"Vote Count by Election"
        graph_election = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, auto_open=False, output_type="div",
                                         
                                         ) 
        context['graph_election'] = graph_election

        return context

    
    





