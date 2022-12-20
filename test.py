from pathlib import Path
def main():

    a = 'luigi.puz'
    
    with open('luigi.puz', 'r') as puz:
        li = []  
        for lines in puz:
            print(lines)
            #lines = lines.replace('\n', '')
            #li.append(lines)

    with open('meow.puz', 'w') as p:
        p.write('name: meow\n')
        p.write('number: 4\n')
        p.write('size: 100\n')
        p.write('thumbnail: Images/meow/meow_thumbnail.gif\n')
        p.write('1: Images/meow/4.gif\n')
        p.write('1: Images/meow/3.gif\n')
        p.write('1: Images/meow/2.gif\n')
        p.write('1: Images/meow/blank.gif\n')

    
    with open('meow.puz', 'r') as puz:
        li = []  
        for lines in puz:
            print(lines)
            #lines = lines.replace('\n', '')
            #li.append(lines)
            

   

if __name__ == "__main__":
    main()
