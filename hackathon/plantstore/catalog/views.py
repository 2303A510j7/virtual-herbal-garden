from django.shortcuts import render, get_object_or_404
from .models import Plant
from django.shortcuts import render, get_object_or_404
from .models import Plant
import json


def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'catalog/plant_list.html', {'plants': plants})

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
  
    image_folder = f'{plant.image_folder}/'
    image_paths = [f'{image_folder}{i:03}.jpg' for i in range(1, 4)]  # Adjust the range if needed
    print(image_paths)
    image_paths_json = json.dumps(image_paths)  # Convert Python list to JSON format for JS
    return render(request, 'catalog/plant_detail.html', {'plant': plant, 'image_paths_json': image_paths_json})

