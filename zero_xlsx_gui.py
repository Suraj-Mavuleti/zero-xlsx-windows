import sys
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, Pango

class ZeroXLSX(Gtk.Window):
    def __init__(self):
        super().__init__(title="Zero XLSX - Ultimate Studio")
        self.set_default_size(1300, 800)
        
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = ""
        self.header.get_style_context().add_class("hidden-header")
        self.set_titlebar(self.header)
        
        self.setup_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(main_box)
        
        # ================= TOP RIBBON =================
        ribbon = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        ribbon.get_style_context().add_class("ribbon")
        main_box.pack_start(ribbon, False, False, 0)
        
        logo = Gtk.Label(label="Z E R O X L S X")
        logo.get_style_context().add_class("logo")
        logo.set_margin_start(20)
        logo.set_margin_end(30)
        ribbon.pack_start(logo, False, False, 0)
        
        tools = ["B", "I", "U", "A", "🎨", "💰", "%,", ".00", "📊", "Σ"]
        tbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        tbox.set_valign(Gtk.Align.CENTER)
        
        for t in tools:
            btn = Gtk.Button(label=t)
            btn.get_style_context().add_class("format-btn")
            tbox.pack_start(btn, False, False, 0)
            
        ribbon.pack_start(tbox, False, False, 0)
        
        btn_export = Gtk.Button(label="📤 Export CSV")
        btn_export.get_style_context().add_class("action-btn")
        btn_export.set_valign(Gtk.Align.CENTER)
        btn_export.set_margin_end(20)
        ribbon.pack_end(btn_export, False, False, 0)
        
        # ================= FORMULA BAR =================
        fx_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        fx_bar.get_style_context().add_class("fx-bar")
        main_box.pack_start(fx_bar, False, False, 0)
        
        l_fx = Gtk.Label(label="fx")
        l_fx.get_style_context().add_class("fx-label")
        l_fx.set_margin_start(20)
        l_fx.set_margin_end(10)
        fx_bar.pack_start(l_fx, False, False, 0)
        
        entry_fx = Gtk.Entry()
        entry_fx.set_text("=SUM(B2:B10) * 1.05")
        entry_fx.get_style_context().add_class("fx-entry")
        fx_bar.pack_start(entry_fx, True, True, 20)
        
        # ================= SPREADSHEET GRID =================
        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        main_box.pack_start(scroll, True, True, 0)
        
        grid = Gtk.Grid()
        grid.get_style_context().add_class("sheet-grid")
        
        # Header Row
        cols = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for j, c in enumerate(cols):
            lbl = Gtk.Label(label=c)
            lbl.get_style_context().add_class("grid-header")
            if j == 0: lbl.set_size_request(50, 30)
            else: lbl.set_size_request(120, 30)
            grid.attach(lbl, j, 0, 1, 1)
            
        # Rows
        data = [
            ["1", "Revenue", "$14,500.00", "Q1", "Up", "", "", "", "", "", ""],
            ["2", "Expenses", "$8,200.00", "Q1", "Down", "", "", "", "", "", ""],
            ["3", "Net Profit", "$6,300.00", "Q1", "Up", "", "", "", "", "", ""],
            ["4", "Growth", "+15.4%", "", "", "", "", "", "", "", ""]
        ]
        
        for i in range(1, 25):
            lbl = Gtk.Label(label=str(i))
            lbl.get_style_context().add_class("grid-header")
            lbl.set_size_request(50, 30)
            grid.attach(lbl, 0, i, 1, 1)
            
            for j in range(1, 11):
                entry = Gtk.Entry()
                entry.get_style_context().add_class("cell")
                if i <= len(data) and j < len(data[i-1]):
                    entry.set_text(data[i-1][j])
                grid.attach(entry, j, i, 1, 1)
                
        scroll.add(grid)
        
        # ================= BOTTOM TAB BAR =================
        bot_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        bot_bar.get_style_context().add_class("bot-bar")
        main_box.pack_start(bot_bar, False, False, 0)
        
        for name in ["Sheet1", "Sheet2", "+"]:
            btn = Gtk.Button(label=name)
            btn.get_style_context().add_class("sheet-tab")
            if name == "Sheet1": btn.get_style_context().add_class("sheet-tab-active")
            bot_bar.pack_start(btn, False, False, 0)

    def setup_css(self):
        css = b'''
            window { background-color: #030305; }
            .hidden-header { background: #030305; min-height: 0px; padding: 0px; border: none; box-shadow: none; }
            .ribbon { background-color: rgba(10, 12, 18, 0.98); border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding: 15px 0px; }
            .logo { color: #FFFFFF; font-size: 20px; font-weight: 900; letter-spacing: 5px; text-shadow: 0 0 15px rgba(0, 204, 102, 0.6); }
            .format-btn { background: transparent; color: #FFFFFF; border: 1px solid transparent; border-radius: 8px; font-weight: bold; padding: 8px 12px; transition: all 0.2s ease; }
            .format-btn:hover { background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); }
            .action-btn { background: linear-gradient(45deg, #00CC66, #00994C); color: #FFFFFF; border-radius: 8px; font-weight: bold; padding: 8px 15px; border: none; box-shadow: 0 5px 15px rgba(0, 204, 102, 0.3); transition: all 0.3s; }
            .action-btn:hover { box-shadow: 0 8px 25px rgba(0, 204, 102, 0.5); }
            .fx-bar { background-color: #0A0D14; padding: 10px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); }
            .fx-label { color: #00CC66; font-family: serif; font-size: 20px; font-style: italic; font-weight: bold; }
            .fx-entry { background: #1C2333; color: #FFFFFF; border: 1px solid rgba(0,204,102,0.3); border-radius: 4px; padding: 8px; font-family: monospace; font-size: 14px; }
            .sheet-grid { background-color: #030305; }
            .grid-header { background: #10141E; color: #8B94A5; border: 1px solid #1C2333; font-weight: bold; font-size: 12px; }
            .cell { background: #050608; color: #FFFFFF; border: 1px solid #10141E; padding: 5px; box-shadow: none; border-radius: 0; font-size: 13px; }
            .cell:focus { border: 2px solid #00CC66; background: rgba(0,204,102,0.05); }
            .bot-bar { background-color: #080A0F; border-top: 1px solid rgba(255, 255, 255, 0.05); }
            .sheet-tab { background: transparent; color: #8B94A5; border: none; padding: 10px 20px; font-weight: bold; border-radius: 0; border-right: 1px solid #1C2333; }
            .sheet-tab:hover { background: rgba(255,255,255,0.05); color: #FFFFFF; }
            .sheet-tab-active { background: #10141E; color: #00CC66; border-bottom: 2px solid #00CC66; }
        '''
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = ZeroXLSX()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
