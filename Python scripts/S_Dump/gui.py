import matplotlib
matplotlib.use("TkAgg") # backend of the matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
#ttk is used for getting better buttons
from tkinter import ttk
LARGE_FONT  = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT  = ("Verdana", 8)
style.use("ggplot")

f = Figure(figsize=(6, 4), dpi=100)
a = f.add_subplot(111)  # plot number 1X1

exchange = "BTC-e"
DatCounter = 9000
programName = "btce"
resampleSize = "15 min"
DataPace = "1d"
candleWidth = 0.008
topIndicator = "none"

def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    else:
        DataPace = tf
        DatCounter = 9000

def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    elif what == "none":
        topIndicator = what
        DatCounter = 9000

    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)

            topIndicator = group
            DatCounter = 9000
            print("Set top indicator to", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == "macd":
        topIndicator = "macd"
        DatCounter = 9000


def changeExchange(toWhat, pn):
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName = pn
    DatCounter = 9000


def popupmsg(msg):
    popup = tk.Tk()

    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORMAL_FONT)
    label.pack(side="top", fill="x", pady=10)
    button1= ttk.Button(popup, text="Okay", command=popup.destroy)
    button1.pack()
    popup.mainloop()


def animate(i):
    '''dataLink = 'https://api.btcmarkets.net/market/BTC/AUD/trades'
    response = requests.get(dataLink)
    data = response.json()
    df = pd.DataFrame(data)
    print(df)'''
    #buys = df[(data['date']=='1545423317')]
    #print(buys)


    #api key = c61d71fc-0763-434e-92ba-4aa4ec0e0d9d


    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x, y = eachLine.split(',')
            xList.append(str(x))
            yList.append(float(y))

    #clear the graphs so they can be redrawn
    a.clear()
    a.plot(xList, yList)

    # the legend goes outside the graph
    #a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)

    title = "Employees hours"
    a.set_title(title)

class SeaofBTCapp(tk.Tk): #between parenthesis I have inheritance

    def __init__(self, *args, **kwargs): #kwargs keyword dictionaries wh
        """This is the constructor that initalizes the window once the program is started."""
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="logo_python.ico")
        tk.Tk.wm_title(self, "EY Audits")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported yet") )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        # add the filemenu to the menu bar
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="BTC-e",
                                   command=lambda: changeExchange("BTC-e", "btce"))
        exchangeChoice.add_command(label="Bitfinex",
                                   command=lambda: changeExchange("Bitfinex", "bitfinex"))
        exchangeChoice.add_command(label="Bitstamp",
                                   command=lambda: changeExchange("Bitstamp", "bitstamp"))
        exchangeChoice.add_command(label="Huobi",
                                   command=lambda: changeExchange("Huobi", "huobi"))

        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label = "Tick",
                           command=lambda: changeTimeFrame('tick'))
        dataTF.add_command(label="1 Day",
                           command=lambda: changeTimeFrame('1d'))
        dataTF.add_command(label="3 Days",
                           command=lambda: changeTimeFrame('2d'))
        dataTF.add_command(label="1 Week",
                           command=lambda: changeTimeFrame('7d'))

        menubar.add_cascade(label = "Data Time Frame", menu=dataTF)

        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None",
                            command= lambda: addTopIndicator('None'))
        topIndi.add_command(label="RSI",
                            command=lambda: addTopIndicator('rsi'))
        topIndi.add_command(label="MACD",
                            command=lambda: addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        # navigation is used here
        # this is used to display all the elements in the GUI
        for F in (StartPage, PageOne, PageTwo, BTC_page):
            frame = F(container, self)
            self.frames[F] = frame
            # stretch everything to all parts of the window
            frame.grid(row=0, column=0, sticky="nsew")

        #start in the main page
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#def quick_function(param):
#    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = """Auditing application, use it at your own risk.""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        #button1 = tk.Button(self, text="Visit page 1",
        #                    command= lambda: quick_function("The button is working!"))

        button1 = ttk.Button(self, text="Agree",
                            command= lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",command=quit)
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button2 = ttk.Button(self, text="View graph",
                            command=lambda: controller.show_frame(BTC_page))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

class BTC_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()







