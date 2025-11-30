import pytest
import tkinter as tk

class DummyRoot:
    def __init__(self, *args, **kwargs):
        self._title = ""
    def title(self, t=None):
        if t is not None:
            self._title = t
        return self._title
    def geometry(self, *a, **k):
        pass
    def configure(self, *a, **k):
        pass
    def grid_rowconfigure(self, *a, **k):
        pass
    def grid_columnconfigure(self, *a, **k):
        pass
    def mainloop(self):
        pass
    def bind(self, *a, **k):
        pass
    def after(self, *a, **k):
        pass
    def destroy(self):
        pass

class DummyEntry:
    def __init__(self, master=None, *args, **kwargs):
        self._text = ""
    def grid(self, *a, **k):
        pass
    def delete(self, start, end=None):
        self._text = ""
    def insert(self, index, text):
        self._text = str(text)
    # helper opcional para tests si quieren leer el contenido:
    def get(self):
        return self._text

class DummyButton:
    def __init__(self, master=None, *args, **kwargs):
        pass
    def grid(self, *a, **k):
        pass

class DummyLabel:
    def __init__(self, master=None, *args, **kwargs):
        self._text = kwargs.get('text', '')
    def grid(self, *a, **k):
        pass
    def config(self, **kwargs):
        if 'text' in kwargs:
            self._text = kwargs['text']
    def get(self):
        return self._text

@pytest.fixture(autouse=True)
def replace_tkinter():
    """
    Fixture autouse que sustituye componentes gráficos por dummies durante los tests.
    Esto evita la necesidad de tener Tcl/Tk instalado para ejecutar los tests unitarios.
    """
    # Guardamos referencias originales para restaurar al finalizar el test
    original_Tk = tk.Tk
    original_Entry = tk.Entry
    original_Button = tk.Button
    original_Label = tk.Label

    tk.Tk = DummyRoot
    tk.Entry = DummyEntry
    tk.Button = DummyButton
    tk.Label = DummyLabel

    try:
        yield
    finally:
        # restaurar
        tk.Tk = original_Tk
        tk.Entry = original_Entry
        tk.Button = original_Button
        tk.Label = original_Label