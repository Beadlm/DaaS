

class Hero():
    def __init__(self, hero_bdd):
        self.pv = hero_bdd.pv
        self.pv_max = hero_bdd.pv_max

        self.agilite = hero_bdd.agilite
        self.force = hero_bdd.force
        self.intelligence = hero_bdd.intelligence

    def calculer_degats(self) :
        return self.force

    def subir_degats(self,atk_monstre) :
        return atk_monstre

class Guerrier(Hero):
    def calculer_degats(self) :
        return 2 + self.force * 2

    def subir_degats(self,atk_monstre) :
        return atk_monstre -1 if atk_monstre -1 >= 1 else 1
    
class Mage(Hero):
    def calculer_degats(self) :
        return 1 + self.intelligence * 3

class Voleur(Hero):
    count = 0
    def __init__(self, hero_bdd):
        super().__init__()
        
    def calculer_degats(self) :
        if self.count == 2 :
            self.count = 0 
            print("CRITTTTT")
            return (2 + self.force * 2) * 2
        else : 
            self.count += 1
            return 2 + self.force * 2 
        
