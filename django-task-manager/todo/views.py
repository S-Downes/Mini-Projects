from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

# Return a template from the templates directory for the app
def get_todo_list(request):
    """
    Import our Item data directly from our app models
    """
    results = Item.objects.all()
    return render(request, "todo_list.html", { "items": results })
    
# Our add item template
def add_item(request):
    """
    Add an Item object using the posted form elements
    """
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        """
        Using Django forms
        """
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()
    
    return render(request, "add_item.html", { "form": form })
    
# Edit item template with prepopulated values
def edit_item(request, id):
    item = get_object_or_404(Item, pk = id)
    form = ItemForm(instance = item)
    
    if request.method == "POST":
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance = item)
    
    return render(request, "add_item.html", { "form": form })
    
# Toggle the done value for each item in the list
def toggle_status(request, id):
    item = get_object_or_404(Item, pk = id)
    if request.method == "POST":
        # Inverts the current value for each item
        item.done = not item.done
        item.save()
    
    return redirect(get_todo_list)
    