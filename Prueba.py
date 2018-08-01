#!/usr/bin/env python
import json
import watson_developer_cloud

import RPi.GPIO as GPIO
import SimpleMFRC522


##print "Acerque la tarjeta: "                  ## para leer la id de la tarjeta
##reader = SimpleMFRC522.SimpleMFRC522()
##
##try:
##        id, ID = reader.read()
##        print(id)                             ## id no modificable
##        print(ID)                             ## informacion almacenada cuando se graba 
##finally:
##        GPIO.cleanup()





assistant = watson_developer_cloud.AssistantV1(
    username='8e547e5c-55f6-4db6-832c-30f70f6623b4',                            ## Autentificacion 
    password='kfvnfs1VjUZY',
    version='2018-07-10'
)





while True:
    
    message = raw_input("Input: ")                                              ## Mensaje que se le manda al assistant
    response = assistant.message(
        workspace_id = '23a5f117-8508-4010-867c-e7f5efc7b9b5',
        input={
            'text': message
        }
    )

    
    
    response_decoded = json.loads(json.dumps(response))                         ## Decodificacion del JSON, luego se trabaja como un array

##    print(json.dumps(response, indent=2))                                     ## Para ver el json completo
    
    text = response_decoded["output"]["text"][0]
    node = response_decoded["output"]["nodes_visited"][0]
    print ''
    if node != "En otras cosas":                                                ## Para que no exista error, cuando se accede al nodo En otras cosas que no tienen intenciones y entidades                                                     
            intents  = response_decoded["intents"][0]["intent"]
            entities = response_decoded["entities"]
            print "intent: ", intents
            print "entity: ", entities
    
    print "text: ", text
    print "node: ", node
    print ''

    
