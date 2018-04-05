## 2 Programmation plus avancée

import numpy as np
import matplotlib.pyplot as plt

# Calcul de l'angle
def Latiso2Lat(lat,eps):
    # IN
    # - lat : latitude isométrique
    # OUT
    # phi : angle

    phi0=0
    phi1=2*np.arctan(np.exp(lat))-np.pi/2
    while abs(phi0-phi1)<esp:
        phi0=phi1
        phi1=2*np.arctan(((1+e*np.sin(phi1)/(1-e*np.sin(phi1)))**e/2*np.exp(lat)))-np.pi/2
    return phi1
    
    
f=1/298.257222101
e=np.sqrt(2*f-f*f)
esp=0.001/6400000
n=6378137.0



# Définition de la classe reseau
class reseau:
    # Constructeur de la classe
    def __init__(self,nomfic):
        mat                = np.genfromtxt(nomfic)
        self.taille_reseau = mat.shape[0]
        self.long_deg      = mat[:,1]
        self.lat_deg       = mat[:,0]
        self.latiso        = np.zeros([self.taille_reseau,1])
        
    # Méthode lat2latiso
    def lat2latiso(self):
        self.lat_deg=self.lat_deg*np.pi/180
        self.latiso=np.log(np.tan(np.pi/4+self.lat_deg/2))-e*np.log((1+e*np.sin(self.lat_deg))/(1-e*np.sin(self.lat_deg)))/2
        print(self.latiso)
        
    # Carte de Mercator
    def carte(self):
        plt.plot(n*self.long_deg*np.pi/180,n*self.latiso*np.pi/180)
        plt.show()


# Programme principal
if __name__ == "__main__":

    # Construction des attributs de l'objet reseau_carte
    reseau_carte=reseau("coast.txt")

    # Affichage des attributs de l'objet reseau_carte
    print('\nTaille du réseau : {0:d}\n'.format(reseau_carte.taille_reseau))
    print('Longitude du premier point(deg) : {0:.3f}\n'.format(reseau_carte.long_deg[0]))
    print('Latitude du premier point(deg) : {0:.3f}\n'.format(reseau_carte.lat_deg[0]))
    
    # Appel à la méthode lat2latiso de la classe reseau
    reseau_carte.lat2latiso()
    
    # Affichage de la carte de Mercator
    reseau_carte.carte()