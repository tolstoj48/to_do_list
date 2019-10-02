import pytest
import datetime
from to_do_list import Note, Notebook
import inspect

def test_note():
    note = Note("Prvni", "Textace", datetime.date.today(), datetime.date.today())
    assert note.name == "Prvni"
    assert note.text == "Textace"
    assert note.date_of_inception == datetime.date.today()
    assert note.scheduled_date == datetime.date.today()

def test_notebook():
    notebook_production = Notebook()
    assert type(notebook_production.all_notes) == dict

def test_add_a_note(notebook_mock):
    note = Note("Prvni", "Textace", datetime.date.today(), datetime.date.today())
    notebook_mock[note.name] = [note.text, note.date_of_inception, note.scheduled_date]
    assert notebook_mock["Prvni"] == ["Textace", datetime.date.today(), datetime.date.today()]

def test_delete_a_note(notebook_mock):
    del notebook_mock["First"]
    assert notebook_mock == {}

def test_validate_date_format():
    notebook_production = Notebook()
    assert notebook_production.validate_date_format('2018-12-12') == True
