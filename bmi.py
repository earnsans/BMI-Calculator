from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    height=input("Enter your height in cm",type=FLOAT)
    weight=input("Enter your weight in Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    bmi_output={ 'Severely underweight : Try some ghee ?' : 16, 'Underweight' : 18.5,
                  'Normal : Woah! Fit as a fiddle!' : 25.0, 'Overweight : time to skip the Sugars yet ?' : 30.0,
                  'Obese : do some weights !?' : 35.0, 'Severely Obese : how about weights and salads ?' : float('inf')}
    
    for out, val in bmi_output.items() :
         if(bmi<= val):
                
                put_text('Your BMI is %.1f and you are %s'%(bmi,out))
                break
if __name__=='__main__':
    bmicalculator()            
