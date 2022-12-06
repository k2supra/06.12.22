class Music_instrument:
    name = ''
    category = ''
    price = 0
    size = ''

    def __init__(self):
        print(f"Created objects of MI:")
        self.name = "Triangle"
        self.category = 'hit'
        self.price = 9999999
        self.size = '236m'


    def ShowOn(self):
        print(f"Name: {self.name} \nCategory: {self.category} \nPrice: {self.price}$ \nSize: {self.size}")
    def __del__(self):
        print("Deleted objects of MI")

if __name__ == '__main__':
    music_instrument = Music_instrument()
    music_instrument.ShowOn()
    del music_instrument