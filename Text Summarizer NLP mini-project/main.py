import fileimage as pp
import documentsummarizer as summ
from fileinput import filename
from flask import *  
app = Flask(__name__)  


@app.route('/')  
def main():  
    return render_template("index.html")  

image_path = r'C:\Users\Admin\Downloads\ximg.png';

@app.route('/success', methods = ['POST'])  
def success():  
    print("HI1")
    if request.method == 'POST':  
        f = request.files['file']
        percentage = request.form['percent']
        f.save(f.filename)  
        image_path = f.filename
        textimg =  pp.displaytext(image_path)
        percentage = float(percentage)
        # print("--------------****************------\n",textimg,"\n")
        finalsum = summ.summary(1,textimg,percentage)
        # print("*****----*********************----***\n",finalsum,"\n")
        # return render_template('index.html',)
        return render_template("index.html",n=finalsum,p1=percentage)  

@app.route('/successtext', methods = ['POST'])
def successtext():  
    print("HI2")
    if request.method == 'POST':  
        textip = request.form['textinput']
        percentage = request.form['percent']
        print("textinput")
        print(percentage)
        percentage = float(percentage)
        finalsum = summ.summary(2,textip,percentage)
        # print("*****----*********************----***\n",finalsum,"\n")
        # return render_template('index.html',)
        print(finalsum);
        return render_template("index.html",ntext=finalsum,ntextip=textip,p=percentage)  


@app.route('/successDoc', methods = ['POST'])  
def successDoc(): 
    print("HI3") 
    if request.method == 'POST':  
        f = request.files['txtfile']
        percentage = request.form['percent']
        percentage = float(percentage)
        f.save(f.filename)  
        txtfile_path = f.filename
        finalsum = summ.summary(3,txtfile_path,percentage)
        print(finalsum);
        return render_template("index.html",ntxtfile=finalsum,p2=percentage)  



if __name__ == '__main__':  
    app.run(debug=True)