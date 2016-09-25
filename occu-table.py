#Angela Yu
#work3

from flask import Flask, render_template
import random
app=Flask(__name__)

#------------------------------------
def importation(filename):
    instream = open(filename, 'r') 
    content = instream.readlines() 
    instream.close()
    return content

data=importation("occupations.csv")
dict = {}

def split(L):
    del L[0]
    del L[len(L)-1]
    for row in L:
        row=row.strip('\n').rsplit(',',1)
        dict[row[0]]=(float)(row[1])

split(data)

def randomOcc(d):
    rand = random.uniform(0,100)
    for key in d.keys():
        if(rand<d[key]):
            return key
        else:
            rand -= d[key]
    return rand
occ=randomOcc(dict)
#--------------------------------------------
@app.route("/occupations")
def info():
    return render_template('model_tmplt.html', foo="Occupations Available", heading="Jobs & their availibity", collection=dict, selected=occ)

if __name__ == "__main__":
    app.debug = True 
    app.run()
