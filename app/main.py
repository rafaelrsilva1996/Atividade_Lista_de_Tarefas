import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk, GdkPixbuf

from crud_tarefa import Tarefa
from webdriver.bscscan import get_token_list_per_wallet

class MainWindow(Gtk.ApplicationWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.set_default_size(500, 500)

    self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.entry = Gtk.Entry(placeholder_text = "Digite aqui adress wallet")
    self.btn = Gtk.Button(label="Pesquisar")

    self.add(self.box)
    self.box.pack_start(self.entry, False, True, 0)
    self.box.pack_start(self.btn, False, True, 0)

    self.btn.connect('clicked', self.btn_press)

    self.css_provider = Gtk.CssProvider()
    self.css_provider.load_from_path('style.css')

  def btn_press(self, widget):
    self.show_all()

    adress_wallet = self.entry.props.text
    adress_wallet = '0x7d3d35878a8d6732a0abc296f0c57426c5a7d75e'
    
    print(get_token_list_per_wallet(adress_wallet))
    df = get_token_list_per_wallet(adress_wallet)

    self.do_process(dataframe=df, adress_wallet=adress_wallet)


    # win = SecondWindow(title="CryptoGames")
    # win.connect("destroy", Gtk.main_quit)
    # print('Acionando do_process')
    # win.do_process(dataframe=df, adress_wallet=adress_wallet)
    # win.show_all()

    # SecondWindow(title="CryptoGames").do_process(dataframe=df)


# class SecondWindow(Gtk.ApplicationWindow):
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)

#     self.set_default_size(500, 500)

  def do_process(self, dataframe, adress_wallet):
    print('Entrou do_process')
    print(self)

    win = Gtk.Window(title="CryptoGames")
    win.set_default_size(800, 600)
    win.connect("destroy", Gtk.main_quit)
    

    label = Gtk.Label(label = adress_wallet)
    # self.box.pack_start(self.label, True, True, 0)

    win.add(label)

    win.show_all()
    Gtk.main()

    # self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    # self.label = Gtk.Label(label = adress_wallet)
    # self.box.pack_start(self.label, True, True, 0)
      
    # self.lst_box = Gtk.ListBox()
    # self.box.pack_start(self.lst_box, False, True, 0)

    # for value in dataframe.values:
    #   label_text = f'{value[0]}, {value[1]}, {value[2]}'      

    #   self.label = Gtk.Label(label = label_text)
    #   self.box.pack_start(self.label, True, True, 0)

    #   self.lst_box.insert(self.box, 0)
    #   self.show_all()
    #   print(f'{value[0]}, {value[1]}, {value[2]}')
    
    print('FIM')


class Application(Gtk.Application):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, application_id='org.pythongtk.application', flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE, **kwargs)

  def do_startup(self):
    Gtk.Application.do_startup(self)
    MainWindow(application=self, title="CryptoGames")

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