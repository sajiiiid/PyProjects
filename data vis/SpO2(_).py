import matplotlib.pyplot as plt

heures = [1, 2, 3, 4, 5]
tas = [i for i in range(120, 99, -5)]
tad = [i for i in range(80, 59, -5)]

fig, ax = plt.subplots()
ax.plot(tas, heures, label='tas')
ax.plot(tad, heures, label='tad')
ax.legend()
ax.set_ylabel('Heures')
ax.set_xlabel('Systolique')

plt.savefig(".gpeg")  # Save instead of show
print("Plot saved as 'blood_pressure_plot.png'")