import PySimpleGUI as b

b.theme('Topanga')

layout = [[b.Text("")],[b.Text("Choose source folder: ", size = (20,1)), b.InputText(readonly = True), b.FolderBrowse()],[b.Text("Choose destination folder: ", size = (20,1)), b.InputText(readonly = True), b.FolderBrowse()], [b.Text("")],[b.Button("Submit", size = (8,1))]]

window = b.Window("Pyhton Project", layout, size = (600,200))

while True:
    event, m = window.read()

    if m[0] == '':
        print("Please enter a source path")
        continue

    if m[1] == '':
        print("Please enter a destination path")
        continue
    if event == b.WIN_CLOSED or event == "Exit":
        break

    elif event == "Submit":
        source = m[0]
        destination = m[1]
        break