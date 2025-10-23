class Breed:
    def __init__(self, Color, Breed):
        self.Color = Color 
        self.Breed = Breed

    
Gershep = Breed('Brown', 'German Shepard')
Goldeen = Breed('Yellow', 'Golden Retriever')
print("Goldeen's Breed is", Goldeen.Breed,"and her color is", Goldeen.Color)
print("Gershep's Breed is", Gershep.Breed,"and her color is", Gershep.Color)