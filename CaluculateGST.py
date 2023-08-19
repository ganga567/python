#Write a python program to caluculate GST of Goods.
#a)create a class with goods information (Attributes and behaviour)
#input the data of goods class objects into file....GoodsInfofile.txt(input data file)
#create a file format before inserting the data.
#read the particular category records from the file and calxculate the GST (5%,14%,18%)
#GST caluculated
#---file name =gstpaid.txt

class GoodsGST:
    ProductName = "Product Name"
    Quantity = "Qty"
    Price = "Price"
    GstPercentage = "GST Percentage"

    def __int__(self,PName,Qty,Price,GstPc):
        self.ProductName = PName
        self.Quantity = Qty
        self.Price = Price
        self.GstPercentage = GstPc
    def DisplayDetails(self):
        print("The Attributes are : ","\n",self.ProductName,"\n",self.Quantity,"\n",self.Price,"\n",self.GstPercentage)
    def UpdateValues(self):
            self.ProductName = input("Enter The name of the Product : ")
            self.Quantity = int(input("Enter the Quantity of the Product : "))
            self.Price = int(input("Enter the price of the Product : "))
            self.GstPercentage = float(input("Enter The GST Percentage : "))
    def CalculateGST(self):
        GST = (self.Price * self.GstPercentage) / 100
        print("The GST on ",self.ProductName,"is : ",GST)

emptyObj = GoodsGST()
emptyObj.DisplayDetails()
emptyObj.UpdateValues()
emptyObj.CalculateGST()


'''import os                                                                                                                                                                                                            

print(os.getcwd())
newfile = ("C:\\Users\Gangadhar\PycharmProjects\pythonProject2\\venv\goodsinfofile.text","a+")
newfile.seek(0,0)

newfile = open("goods infofile.text","a+")'''
