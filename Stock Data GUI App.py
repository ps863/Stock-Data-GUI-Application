from tkinter import *
from  tkinter.font import Font
import requests
import locale

class App:
    """GUI app that retrieve stock price for a company listed on the NYSE"""
    def __init__(self,window_name):
        """Initializes the main window of GUI application"""
        #Setting name of main window title
        window_name.title("Stock Data Price Finder")

        # Inserting Main Title Label
        main_title = Label(window_name, text="Stock Data Collector", bg='yellow', font="Verdana 48 bold italic")
        main_title.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.5, anchor=CENTER)

        # Insert Entry Widget
        self.stock_name_entry = Entry(window_name)
        self.stock_name_entry.place(relx=0.5, rely=0.6, relwidth=0.3, anchor=CENTER)

        # Label of Entry Widget
        stock_name = Label(window_name, text="Ticker Symbol:")
        stock_name.place(relx=0.3, rely=0.6, anchor=CENTER)

        # Inserting the stock Data Button
        get_stock_data = Button(window_name, text="Get Stock Price",
                                command=lambda :self.other_window(window_name))
        get_stock_data.place(relx=0.4, rely=0.7, anchor=CENTER)

        # Inserting the Quit button
        quit_button = Button(window_name, text="Quit", command=window_name.destroy)
        quit_button.place(relx=0.6, rely=0.7, anchor=CENTER)
        window_name.mainloop()


    def getCompanyData(self,ticker_name):
        """Returns the stock price for a given company on the NYSE, using API"""
        locale.setlocale(locale.LC_ALL, '')
        try:
            source_site = 'https://financialmodelingprep.com/api/v3/stock/real-time-price'  # This is the source site
            if (len(ticker_name) == 0):
                return "You must enter a company name "
            company_name = "/" + str(ticker_name)
            query = source_site + company_name
            url = requests.get(query)
            jsonObj = url.json()
            output=locale.currency(jsonObj["price"], grouping=True)
            return output
        except:
            return "Invalid ticker symbol. Please enter a valid ticker symbol for a company"


    def other_window(self,window_name):
        """Sets up second window to display outcome of user request for stock data"""
        window=Tk()
        window.title('Stock Price')
        window.configure(background='light blue')
        message = self.getCompanyData(self.stock_name_entry.get())
        if (message=="Invalid ticker symbol. Please enter a valid ticker symbol for a company"):
            toPrint = Label(window, text="Invalid ticker symbol! Please enter a valid ticker symbol for a company", font=" Verdana 16 bold italic", bg='red',fg='white')
            toPrint.place(relx=0.5, rely=0.4, anchor=CENTER)
            quit_button = Button(window, text="Close", command=window.destroy)
            quit_button.place(relx=0.5, rely=0.7, anchor=CENTER)
        else:
            stringToShow = "Current Stock Price:" + str(message)
            toPrint = Label(window, text=stringToShow, font=" Verdana 16 bold italic",bg='light green')
            toPrint.place(relx=0.5, rely=0.4, anchor=CENTER)
            quit_button = Button(window, text="Close", command=window.destroy)
            quit_button.place(relx=0.5, rely=0.7, anchor=CENTER)

stock=App(window_name=Tk())
