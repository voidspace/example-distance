from django import forms
from django.shortcuts import render

from location import get_store

store = get_store()


class DistanceForm(forms.Form):
    from_town = forms.ChoiceField(choices=[(town.name, town.name) for town in store])
    to_town = forms.ChoiceField(choices=[(town.name, town.name) for town in store])


def distance(request):
    result = False
    form = DistanceForm()
    from_town = to_town = distance = None

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DistanceForm(request.POST)
        if form.is_valid():
            result = True
            from_town = form.cleaned_data["from_town"]
            to_town = form.cleaned_data["to_town"]
            distance = store.distance(from_town, to_town)

    variables = {
        "form": form,
        "result": result,
        "from_town": from_town,
        "to_town": to_town,
        "distance": distance,
    }
    return render(request, "distance.html", variables)
