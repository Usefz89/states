from django.shortcuts import render
from django.http import HttpResponse

from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app.forms import *


# Create your views here.

def first_view(request, starts_with):
    states = State.objects.all()
    text_string = ""

    for state in states:
        cities = state.city_set.filter(name__startswith=starts_with)
        for city in cities:
            text_string += " State = %s, City = %s <br>" % (state, city.name)

    return HttpResponse(text_string)


@csrf_exempt
def get_post(request):
    if request.method == "GET":
        state_for_string = """
        <form action = "/get_post" method = "POST">

        State:
        <br>
        <input type = "text" name = "state">

        <br>

        City:
        <br>
        <input type = "text" name = "state">

        <br>

        <input type= "submit" value = "Submit">
        </form>

        """
        response = state_for_string
        return HttpResponse(response)


    elif request.method == "POST":

        get_state = request.POST.get('state', None)
        get_city = request.POST.get('city', None)

        states = State.objects.filter(name__startswith="%s" % get_state)
        state_for_string = ""

        for state in states:
            cities = state.city_set.filter(name__startswith="%s" % get_city)

            for city in cities:
                state_for_string += "<br> State: %s </b> -- City: %s" % (state, city.name)

        state_for_string += """
        <form action="/get_post" method="POST">

        State:
        <br>
        <input type="text" name="state">
        <br>

        City:
        <br>
        <input type="text" name="city">
        <br>

        <input type="submit" value="Submit">
        </form>

        """
        response = state_for_string
        return HttpResponse(response)




def template_view(request):
    context = {}
    state_city = {}

    states = State.objects.all()
    for state in states:
        cities = state.city_set.filter(name__startswith="A")
        state.name = {state.name : cities}

        state_city.update(state.name)

    context['states'] = state_city

    return render(request, 'base.html', context)


class StateListView(ListView):
    model = State
    template_name = "state_list.html"
    context_object_name = "state_list"

# class StateDetailView(DetailView):
#     model = State
#     template_name = "State_detail.html"
#     context_object_name = "state"


def state_detail(request,pk):
    context = {}
    city_list = []


    states = State.objects.filter(pk=pk)

    for state in states:
        context['state'] = state
        cities = state.city_set.all()
        for city in cities:
            city_list.append(city)


    context['cities'] = city_list

    return render(request, 'state_detail.html', context)















class CityDetailView(DetailView):
    model = City
    template_name = "city_detail.html"
    context_object_name = "city"



def city_search(request):


    context = {}

    if request.method == "POST":
        form = CitySearchForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = "%s" %form.cleaned_data['city']
            state = "%s" %form.cleaned_data['state']

            city_list = City.objects.filter(name__startswith='%s' % name, state__name__startswith="%s" % state)
            context['city_list'] = city_list
            context['valid'] = "is_valid"

            return render(request, "city_search.html", context)


        else:
            context['valid'] = form.errors
            return render(request, "city_search.html", context)

    else:
        form = CitySearchForm()
        context['form'] = form

        return render(request, "city_search.html", context)


def city_create(request):
    context = {}

    if request.method == "POST":
        form = CreateCityForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['valid'] = "is_valid"
            return render(request, "city_createa.html", context)

        else:

            context['valid'] = form.errors
            return render(request, "city_create.html", context)

    else:
        form = CreateCityForm()
        context['form'] = form
        return render(request, "city_create.html", context)















