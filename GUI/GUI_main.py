import gui_alle                     #import der GUI
import cam                          #import der Cam-Funktionen
from subprocess import call         #für shutdown command
import os                           #zum löschen der Bilder

camera = cam.Cam();                 #Init der Cam
gui_alle = gui_alle.GUI()           #Init der GUI
while True :
    np = gui_alle.new_picture();    #Abfrage, ob neuer Patient

    if np == 'YES':
        ln = gui_alle.last_name()
        last_name = ln[0]
        if last_name != None and last_name != '':     #Rotes Kreuz gedrückt
            image_path = '/home/pi/Pictures/' + last_name + '.png'
            image_path_ext = '//home//pi//Pictures//' + last_name + '.png'
            l_r = gui_alle.l_or_r();#Abfrage linkes oder rechtes Auge

            if l_r == 'Left':       #linkes Auge wird fotografiert
                camera.capture(last_name);
                save = gui_alle.image_view(image_path_ext);
                if save == 'Erneut aufnehmen':
                    os.remove(image_path)
                continue

            elif l_r == 'Right':    #rechtes Auge wird fotografiert
                camera.rotate_capture(last_name);
                save = gui_alle.image_view(image_path_ext);
                if save == 'Erneut aufnehmen':
                    os.remove(image_path)
                continue
        break

    if np == 'NO':
        s = gui_alle.select();

        if s[0] != '' and s[0] != None:
            select = gui_alle.Analyse()
            if select[0] == 'True':             #0 = Ves Seg.
                break
            if select[1] == 'True':              #1 = AV Seg.
                break#send to
            if select[2] == 'True':             #2 = OD Seg.
                break#send to

        break

    else:                       #Rotes Kreuz gedrückt
        #call("sudo nohup shutdown -h now", shell=True);
        break
