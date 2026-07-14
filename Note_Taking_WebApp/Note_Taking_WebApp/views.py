from . import forms, services
from django.shortcuts import render

def index(request):
    notes = services.get_all_notes()
    form = forms.NoteForm()
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            services.create_note(title, content)
            notes = services.get_all_notes()  # Refresh the notes list after adding a new note

    return render(request, 'index.html', {'notes': notes, 'form': form})
