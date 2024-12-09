def dessiner_cercle():
    try:
        rayon = float(input("entrez le rayon du cercle:"))
        if rayon <= 0:
            print("le rayon doit etre un nombre positive")
            return

        theta = np.inspace(0.2*np.pi,100)
        x = rayon*np.cos(theta)
        y = rayon*np.sin(theta)
        plt.plot(x,y,label = f"cercle de rayon{rayon}")
        plt.gca().set_aspect("equal",abjustable = "box")
        plt.axhline(0,color ='black',linewidth = 0.5)
        plt.axvline(0,color = "black",linewidth = 0.5)
        plt.grid(color = "gray",linestyle="__", linewidth=0.5)

        plt.legend()
        plt.title("Representation du cercle")
        plt.show()
    except ValueError:
            print("veuillez entrez un nombre")
    dessiner_cercle()
