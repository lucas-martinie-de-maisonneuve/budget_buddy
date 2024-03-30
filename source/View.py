from source.pygame_manager.Screen import Screen
from source.gui.LogIn import LogIn
from source.gui.HomePage import HomePage

def display():
    s = Screen()
    l = LogIn()

    while not l.quit:
        if l.login_running:
            l.login_run()
        elif l.register_running:
            l.register_run()
        elif l.connected or h.accounts_running:
            if l.connected:
                h = HomePage(l.user)
                l.connected = False
            h.homepage_run()
            if h.profile_display:
                h.profile_design()
            elif h.checking_saving_display:
                h.saving_checking_design()
            elif h.transfer_display:
                h.transaction_design()
            h.top_bar()

        elif h.disconnected:
            l.login_running = True

        s.update()