from django.shortcuts import render
from django.http import JsonResponse

feedback_list = []

def feedback_page(request):
    return render(request, "feedback.html")

def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        feedback = request.POST.get("feedback")

        data = {"name": name, "feedback": feedback}
        feedback_list.append(data)

        return JsonResponse(data)