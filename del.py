import os
print(os.getcwd())
from PIL import Image 

  

def main(): 

    try: 

        #Relative Path 

        imge = Image.open("img.jpg")  
        print(imge.mode)
        print()

          

        #splitting the image 

        print (imge.split() )

    except IOError: 

        pass

  

if __name__ == "__main__": 

    main() 