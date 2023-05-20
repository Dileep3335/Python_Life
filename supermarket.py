from datetime import datetime

print("="*40,"MANGO MART","="*40)
name=str(input("Enter you name : "))
print("Welcome ",name)
lists='''
Items available in our store

Item             Price       Item_code
----------------------------------------
Rice             Rs 50/KG       1
Salt             Rs 15/kg       2
Sugar            Rs 40/kg       3
dry chilli       Rs 100/kg      4
groundnuts       Rs 50/kg       5
milk             Rs 70/Li       6
Palm oil         Rs 90/Li       7
Sunflower oil    Rs 190/Li      8
Eggs             Rs 72/Dz       9
Oreo biscuits    Rs 96          10
soap             Rs 45          11
----------------------------------------
Please Use Item_code while ordering the Item
          Thank you 
'''
Grand_total=0
bill={}            #Dictionary for storing bill details
print(lists)
n=int(input("Press 1 to continue shopping.\nYour answer : "))
Item={1:{"item":"RICE",          "Price":50,        "measurement":"KG"},
      2:{"item":"SALT",          "Price":15,        "measurement":"KG"},
      3:{"item":"SUGAR",         "Price":40,        "measurement":"KG"},
      4:{"item":"DRY_CHILLI",    "Price":100,       "measurement":"KG"},
      5:{"item":"GROUND_NUTS",   "Price":50,        "measurement":"KG"},
      6:{"item":"MILK",          "Price":70,        "measurement":"Li"},
      7:{"item":"PALM_OIL",      "Price":90,        "measurement":"Li"},
      8:{"item":"SUNFLOWER_OIL", "Price":190,       "measurement":"Li"},
      9:{"item":"EGGS",          "Price":72,        "measurement":"DZ"},
      10:{"item":"OREO_BISCUITS","Price":96,        "measurement":"  "},
      11:{"item":"SOAP",         "Price":45,        "measurement":"  "},
      }                    #Nested dictionary for storing items available in the store
while True:
    a=int(input("Enter Item_Code for your choice or Enter 0 to generate bill : "))
    if(a!=0 and a<=11):                 #"a" refers item_code, which are declared as keys in above Dictionary
        print("You have selected",Item[a]["item"], "Enter quantity in",Item[a]["measurement"])
        temp=Item[a]["item"]
        q=float(input("quantity : "))
        price=Item[a]["Price"]*q        #calculating price of an Item for a given quantity
        bill.update({temp:{"quantity":q,"cost":price,"measure":Item[a]["measurement"]}})   
                  #appending "quantity, cost, and measure(kg/litre/dozen)" of an Item into the nested dictionary "bill"
        Grand_total=Grand_total+price
    elif(a==0):   # breaks loop when shopping completed
        break
    else:        # Notifies user when an undefined key is selected
        print("Oops! Undefined Item selection...")

#BILL GENERATION

print(40*"=","bill",40*"=")
print("Mango mart\nAddress : 9/23 IV7, ynb road, Delhi")
print("Name : ",name)
print("Billed date : ",datetime.now())
#Above code snippet is for printing user and shop details in the bill
print("S.NO"," "*9,"Item"," "*11,"Quantity"," "*11,"Price")
print("-"*80)
sno=1
for keys,values in bill.items():       #printing the dictionary "bill" accordingly
    print(sno ," "*12, keys," "*(16-len(keys)), bill[keys]["quantity"],bill[keys]["measure"]," "*12, bill[keys]["cost"],"Rs")
    sno+=1
gst=(Grand_total*5)/100             #GST 5%
print("-"*80)
print("-"," "*12,"GST"," "*33,gst,"Rs")
print("-"," "*12,"Total"," "*31,Grand_total+gst,"Rs")          #Final price
print("="*85)
print(" "*20,"Thanks for visiting")


