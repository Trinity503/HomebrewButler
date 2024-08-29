#Icon-Source: https://iconduck.com/sets/simple-icons "Simple Icons is an Icon Set of 1,461 icons. Each icon is solid, which is useful for changing icon colors. It's been open sourced with the license: Creative Commons Zero v1.0 Universal. All icons can be used for personal & commercial purposes."
#Prerequisities
#pip3 install -U rumps

import rumps
import subprocess

class HomebrewButlerApp(rumps.App):
    def __init__(self):
        super(HomebrewButlerApp, self).__init__("Homebrew Butler", title=None, icon="./media/HomebrewButler_menubar_n.icns")
        #self.app = rumps.App("Homebrew Butler", title=None, icon="./media/HomebrewButler_menubar_n.icns")
        self.check4updates_button = rumps.MenuItem(title="Check for Updates", callback=self.check4updates)
        self.update_all_button = rumps.MenuItem(title="Update all", callback=self.update_all)
        self.menu = [self.check4updates_button, self.update_all_button]

    @rumps.timer(1800)
    def check4updates(self, sender=None):
        #subprocess.run(["ls", "-l"])
        outdated = subprocess.check_output(["brew outdated -v"], shell=True).decode("utf-8")
        #self.app.menu.add(f'Avaible updates: 5')
        
        if len(outdated) > 0:
            print("Outdated: " + outdated)
            self.icon = "./media/HomebrewButler_menubar_y.icns"
            #self.app = rumps.App("Homebrew Butler", title=None, icon="./media/HomebrewButler_menubar_y.icns") 
            if sender == "Timer": # If check was instanced by the menu.  
                rumps.alert(title="Check for updates finished", message='Outdated packages: ' + outdated)
                rumps.notification(title='HomebrewButler', subtitle='Check for updates finished', message='Outdated packages: ' + outdated)
        else:
            print("No outdated packages.")
            self.icon = "./media/HomebrewButler_menubar_n.icns"
            if sender == "Timer": # If check was instanced by the menu.
                rumps.alert(title="Check for updates finished", message='No outdated packages.')
                rumps.notification(title='HomebrewButler', subtitle='Check for updates', message='No outdated packages.')            

    def update_all(self,sender):
        subprocess.run(["brew", "upgrade"])
        self.icon = "./media/HomebrewButler_menubar_n.icns"
    


   

if __name__ == '__main__':
    app = HomebrewButlerApp()
    app.run()