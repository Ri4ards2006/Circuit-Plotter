import matplotlib.pyplot as plt

def plot_voltage_over_time(spannungen, zeiten):
    plt.plot(zeiten, spannungen, marker='o')
    plt.title("Spannung über Zeit")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Spannung (V)")
    plt.grid(True)
    plt.show()  # Ohne diesen Befehl wird der Plot nicht angezeigt!



#
#import matplotlib.pyplot as plt

#  was bedeutet as plt ?

#def plot_voltage_over_time(times, voltages):

 #   plt.title("Spannung über Zeit")
  #  plt.xlabel("Zeit in (s) ")
   # plt.ylabel("Spannung in (V)")
    #plt.grid(True)
    #plt.show()

