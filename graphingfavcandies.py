import matplotlib.pyplot as plt
from matplotlib.widgets import Button

plt.style.use("seaborn-v0_8-whitegrid")

candy_options=["Kitkat", "Reese's","Snickers","Hershey's","M&M's"] 
votes=[5,2,1,1,1]
colors=["#EC2227","#FF5200","#58352F", "#7ACFF3", "#187C36"]

def on_button_click(event): 
    ax.cla()
    print("Oh yeah! You're changing the graph!")
    ax.set_title("Yeah! New, cooler, different food graph!LEAST Favorite Cnadies now!")
    candy_options=["Licorice", "Lego Candy","Sour Skittles","Milk duds", " Smarties "] 
    votes=[3,1,2,1,2]
    colors=["#A53E4B","#ea859a","#7DC900", "#F9C822", "#CDB7F0"]
    bars=ax.bar(candy_options,votes,color=colors,edgecolor="black", width=0.6)
    fig.canvas.draw()
    




fig, ax=plt.subplots(figsize=(8,5))
bars=ax.bar(candy_options,votes,color=colors,edgecolor="black", width=0.6)

button_ax = plt.axes([0.4, 0.01, 0.4, 0.06])

my_button = Button( button_ax, ' Click for the next, even cooler graph!', color = 'darkcyan', hovercolor='lightsteelblue')

my_button.on_clicked(on_button_click)


def on_loremipsum_click(event): 
    ax.cla()
    print("Oh yeah! You're changing the graph!")
    ax.set_title("Yeah! Old, cooler, different food graph!FAVORITE candies now!")
    candy_options=["Kitkat", "Reese's","Snickers","Hershey's", "M&M'S"] 
    votes=[5,2,1,1,1]
    colors=["#EC2227","#FF5200","#58352F", "#7ACFF3", "#187C36"]
    bars=ax.bar(candy_options,votes,color=colors,edgecolor="black", width=0.6)
    fig.canvas.draw()


button_ax = plt.axes([0, 0.9, 0.2, 0.06])

your_button = Button( button_ax, ' Click for the old, even cooler graph!', color = 'darkorange', hovercolor='moccasin')

your_button.on_clicked(on_loremipsum_click)

mytuple = ("foo","bar")



button_ax = plt.axes([4, 0.3, 0.4, 0.06])

button_button = Button( button_ax, ' Click for the newer, even cooler graph!', color = 'darkred', hovercolor='powderblue')

button_button.on_clicked(on_loremipsum_click)


def on_loremipsum_click(event): 
   ax.cla()
    print("Oh yeah! You're changing the graph!")
    ax.set_title("Yeah! Extra New, cooler, different food graph!")
    candy_options=["Red Doritos", "Blue Doritos","Other"] 
    votes=[6,4,10,]
    colors=["#BA0C2F","#004B87","#4A154B",]
    bars=ax.bar(candy_options,votes,color=colors,edgecolor="black", width=0.6)
    fig.canvas.draw()
    




print(mytuple[0])

plt.show()
