from django.shortcuts import render_to_response

def index_action(request):
    return render_to_response('default.html', {})