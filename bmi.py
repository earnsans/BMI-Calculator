from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    height=input("Enter your height in cm",type=FLOAT)
    weight=input("Enter your weight in Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    bmi_output={ 'Severely underweight' : 16, 'Underweight' : 18.5,
                  'Normal' : 25, 'Overweight' : 30,
                  'Moderately obese' : 35, 'Severely obese' : float('inf')}
    
    for out, val in bmi_output.items() :
         if(bmi<= val):
                
                put_text('Your BMI is :%.1f and the person is :%s'%(bmi,out))
                break
if __name__=='__main__':
    bmicalculator()            
