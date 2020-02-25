from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index(): 
        if request.method=='POST':
            form=request.form
            Loan_amount=float(form['loan_amount'])
            Payments_per_year=float(form['payment_per_year'])
            Number_of_year=float(form['number_of_year'])
            Annual_rate=float(form['annual_rate'])
            Payment_period=float(form['payment_period'])

            n=Payments_per_year*Number_of_year
            i=Annual_rate/Payment_period
            D=((1+i)**n-1)/(i*( 1+ i)**n)
            P=Loan_amount/D

            print('Your loan payment is ${0:,.2f}'.format(P))
            Loan_estimate='Your loan payment is ${0:,.2f}'.format(P)
            return render_template('index.html',pageTitle='Calculator main page',display=Loan_estimate)
    
        return render_template('index.html',pageTitle='Calculator main page')


if __name__ == '__main__':   
     app.run(debug=True, host='0.0.0.0')