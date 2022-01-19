from typing import List
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

pending_tasks: List[str] = []
completed_tasks: List[str] = []


def index(request):
    return render(request, "index.html")


def all_tasks_view(request):
    return render(request, "all.html", {"pending_tasks": pending_tasks, "completed_tasks": completed_tasks})


def pending_tasks_view(request):
    return render(request, "pending.html", {"tasks": pending_tasks})


def completed_tasks_view(request):
    return render(request, "completed.html", {"tasks": completed_tasks})


def add_task_view(request):
    task = request.GET.get("task")
    if task:
        pending_tasks.append(task)
        return HttpResponseRedirect("/tasks")
    else:
        return render(request, "add.html")


def complete_task(request, task_id):
    completed_tasks.append(pending_tasks.pop(task_id - 1))
    return HttpResponseRedirect("/tasks")


def delete_task(request, task_id):
    pending_tasks.pop(task_id - 1)
    return HttpResponseRedirect("/tasks")
