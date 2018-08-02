import RFID

def main():

    while(1):
        id,data = RFID.detectRFID()
        print(id)

main()
