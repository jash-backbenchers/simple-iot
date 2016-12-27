from flask import Flask
import RPi.GPIO as GPIO      
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

app=Flask(__name__)

@app.route('/ledon',methods=['POST'])
def ledon():
    GPIO.output(11,True)
    return "led on"

@app.route('/ledoff',methods=['POST'])
def ledoff():
   GPIO.output(11,False)
   return "led off"
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
