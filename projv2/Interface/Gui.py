import PySimpleGUI as sg
import os
import shutil

tech_Degrees = ['Computer Science','Computer Engineering','Information Technology','Information Systems','Software Engineering','Data Science','Data Analytics','Cybersecurity','Information Security','Artificial Intelligence','Machine Learning']
non_tech_Degrees = ['Business','Economics']

tech_fields = ['SE','DS','IT','CS']
non_tech_fields = ['Sales','Accounting']

sg.theme('Dark Grey 13')   # Add a touch of color
# All the stuff inside your window.
NAME_SIZE = 30
def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + ' '*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

def newCert(i):
    return [[name('Field:'), sg.OptionMenu(tech_fields+ non_tech_fields,s=(15,2), key='-CertField-'+str(i))],
            [name('Name:'),  sg.InputText(key='-CertName-'+str(i))]]

def newDegree(i):
    return [[name('Degree: '), sg.OptionMenu(tech_Degrees+non_tech_Degrees,s=(15,2), key='-Degree-'+str(i))]]

def newWork(i):
    return[[name('Field:'), sg.OptionMenu(tech_fields+ non_tech_fields,s=(15,2),key='-WorkField-'+str(i))],
           [name('years:'),sg.InputText(key='-WorkYears-'+str(i))]]
    
# sg.theme(t)
layout_l = [
            [name('Enter your gender'),sg.Radio('Male', 1, key='Male'),sg.Radio('Female',1, key='Female')],
            [name('Enter your degree(s):'), sg.Button('+', key='-+Deg-')],
            [sg.Frame('',[[]], key='-Degree-')],
            [name('Enter your certificate(s):'), sg.Button('+', key='-+Cert-')],
            [sg.Frame('',[[]], key='-Cert-')],
            [name('Enter your Work Experience(s):'), sg.Button('+', key='-+Work-')],
            [sg.Frame('',[[]], key='-Work-')],
            [sg.Button('Ok', key='Submit'), sg.Button('Cancel')]
        ]

layout_r = [
    [sg.Text('You Are Qualified For THe Following Jobs', size=(50,1), pad=(50,10), font='Courier 10')],
    [sg.Text('', key='-Jobs-', size=(50,10), pad=(50,10), font='Courier 10')]
]

layout = [[sg.Col(layout_l), sg.Col(layout_r, element_justification='t')]]
def writeToFile(Gender, Degs, Certs, Work):
    with open('facts.kfb', 'a') as f:
        if(Gender[0] == 1):
            f.write("gender('male')\n")
        elif (Gender[1] == 1):
            f.write("gender('female')\n")
        for deg in Degs:
            if(deg in tech_Degrees):
                f.write("tech_degree('"+deg+"')\n")
            elif(deg in non_tech_Degrees):
                f.write("buisness_degree('"+deg+"')\n")
        for cert in Certs:
            cert = cert.split()
            if(cert[0] in tech_fields):
                f.write("tech_cert('"+cert[0]+"','"+ cert[1] +"')\n")
            elif(cert[0] in non_tech_fields):
                f.write("buisness_cert('"+cert[0]+"','"+ cert[1] +"')\n")
        for work in Work:
            work = work.split()
            if(work[0] in tech_fields):
                f.write("tech_experience('"+work[0]+"',"+ work[1] +")\n")
            elif(work[0] in non_tech_fields):
                f.write("buisness_experience('"+work[0]+"',"+ work[1] +")\n")

        

# Create the Window
window = sg.Window('HR', layout)
certs = 0
degs = 0
work= 0
elements= 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if (event == '-+Deg-'):
        window.extend_layout(window['-Degree-'], newDegree(degs))
        degs+=1
    if (event == '-+Cert-'):
        window.extend_layout(window['-Cert-'], newCert(certs))
        certs+=1
    if (event == '-+Work-'):
        window.extend_layout(window['-Work-'], newWork(work))
        work+=1
    if (event == 'Submit'):
        Gender = [values['Male'], values['Female']]
        Degs = [values['-Degree-'+str(i)] for i in range(degs)]
        Certs = [values['-CertField-'+str(i)] + ' ' + values['-CertName-'+str(i)] for i in range(certs)]
        Work = [values['-WorkField-'+str(i)] + ' ' + values['-WorkYears-'+str(i)] for i in range(work)]
        writeToFile(Gender, Degs, Certs, Work)
        os.system('python driver.py')
        with open('results.txt', 'r') as f:
            result = f.readlines()
        rstring = ''
        for res in result:
            rstring += res + '\n'

        # window['-Jobs-'].update(value='')
        print(rstring)
        window['-Jobs-'].update(str(rstring))
        ## removes the content of the facts.kfb file
        with open('facts.kfb', 'w') as f:
            f.write('')
        try:
            shutil.rmtree('compiled_krb')
        except FileNotFoundError:
            pass


window.close()