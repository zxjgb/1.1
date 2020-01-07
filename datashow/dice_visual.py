import pygal
from die import Die

die1=Die()
die2=Die()
results=[]
for x in range(1000):
	result=die1.roll()+die2.roll()
	results.append(result)

frequencies=[]
for x  in range(2,13):
	frequency=results.count(x)
	frequencies.append(frequency)
	
hist=pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times." 
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] 
hist.x_title = "Result" 
hist.y_title = "Frequency of Result" 
hist.add('D6 + D6', frequencies) 
hist.render_to_file(r"C:\Users\ZXJ\Desktop\dice_visual.svg")