from flask import Flask,render_template,request,flash,redirect,url_for
import matplotlib.pyplot as plt


app = Flask(__name__)






@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


@app.route('/cadastro' , methods=['POST'])
def postvalue():
    #if request.method == 'POST':
    value = request.form['value']
    time = request.form['time']


    release(time,value)

    return render_template('index.html',value=value,time=time)
def release(y,x):
    y=int(y)
    x=float(x)
    list=[]
    for i in range(y):
        if i==0:
            list.append(x)
        else:
            x=x*1.1375
            list.append(x)


    plt.plot(list,range(y))

    plt.savefig('graph.png', format='png')
    return






if __name__ == '__main__':
    app.run(debug=True)



