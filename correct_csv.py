import csv
import os
import glob
import string
import re

nn=0

for filepath in glob.iglob("**/*.csv*", recursive=True):
    #contentArray=[]
    rows= []
    n=0
    #print(filepath)
    fruit_wanted=[]
    fruit_wanted = ['class'] + ["'%s'" % f for f in str(fruit_wanted).split(',')]
    #outfile = csv.DictWriter(open(filepath, 'w'), fieldnames=fruit_wanted)
    fruit_wanted = set(fruit_wanted)

    filename=[]
    filename = ['filename'] + ["'%s'" % f for f in str(filename).split(',')]
    #outfile = csv.DictWriter(open(filepath, 'w'), fieldnames=fruit_wanted)
    filename = set(filename)

    
    with open(filepath,'r', newline='') as csvfile:
        contents=csvfile.read()
        newcontents=contents.replace("Filename","filename").replace("Width","width").replace("Height","height").replace("Roi.X1","xmin").replace("Roi.Y1","ymin").replace("Roi.X2","xmax").replace("Roi.Y2","ymax").replace("ClassId","class").replace("ppm","png")
        print(newcontents)
        obj=csv.DictReader(csvfile)
        for row in obj:
            #print(row['class'])
            row = {k: row[k] for k in row if k in fruit_wanted}
            #print(row['class'])
##    with open(filepath,'r', newline='') as csvfile:
##        contents=csvfile.read()
##        newcontents=re.sub(";", ",", contents)
##        #print(newcontents)
##        obj=csv.DictReader(csvfile)
##        for row in obj:
##            row={k: row[k] for k in row if k in filename}
##            print(row)
##            outfile.writerow(row)
##            s = str(row)
##            #print(re.sub(";", ",", s))
##            rows.insert(n,row)
##            #print(filepath)
##            #print("string= ",s)




## UNCOMMENT HERE TO FIX FIELDNAMES

##    with open(filepath,'w', newline='') as csvfile:
##        csvfile.write(newcontents)
##        #fieldnames={'Filename','Width','Height','Roi.X1','Roi.Y1','Roi.X2','Roi.Y2','ClassId'}
##        #obj2=csv.DictWriter(csvfile,fieldnames)
##        #print(str(rows))
##        for row in rows:
##            s = str(row)
##            s=re.sub(";", ",", s)
##            row=s
##            print(row)
##            obj2.writerow(row)


##  UNCOMMENT HERE TO COLLATE
    with open(filepath,'r', newline='') as infile, open('train_labels.csv', 'a',newline='') as outfile:
        fieldnames = ['filename', 'width', 'height', 'class', 'xmin','ymin','xmax','ymax']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames,skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
        if nn ==0:
            writer.writeheader()
        nn+=1
                
        reader =csv.DictReader(infile)
        next(reader, None)
        for row in reader:
            if '02513' not in str(row) and '02473' not in str(row):
                row['class']='sign_unreadable'
                #print(str(row))
                writer.writerow(row)
            else:
                row['class']='sign_readable'
                print('found stop sign')
                writer.writerow(row)

            
            #print(row['class'])
            #row = {k: row[k] for k in row if k in fruit_wanted}
            #print(row['class'])




            


            #n+=1
##    with open(filepath,'w', newline='') as csvfile:
##        csvfile.write(newcontents)
##        fieldnames={'Filename','Width','Height','Roi.X1','Roi.Y1','Roi.X2','Roi.Y2','ClassId'}
##        obj2=csv.DictWriter(csvfile,fieldnames)
##        print(str(rows))
##        for row in rows:
##            s = str(row)
##            s=re.sub(";", ",", s)
##            row=s
##            print(row)
##            obj2.writerow(row)
##            #print(str(rows))
##            #print("Rows= ",rows)
            
        
