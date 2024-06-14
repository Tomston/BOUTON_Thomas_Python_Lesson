class data():

    # Constructor by default
    def __init__(self):
        ...

    # numpy.array() pour les matrices 2D - à voir
    def Nasdaq_data_index(self):
        self.Nasdaq_date = ["3 months", "1 year", "5 years", "10 years"]
        self.Nasdaq_performance = ["8.35%", "31.38%", "160.65%", "418.52%"]
  
    def SP500_data_index(self):
        self.SP500_date = ["3 months", "1 year", "5 years", "10 years"]
        self.SP500_performance = ["5.20%", "24.37%", "87.91%", "180.65%"]

    def CAC40_data_index(self):
        self.CAC40_date = ["3 months", "1 year", "5 years", "10 years"]
        self.CAC40_performance = ["-5,28%", "5.72%", "43.39%", "69.66%"]

    def Eurostoxx50_data_index(self):
        self.Eurostoxx50_date = ["3 months", "1 year", "5 years", "10 years"]
        self.Eurostoxx50_performance = ["-1.30%", "19.60%", "45.57%", "50.34%"]


    def MSCIWORLD_data_index(self):
        self.MSCIWORLD_date = ["3 months", "1 year", "5 years", "10 years"]
        self.MSCIWORLD_performance = ["3.19%", "19.62%", "63.99%", "102.90%"]
