import os, sys



class Track:
    def __init__(self, name,
                 distance, terrain):
        self.name=name
        self.distance=distance
        self.terrain=terrain

class Racer:
    def __init__(self, name,
                 speedSTAT, staminaSTAT, gutsSTAT, footingSTAT,
                 growth_speed, growth_stamina, growth_guts, growth_footing, Player=False):
        self.name = name

        # Fix stats
        self.MaxStamina = 3
        self.Player=Player
        
        # Core stats
        self.speedSTAT = speedSTAT
        self.staminaSTAT = staminaSTAT
        self.gutsSTAT = gutsSTAT
        self.footingSTAT = footingSTAT

        # Growth rates
        self.growth_speed = growth_speed
        self.growth_stamina = growth_stamina
        self.growth_guts = growth_guts
        self.growth_footing = growth_footing

        # Other race-related states
        self.stamina_count = 3
        self.injured = False
        self.mood = 100  # placeholder

    def reset_for_race(self):
        self.stamina_count = self.MaxStamina
        self.injured = False
    
    def StaminaChange(self,increase:bool):
        if increase:
            self.stamina_count = min(self.MaxStamina,self.stamina_count+1)
        else: 
            self.stamina_count = max(0,self.stamina_count-1)




def StoryMode():
    os.system('cls' if os.name == 'nt' else 'clear')


    Player = Racer("Player",1,1,1,1,.1,.1,.1,.1)
    print(Player)




    input("Not implemented yet")

def HallFame():
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Not implemented yet")

def AdventureMode():
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Not implemented yet")


MenuText="""
          Welcome to RACING GAME\n
    
(1) Story Mode.
(2) Adventure Mode.
(3) Hall of Fame.
(4) Exit.

>"""

ChoiceDic={
    "1":"StoryMode",
    "2":"AdventureMode",
    "3":"HallFame",
    "4":"Exit"
}

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(MenuText, end="")
        choice_input  = input()

        if choice_input  not in ChoiceDic:
            print("\n-Bad choice-")
            input("Press Enter to continue.")
        else:
            Choice = ChoiceDic[choice_input ]
            if Choice=="StoryMode":
                StoryMode()
            elif Choice=="AdventureMode":
                AdventureMode()    
            elif Choice=="HallFame":
                HallFame()
            elif Choice=="Exit":
                sys.exit()


if __name__ == "__main__":
    main()