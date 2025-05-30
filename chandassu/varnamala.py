class Varnamala:

    def __init__( self ):

        self.varnamala= [
                        'అ','ఆ','ఇ','ఈ','ఉ','ఊ','ఋ','ౠ','ఎ','ఏ','ఐ','ఒ','ఓ','ఔ', # add am, aha
                        'క','ఖ','గ', 'ఘ', 'ఙ',
                        'చ','ఛ','జ','ఝ', 'ఞ',
                        'ట','ఠ','డ', 'ఢ', 'ణ',
                        'త', 'థ', 'ద','ధ','న',
                        'ప','ఫ','బ','భ', 'మ',
                        'య', 'ర', 'ల','వ','శ','ష','స','హ', 'ళ', 'ఱ'
                    ]
        
        self.special_characters= []

        self.sankhya= [ "౦", "౧", "౨", "౩", "౪", "౫", "౬", "౭", "౮", "౯"]

        self.guninta_chihnam= ["఼","ఽ","ా","ి","ీ","ు","ూ","ృ","ౄ","ె","ే","ై","ొ","ో","ౌ","్","ౖ","౦","౧","ಂ","ಃ"]

    def varnamala_map( self, to_num= True ):

        if to_num == False:
            return {ord(i): i for i in self.varnamala}
        
        return {i: ord(i) for i in self.varnamala}