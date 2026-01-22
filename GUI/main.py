import PySimpleGUIQt as sg

layout = [
    [sg.Text("Minha primeira Interface Grafica")],
    [sg.Button("OK")]
]

window = sg.Window("Minha primeira Janelinha", layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WINDOW_CLOSED:
        break

window.close()