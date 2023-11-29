
class Article:
    def __init__(self, num_serie, contite_stock, prix):
        self.__num_serie = num_serie
        self.__contite_stock = contite_stock
        self.__prix = prix


    def get_num_serie(self):
        return self.__num_serie

    def get_contite_stock(self):
        return self.__contite_stock
    
    def get_prix(self):
        return self.__prix

    def afficher(self):
        print(f"le numero:{self.get_num_serie()}\nle prix hors taxe:{self.get_prix()}\nla la quantité en stock:{self.get_contite_stock()}")

    def approvisionner(self, qte):
        self.__contite_stock += qte

    def achat(self, qte):
        if self.__contite_stock - qte >= 0:
            self.__contite_stock -= qte 
            print("merci :)")

        else:
            print(f"il reste just {self.get_contite_stock()} piece")


class Habit(Article):
    def __init__(self, num_serie, contite_stock, prix, taille, couleur):
        super().__init__(num_serie, contite_stock, prix)
        self.taille = taille
        self.couleur = couleur


    def afficher(self):
        super().afficher()
        print(f"la taille:{self.taille}\nla couleur:{self.couleur}")
import datetime
class Electromenager(Article):
    def __init__(self, num_serie, contite_stock, prix, pois, D_garanti_mois):
        super().__init__(num_serie, contite_stock, prix)
        self.__pois = pois
        self.__garanti = D_garanti_mois

    def get_pois(self):
        return self.__pois
    
    def get_garanti(self):
        return self.__garanti

    def dateFinGarantie(self):
        DateF = datetime.datetime.now() + datetime.timedelta(days= self.get_garanti() *30)
        return DateF

    def afficher(self):
        super().afficher()
        print(f"le pois:{self.get_pois()}\nla Date de fin de garanti:{self.dateFinGarantie()}")


ls_Habits = []
ls_Electro = []

class gestion:
    def __init__(self) -> None:
        pass


    def ajouter_Habit(self, num):
        try:
            prix = input("entrez le prix: ")
            taille = input("entrez la taille: ")
            couleur = input("entrez la couleur: ")
            con = int(input("entrez la quantite:"))
            H = Habit(num, con, prix, taille, couleur)
            ls_Habits.append(H)
        except ValueError:
            print("\n\nereur\n")
            print("entre un nombre entier")


    def ajouter_electromenager(self, num):
        try:
            prix = input("entrez le prix: ")
            poix = input("entrez le poix de l'article: ")
            gar = int(input("entrez le duree de garantie on mois: "))
            con = int(input("entrez la quantite:"))
            E = Electromenager(num, con, prix, poix, gar)
            ls_Electro.append(E)
        except ValueError:
            print("\n\nereur\n")
            print("entre un nombre entier")

    def chercher_H(self, num):
        for art in ls_Habits:
            if art.get_num_serie() == num:
                return art
        return
    
    def chercher_E(self, num):
        for art in ls_Electro:
            if art.get_num_serie() == num:
                return art
        return



    def afficher_H(self):
        for i in ls_Habits:
            i.afficher()

    def afficher_E(self):
        for i in ls_Electro:
            i.afficher()

    



mp = "1234"
G = gestion()
def main():
    while True:
        print("\n\n\n")
        print("#############")
        print("___main menu___")
        print("'1' pour entrez pour entrez comme vendeur")
        print("'2' pour entrez pour entrez comme client")
        print("'0' pour quiter ")
        print("#############")
        print("\n\n\n")


        choix = input("entrez: ")


        if choix == "1":
            print("'0' pour quiter")
            m = input("entrez le mote de pass: ")
            if m != 0:
                while m != mp:
                    if m == "0":
                        break
                    else:
                        print("foux")
                        print("'0' pour quiter")
                        m = input("entrez le mote de pass: ")
            else:
                break 
            if m == mp:
                while True:
                    print("\n\n\n")
                    print("#############")
                    print("___vendeur___")
                    print("'1' pour ajouter un article")
                    print("'2' pour afficher les article")
                    print("'3' pour ajouter la quantite d'un article")
                    print("'0' pour quiter")
                    print("#############")
                    print("\n\n\n")


                    choix = input("entrez: ")

                    if choix == "1":
                        while True:
                            print("\n\n\n")
                            print("#############")
                            print("___ajouter article___")
                            print("'1' pour ajouter un Habit")
                            print("'2' pour ajouter un Electromenager")
                            print("'0' pour quiter")
                            print("#############")
                            print("\n\n\n")


                            choix = input("entrez: ")

                            if choix == "1":
                                num = input("entrez un numero de serie: ")
                                if not G.chercher_H(num):
                                    G.ajouter_Habit(num)
                                else:
                                    print("l'article est deja dans la liste des article")

                            elif choix == "2":
                                num = input("entrez un numero de serie: ")
                                if not G.chercher_E(num):
                                    G.ajouter_electromenager(num)
                            elif choix == "0":
                                break
                            else: 
                                print("donner invalid")
                    elif choix == "2":
                        while True:
                            print("\n\n\n")
                            print("#############")
                            print("___afficher article___")
                            print("'1' pour afficher les Habits")
                            print("'2' pour afficher les electromenager")
                            print("'3' pour afficher tous")
                            print("'0' pour quiter")
                            print("#############")
                            print("\n\n\n")

                            choix = input("entrez: ")

                            if choix == "1":
                                G.afficher_H()
                            elif choix == "2":
                                G.afficher_E()
                            elif choix == "3":
                                G.afficher_H()
                                G.afficher_E()
                            elif choix == "0":
                                break
                            else: 
                                print("donner invalide")
                    elif choix == "3":
                                while True:
                                    print("\n\n\n")
                                    print("#############")
                                    print("___ajouter___")
                                    print("'1' Habits")
                                    print("'2' electromenager")
                                    print("'0' pour quiter")
                                    print("#############")
                                    print("\n\n\n")

                                    choix = input("entrez: ")

                                    if choix == "1":
                                        num = input("entrez le numero de serie d'un article: ")
                                        art = G.chercher_H(num)
                                        if art:
                                            try:
                                                qte = int(input("entrez la quantite: "))
                                                art.approvisionner(qte)
                                                print("merci")  
                                            except ValueError:
                                                print("\n\nereur\n")
                                                print("entre un nombre entier")
                                        else:
                                            print("le article n'existe pas")
                                    elif choix == "2":
                                        num = input("entrez le numero de serie d'un article: ")
                                        art = G.chercher_E(num)
                                        if art:
                                            try:
                                                qte = int(input("entrez la quantite: "))
                                                art.approvisionner(qte)
                                                print("merci")   
                                            except ValueError:
                                                print("\n\nereur\n")
                                                print("entrez un entier")
                                        else:
                                            print("le article n'existe pas")
                                    elif choix == "0":
                                            break
                                    else:
                                        print("donner invalide")
                                
                    elif choix == "0":
                        break
        elif choix == "2":
            while True:
                print("\n\n\n")
                print("#############")
                print("___client___")
                print("'1' pour afficher les Habits")
                print("'2' pour afficher les electromenager")
                print("'3' pour acheter les Habits")
                print("'4' pour acheter les Electromeneger")
                print("'0' pour quiter")
                print("#############")
                print("\n\n\n")

                choix = input("entrez: ")

                if choix == "1":
                    G.afficher_H()
                elif choix == "2":
                    G.afficher_E()
                elif choix == "3":
                    num = input("entrez le numero d'article: ")
                    art = G.chercher_H(num)
                    if art :
                        try:
                            qte = int(input("entrer la quantite que vous voulez achetez: "))
                            art.achat(qte)
                        except ValueError:
                            print("\n\nereur\n")
                            print("entrez un entier")
                    else: 
                        print("ce article n'existe pas")
                elif choix == "4":
                    num = input("entrez le numero de article: ")
                    art = G.chercher_E(num)
                    if art:
                        try:
                            qte = int(input("entrer la quantite que vous voulez achetez: "))
                            art.achat(qte)
                        except ValueError:
                            print("\n\nereur\n")
                            print("entrez un entier")
                    else:
                        print("ce article n'existe pas")
                elif choix == "0":
                    break

                else:
                    print("donner invalide")

        elif choix == "0":
            break

        else:
            print("donner anvalide")

if __name__ == "__main__":
    main()
