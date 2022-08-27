from matplotlib import pyplot as plt 

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8 so we'll add 0.1 to the left coordinates
#so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
#print(xs)
#plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# of academy awards")
plt.title("My favorite movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
#plt.bar(movies, num_oscars)
plt.show()