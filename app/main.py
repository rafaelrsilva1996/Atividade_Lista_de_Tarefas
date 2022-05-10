import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk, GdkPixbuf

from crud_tarefa import Tarefa

class MainWindow(Gtk.ApplicationWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.set_default_size(500, 500)

    self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.entry = Gtk.Entry(placeholder_text = "Descrição da tarefa.")
    self.btn = Gtk.Button(label="Criar tarefa")
    self.lst_box = Gtk.ListBox()

    self.add(self.box)
    self.box.pack_start(self.lst_box, False, True, 0)
    self.box.pack_start(self.entry, False, True, 0)
    self.box.pack_start(self.btn, False, True, 0)

    self.btn.connect('clicked', self.btn_press)

    self.css_provider = Gtk.CssProvider()
    self.css_provider.load_from_path('style.css')

    tarefas = Tarefa().listar()
    for tarefa in tarefas:
      label_text = f'{tarefa[2]}'

      cbtn_feito = Gtk.CheckButton()
      cbtn_feito.set_active(tarefa[1] == 'feito')

      box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
      label = Gtk.Label(label = label_text)
      btn_remove = Gtk.Button(label="X")
      
      box.pack_start(cbtn_feito, False, False, 0)
      box.pack_start(label, True, True, 0)
      box.pack_start(btn_remove, False, False, 0)

      cbtn_feito.connect('toggled', self.check_toggle, label, tarefa)

      self.lst_box.insert(box, 0)
      self.show_all()

      context = label.get_style_context()
      context.add_provider(self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
      if tarefa[1] == 'feito':
        context.add_class('label-done')
      else:
        context.add_class('label-todo')

      btn_remove.connect('clicked', self.btn_press_remove, tarefa)

  def btn_press(self, widget):
    cbtn_feito = Gtk.CheckButton()

    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    label = Gtk.Label(label = self.entry.props.text)
    btn_remove = Gtk.Button(label="X")
    
    box.pack_start(cbtn_feito, False, False, 0)
    box.pack_start(label, True, True, 0)
    box.pack_start(btn_remove, False, False, 0)    
    self.lst_box.insert(box, 0)

    self.show_all()

    context = label.get_style_context()
    context.add_provider(self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    context.add_class('label-todo')

    tarefa = Tarefa(self.entry.props.text, 'pendente')
    tarefa.inserir()
    
    cbtn_feito.connect('toggled', self.check_toggle, label, tarefa)
    btn_remove.connect('clicked', self.btn_press_remove, tarefa)
  
  def btn_press_remove(self, widget, tarefa):
    vbox = widget.get_parent()
    base = vbox.get_parent()
    children = base.get_children()
    listbox = children[0]
    for row in listbox.get_children():
      listbox.remove(row)

    if isinstance(tarefa, tuple):
      tarefa = Tarefa(tarefa[2], tarefa[1], tarefa[0])
    tarefa.deletar()

  def check_toggle(self, widget, label, tarefa=None):
    context = label.get_style_context()
    
    if isinstance(tarefa, tuple):
      tarefa = Tarefa(tarefa[2], tarefa[1], tarefa[0])
    tarefa.situacao = 'feito'

    if widget.props.active:
      if tarefa.atualizar():
        context.remove_class('label-todo')
        context.add_class('label-done')
    else:
      if tarefa.atualizar():
        context.remove_class('label-done')
        context.add_class('label-todo')
        tarefa.situacao = 'pendente'
        tarefa.atualizar()


class Application(Gtk.Application):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, application_id='org.pythongtk.application', flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE, **kwargs)

  def do_startup(self):
    Gtk.Application.do_startup(self)
    MainWindow(application=self, title="Lista de tarefas")

  def do_activate(self):
    for window in self.get_windows():
      window.show_all()
      window.present()

  def do_command_line(self, command_line):
    self.activate()
    return True

  def on_quit(self, action, param):
    self.quit()


if __name__ == '__main__':
  application = Application()
  application.run(sys.argv)