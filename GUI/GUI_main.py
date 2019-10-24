import gui_design                   #Import the GUI Design
import cam                          #Import Camera Settings
from subprocess import call         #for Shutdown Command
import os                           #to be able to delete Pictures

camera = cam.Cam();                 #initialize the Camera
gui_design = gui_design.GUI()           #Start the GUI
while True :
    np = gui_design.new_picture();    #Abfrage, ob neuer Patient

    if np == 'YES':
        ln = gui_design.last_name()
        last_name = ln[0]
        if last_name != None and last_name != '':     #Rotes Kreuz gedrückt
            image_path = '/home/pi/Pictures/' + last_name + '.png'
            image_path_ext = '//home//pi//Pictures//' + last_name + '.png'
            l_r = gui_design.l_or_r();#Abfrage linkes oder rechtes Auge

            if l_r == 'Left':       #linkes Auge wird fotografiert
                camera.capture(last_name);
                save = gui_design.image_view(image_path_ext);
                if save == 'Erneut aufnehmen':
                    os.remove(image_path)
                continue

            elif l_r == 'Right':    #rechtes Auge wird fotografiert
                camera.rotate_capture(last_name);
                save = gui_design.image_view(image_path_ext);
                if save == 'Erneut aufnehmen':
                    os.remove(image_path)
                continue
        break

    if np == 'NO':
        s = gui_design.select();
    ##experimental, not finished##
        if s[0] != '' and s[0] != None:
            select = gui_design.Analyse()
            if select[0] == 'True':             #0 = Ves Seg.
                break
            if select[1] == 'True':              #1 = AV Seg.
                break#send to
            if select[2] == 'True':             #2 = OD Seg.
                break#send to

        break

    else:                       #Red X pressed
        #call("sudo nohup shutdown -h now", shell=True);
        break
