file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()    


with open('youtube.txt', 'W') as file:
    file.write("chai aur python")   