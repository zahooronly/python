# from turtle import Turtle, Screen
from prettytable import PrettyTable


# def onScreenClick(x, y):
#     myScreen.bye()  # Close the screen when clicked


# myTurtle = Turtle("turtle")
# myTurtle.color('coral')
# myTurtle.forward(100)
# myScreen = Screen()
# print(myScreen.canvheight)

# myScreen.onclick(onScreenClick)  # Register the click event

# myScreen.mainloop()  # Keep the screen open until closed by the user
AGNumbers = [
    "2020-ag-6389","2021-ag-7738","2021-ag-7743","2021-ag-7744","2021-ag-7745","2021-ag-7748","2021-ag-7751","2021-ag-7754","2021-ag-7756","2021-ag-7758","2021-ag-7760","2021-ag-7765","2021-ag-7768","2021-ag-7769","2021-ag-7772","2021-ag-7774","2021-ag-7775","2021-ag-7776","2021-ag-7777","2021-ag-7781","2021-ag-7784","2021-ag-7785","2021-ag-7786","2021-ag-7789","2021-ag-7791","2021-ag-7793","2021-ag-7795","2021-ag-7796","2021-ag-7797","2021-ag-7800","2021-ag-7801","2021-ag-7802","2021-ag-7803","2021-ag-7806","2021-ag-7808","2021-ag-7811","2021-ag-7812","2021-ag-7813","2021-ag-7815","2021-ag-7817","2021-ag-7828","2021-ag-7832","2021-ag-7834","2021-ag-7836","2021-ag-7837","2021-ag-7839","2021-ag-7841","2021-ag-7842","2021-ag-7843","2021-ag-7844","2021-ag-7846","2021-ag-7848","2021-ag-7854","2021-ag-7858","2021-ag-7864","2021-ag-7866","2021-ag-7867","2021-ag-7869","2021-ag-7874","2021-ag-7875","2021-ag-7876","2021-ag-7879","2021-ag-7880","2021-ag-7882","2021-ag-7883"]
names = [
    "NISHA SHARIF", "MUHAMMAD ARSLAN", "ELSA", "TANZILA", "MUHAMMAD ARFAN",
    "MUZAMMIL HUSSAIN", "ZAHOOR AHMAD", "NOOR FATIMA", "NATASHA ANWAR",
    "MUHAMMAD ARHAM MURTAZA", "ZARNAB NADEEM", "MUHAMMAD JAWAD",
    "MUHAMMAD ABUZAR", "ALI ABBAS", "BUSHRA SHAFIQUE", "ASIF DANYAL",
    "MUHAMMAD FAIZAN", "KALSOOM TAHIR", "SHAHZMAN MAZHAR", "MUHAMMAD TALHA",
    "KHADIJA", "HURAIRA AHMAD ZAHID", "ABDUL RAZZAQ", "ZARQA NAWAZ",
    "MUHAMMAD SAAD BIN KHALID", "HASSAN MUKHTAR", "SHERAZ AHMAD",
    "MUHAMMAD UMAR SHEHZAD", "DANISH IJAZ", "ZOHA ASGHAR",
    "SYED MUHAMMAD ZAEEM FAROOQ", "KASHAF NOOR", "MUHAMMAD AHMAD",
    "MUHAMMAD IMRAN", "HAMZA MUSHARAF", "NOOR FATIMA", "MUHAMMAD ILYAS CHISHTI",
    "VANEEZA NOOR", "HASSAN MANZOOR", "YUSRA SAJJAD", "SOHAIB KHAWER",
    "USWAH IHSAN KHAN", "MUHAMMAD SHERAZ", "SAHIL JAHAN", "BUSHRA FATIMA",
    "FAKHAR ABBAS", "UMAR ANAYAT", "WAQAR AKRAM BHUTTA", "SHAHZAIB ALI",
    "AHMAD SABOOR", "MOAZZAM ABBAS", "ZAFAR IQBAL", "ASAD DILAWAR",
    "AHMAD NAZIR", "AHSAN ALI", "LAIBA KHAWAR", "AMNA", "NOOR UL HUDA",
    "MUHAMMAD UMAR", "MUHAMMAD HARIS ABBAS", "AREEBA", "ZAIN-UL-ABIDEN",
    "IQRA ZAFAR RAO", "ABDULLAH BIN TAHIR", "Placeholder"  # Add a placeholder value
]
myTable=PrettyTable()
myTable.add_column('AG Numbers',AGNumbers)
myTable.add_column('Names',names)
myTable.align='l'
print(myTable)

# just practice here!