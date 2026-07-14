from . import models

def create_note(title, content):
    return models.Notes.objects.create(title=title, content=content)

def get_all_notes():
    return models.Notes.objects.all()