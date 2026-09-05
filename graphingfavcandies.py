import matplotlib.pyplot as plt

candy_options=["Kitkat", "Reese's","Snickers","Hershey's Cookies 'n' Cream","M&Ms"] 
votes=[5,2,1,1,1]
colors=["#EC2227","#FF5200","#58352F", "#003399", "#187C36"]

fig, ax=plt.subplots(figsize=(8,5))
bars=ax.bar(candy_options,votes,color=colors,edgecolor="black", width=0.6)

for bar in bars:
  height=bar.get_height()
  ax.annotate(
      f"{height}",
      x=(bar.get_x()+bar.get_width()/2,height),
