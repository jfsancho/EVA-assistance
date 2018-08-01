import RPi.GPIO as GPIO
import ./libs/SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def detectRFID():
    try:
        id, text = reader.read()
        return (id, text)
    except Exception as e:
        print( 'Error occurred : ' + str(e))
    finally:
        GPIO.cleanup()
