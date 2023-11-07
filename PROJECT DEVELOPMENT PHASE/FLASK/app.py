from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   p1 = request.form["age"]

   q1 = request.form["a"]
   if (q1=="mal"):
       s=0
   elif(q1=="fem"):
       s=1

   r1 = request.form["b"]
   if (r1=="yes"):
       s=0
   elif(r1=="no"):
       s=1

   c1 = request.form["c"]
   if (c1=="yes"):
       s=0
   elif(c1=="no"):
       s=1

   d1 = request.form["d"]
   if (d1=="yes"):
       s=0
   elif(d1=="no"):
       s=1

   e1 = request.form["e"]
   if (e1=="of"):
       s=0
   elif(e1=="rar"):
       s=1
   elif(e1=="nev"):
       s=2
   elif(e1=="som"):
       s=3
   else:
       s=4
       
   f1 = request.form["f"]
   if (f1=="yes"):
       s=0
   elif(f1=="no"):
       s=1

   g1 = request.form["g"]
   if (g1=="yes"):
       s=0
   elif(g1=="no"):
       s=1
    
   h1 = request.form["h"]
   if (h1=="yes"):
       s=0
   elif(h1=="no"):
       s=1
   else:
       s=2

   i1 = request.form["h"]
   if (h1=="yes"):
       s=0
   elif(h1=="no"):
       s=1
   else:
       s=2

   y1 = request.form["y"]
   if (y1=="yes"):
       s=0
   elif(y1=="no"):
       s=1
   else:
       s=2

   z1 = request.form["z"]
   if (z1=="yes"):
       s=0
   elif(z1=="no"):
       s=1
   else:
       s=2

   j1 = request.form["j"]
   if (j1=="yes"):
       s=0
   elif(j1=="no"):
       s=1
   else:
       s=2

   k1 = request.form["k"]
   if (k1=="yes"):
       s=0
   elif(k1=="sd"):
       s=1
   elif(k1=="dk"):
       s=2
   elif(k1=="ve"):
       s=3
   else:
       s=4
    
   l1 = request.form["l"]
   if (l1=="yes"):
       s=0
   elif(l1=="no"):
       s=1
   else:
       s=2

   m1 = request.form["m"]
   if (m1=="yes"):
       s=0
   elif(m1=="no"):
       s=1
   else:
       s=2
    
   n1 = request.form["n"]
   if (n1=="yes"):
       s=0
   elif(n1=="no"):
       s=1
   else:
       s=2

   o1 = request.form["o"]
   if (o1=="yes"):
       s=0
   elif(o1=="no"):
       s=1
   else:
       s=2

   u1 = request.form["p"]
   if (p1=="yes"):
       s=0
   elif(p1=="no"):
       s=1
   else:
       s=2

   v1 = request.form["q"]
   if (q1=="yes"):
       s=0
   elif(q1=="no"):
       s=1
   else:
       s=2

   w1 = request.form["r"]
   if (r1=="yes"):
       s=0
   elif(r1=="no"):
       s=1
   else:
       s=2


   t =  [[float(p1),float(q1),float(r1),float(c1),float(d1),float(e1),float(f1),float(g1),float(h1),float(i1),float(j1),float(y1),float(z1),float(l1),float(m1),float(n1),float(o1),float(u1),float(v1),float(w1)]] 
   output =model.predict(t)
   print(output)

   return render_template("index.html", y = "The predicted profit is  "+str(np.output[0]))

if __name__ == '__main__' :
    app.run(debug=True)
          






