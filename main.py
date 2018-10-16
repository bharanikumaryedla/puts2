from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'

@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1+value2
    return '%d \n' % result

@app.route('/sub')
def substraction():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1-value2
    return '%d \n' % result

@app.route('/mul')
def multiplication():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=value1*value2
    return '%d \n' % result

@app.route('/div')
def division():
    value1=request.args.get('A',default = 0, type = int)
    value2=request.args.get('B',default = 0, type = int)
    result=float(value1/value2)
    return '%.2f \n' % result
@app.route('/addrational')
def rational_addition():
    value1=request.args.get('A',default=0,type=str)
    numb1,denom1=str(value1).split('/')
    value2=request.args.get('B',default=0,type=str)
    numb2,denom2=str(value2).split('/')
    result=str(Fraction(int(numb1),int(denom1))+Fraction(int(numb2),int(denom2)))
    return result
@app.route('/subrational')
def rational_substraction():
    value1=request.args.get('A',default=0,type=str)
    numb1,denom1=str(value1).split('/')
    value2=request.args.get('B',default=0,type=str)
    numb2,denom2=str(value2).split('/')
    result=str(Fraction(int(numb1),int(denom1))-Fraction(int(numb2),int(denom2)))
    return result

if __name__ == "__main__":
    app.run()
