import PySimpleGUI as sg

class GUI(object):
    def new_picture(self):
        layout = [[sg.Text('New Picture?')],
                                [sg.Submit('YES'), sg.Cancel('NO')]]

        window = sg.Window('New Picture', layout)

        event, values = window.Read()
        window.Close()
        return event

    def image_view(self, image_path):
        layout = [[sg.Text('Möchten sie dieses Bild speichern?')],
                        [sg.Image(image_path, size=(800,360))],
                        [sg.Submit('Speichern'), sg.Cancel('Erneut aufnehmen')]]

        window = sg.Window('Bild speichern?', layout)
        event, values = window.Read()

        window.Close()
        pass

    def Analyse(self):
        layout = [[sg.Text('Choose Features to Analyse:')],
                                [sg.Checkbox('Vessel Segmentation')],
                                [sg.Checkbox('Ateries-Veins Segmentation')],
                                [sg.Checkbox('Optic-Disk Segmentation')],
                                [sg.Submit(), sg.Cancel()]]

        window = sg.Window('Choose Segmentation', layout)

        event, values = window.Read()
        window.Close()
        return values

    def l_or_r(self):
        layout = [[sg.Text('LEFT or RIGHT Eye?')],
                                [sg.Submit('Left'), sg.Submit('Right')]]

        window = sg.Window('Left or Right Eye', layout)

        event, values = window.Read()
        window.Close()
        return event

    def last_name(self):
        layout = [[sg.Text('Enter Last Name.')],
                                [sg.Text('This will be the filename!')],
                                [sg.InputText()],
                                [sg.Submit(), sg.Cancel()]]

        window = sg.Window('Enter Last Name', layout)

        event, values = window.Read()
        window.Close()
        return values

    def select(self):
        layout = [[sg.Text('Choose Patient Image')],
                                [sg.Input(),sg.FileBrowse()],
                                [sg.Submit(), sg.Cancel()]]

        window = sg.Window('Choose Patient', layout)

        event, values = window.Read()
        window.Close()
        return values
