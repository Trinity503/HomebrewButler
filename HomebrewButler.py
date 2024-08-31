#Icon-Source: https://iconduck.com/sets/simple-icons "Simple Icons is an Icon Set of 1,461 icons. Each icon is solid, which is useful for changing icon colors. It's been open sourced with the license: Creative Commons Zero v1.0 Universal. All icons can be used for personal & commercial purposes."
#Prerequisities
#pip3 install -U rumps

#If the icon is coloured, there are updates available.
#brew needs its full path for working as a menu-bar-app, because the shell works different than as if started within a terminal
#When launched without Terminal the subprocessed seems to dont work - solved by giving the full path for brew
#get directory for brew (which brew) command  - does not work either

#ToDo
#Make the Timer configurable
#Notifications not working

import rumps
import subprocess
import os

checkinterval = 1800
#which_brew = os.popen('which brew').read().rstrip()

class HomebrewButlerApp(rumps.App):
    def __init__(self):
        super(HomebrewButlerApp, self).__init__("Homebrew Butler", title=None, icon="./media/HomebrewButler_menubar_n.icns")
        self.check4updates_button = rumps.MenuItem(title="Check for Updates", callback=self.check4updates)
        self.update_all_button = rumps.MenuItem(title="Update all", callback=self.update_all)
        self.menu = [self.check4updates_button, self.update_all_button]
 
    @rumps.timer(checkinterval)
    def check4updates(self, sender=None):
        
        #find out who started "check4updates". If it was the menu then show notifications. If it was the timer, then don't show them.
        if hasattr(sender, 'title'):
            notifications = True
        else:
            notifications = False
        
        command_update = '/usr/local/bin/brew update'
        os.popen(command_update)

        command_outdated = '/usr/local/bin/brew outdated -v'
        outdated = os.popen(command_outdated).read()
                
        if len(outdated) > 0:
            print("Outdated: " + outdated)
            self.icon = "./media/HomebrewButler_menubar_y.icns"
            if notifications: # If check was instanced by the menu.  
                rumps.alert(title="Check for updates finished", message='Outdated packages: ' + outdated)
                rumps.notification(title='HomebrewButler', subtitle='Check for updates finished', message='Outdated packages: ' + outdated)
        else:
            print("No outdated packages.")
            self.icon = "./media/HomebrewButler_menubar_n.icns"
            if notifications: # If check was instanced by the menu.
                rumps.alert(title="Check for updates finished", message='No outdated packages.')
                rumps.notification(title='HomebrewButler', subtitle='Check for updates', message='No outdated packages.')            

    def update_all(self,sender):
                
        #removed 'W' for wait, because this crashed HomebreButler, perhaps because of waiting for ALL Terminals to close.
        #This was the only way that a windows opens, which is required to see if the sudo password is required.
        subprocess.run(['open', '-a', 'Terminal.app', 'brew_upgrade.sh'])

        self.icon = "./media/HomebrewButler_menubar_n.icns"


if __name__ == '__main__':
    app = HomebrewButlerApp()
    app.run()