from django.shortcuts import render, redirect
from django.conf import settings
from myapp.Forms import MarkForm
import os
import xml.etree.ElementTree as ET

# Определяем путь к папке и файлу

def save_mark_data(data):
    marks_dir = os.path.join(settings.BASE_DIR, 'Marks') # Определяем путь к папке и файлу
    if not os.path.exists(marks_dir):
        os.makedirs(marks_dir)
        file_path = os.path.join(marks_dir, 'marks.xml')
    if os.path.exists(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
    else:
        root = ET.Element('Marks')
        tree = ET.ElementTree(root)
    mark = ET.Element('Mark')
    ET.SubElement(mark, 'Country').text = data['country']
    ET.SubElement(mark, 'View').text = data['view']
    ET.SubElement(mark, 'Year').text = str(data['year'])
    ET.SubElement(mark, 'Image').text = data['image']
    root.append(mark)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def mark_form(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            save_mark_data(form.cleaned_data)
            return redirect('mark_list')
    else:
        form = MarkForm()
    return render(request, 'myapp/Form.html', {'form': form})

def mark_list(request):
    books_dir = os.path.join(settings.BASE_DIR, 'Marks')
    file_path = os.path.join(marks_dir, 'marks.xml')
    marks = []
    if os.path.exists(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for mark in root.findall('Mark'):
            marks.append({
                'country': mark.find('Country').text,
                'view': mark.find('View').text,
                'year': mark.find('Year').text,
                'image': mark.find('Image').text
                })
    return render(request, 'myapp/List.html', {'marks': marks})
