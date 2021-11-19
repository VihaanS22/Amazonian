import csv
import pandas as pd
import plotly.figure_factory as pf
import plotly.express as px
import plotly.graph_objects as go

print("")
print("Amazonian")
print("- A mobile rater")
print("")
print("Hi there...Please choose your type of mobile and check the rating of that mobile.")
print("")
print("Given below are the list of mobiles - ")
print("")
print("Samsung")
print("Apple")
print("Nokia")
print("Motorala")
print("HUAWEI")
print("ASUS")
print("Google")
print("OnePlus")
print("Sony")
print("Xiaomi")
print("")
print("Do you want to see all mobile ratings? Type in 'Every Rating'")

print("")
mob = input("please enter your choice exactly as per the options given:-")
print("")

df = pd.read_csv("data.csv")
#fig = pf.create_distplot( [df["Avg Rating"].tolist() ], ["Average Rating"], show_hist = False)
#fig.show()


samsung_df = df.loc[df['Mobile'] == 'Samsung']
apple_df = df.loc[df['Mobile'] == 'Apple']
moto_df = df.loc[df['Mobile'] == 'Motorola']
nokia_df = df.loc[df['Mobile'] == 'Nokia']
hu_df = df.loc[df['Mobile'] == 'HUAWEI']
asus_df = df.loc[df['Mobile'] == 'ASUS']
gog_df = df.loc[df['Mobile'] == 'Google']
one_df = df.loc[df['Mobile'] == 'OnePlus']
sony_df = df.loc[df['Mobile'] == 'Sony']
xi_df = df.loc[df['Mobile'] == 'Xiaomi']

if(mob == "Every Rating"):
    
    mean = df.groupby(["Mobile", "Avg Rating"], as_index= False).mean()

    fig = px.scatter(mean, x = "Mobile" , y = "Avg Rating", size = 'Avg Rating', color = 'Avg Rating')
    fig.show()

if(mob == "Samsung"):
    
    fig = pf.create_distplot( [samsung_df["Avg Rating"].tolist() ], ["Average Rating for Samsung Phones"], show_hist = False)
    fig.show()


if(mob == "Apple"):
    
    fig = pf.create_distplot( [apple_df["Avg Rating"].tolist() ], ["Average Rating for Apple Phones"], show_hist = False)
    fig.show()


if(mob == "Motorola"):
    
    fig = pf.create_distplot( [moto_df["Avg Rating"].tolist() ], ["Average Rating for Moto Phones"], show_hist = False)
    fig.show()


if(mob == "Nokia"):
    
    fig = pf.create_distplot( [nokia_df["Avg Rating"].tolist() ], ["Average Rating for Nokia Phones"], show_hist = False)
    fig.show()

if(mob == "HUAWEI"):
    
    fig = pf.create_distplot( [hu_df["Avg Rating"].tolist() ], ["Average Rating for HUAWEI phones"], show_hist = False)
    fig.show()

if(mob == "ASUS"):
    
    fig = pf.create_distplot( [asus_df["Avg Rating"].tolist() ], ["Average Rating for ASUS phones"], show_hist = False)
    fig.show()

if(mob == "Google"):
    
    fig = pf.create_distplot( [gog_df["Avg Rating"].tolist() ], ["Average Rating for Google phones"], show_hist = False)
    fig.show()

if(mob == "OnePlus"):
    
    fig = pf.create_distplot( [one_df["Avg Rating"].tolist() ], ["Average Rating for OnePlus phones"], show_hist = False)
    fig.show()

if(mob == "Sony"):
    
    fig = pf.create_distplot( [sony_df["Avg Rating"].tolist() ], ["Average Rating for Sony phones"], show_hist = False)
    fig.show()

if(mob == "Xiaomi"):
    
    fig = pf.create_distplot( [xi_df["Avg Rating"].tolist() ], ["Average Rating for Xiaomi phones"], show_hist = False)
    fig.show()

print("")
print("Thanks for using the Amazonian :)")
print("")