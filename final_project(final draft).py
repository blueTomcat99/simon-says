from engi1020.arduino.api import *
from time import sleep
from random import *
i = 3
score = 0
while analog_read (0) == 0:
    colour = randint (0, 5)
    if colour == 0:
       rgb_lcd_colour(255,0,0)
       x = input('colour:')
       if x == 'red':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break     
       else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break
    if colour == 1:
        rgb_lcd_colour(0,0,255)
        x = input('colour:' )
        if x == 'blue':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break
        else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break               
    if colour == 2:
        rgb_lcd_colour(0,255,0)
        x = input('colour:' )
        if x == 'green':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break
        else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break    
    if colour == 3:
        rgb_lcd_colour(153,76,0)
        x = input('colour:' )
        if x == 'orange':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break
        else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break    
    if colour == 4:
        rgb_lcd_colour(128,0,128)
        x = input('colour:' )
        if x == 'purple':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break
        else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break    
    if colour == 5: 
        rgb_lcd_colour(150,150,0)
        x = input('colour:' )
        if x == 'yellow':
            sleep (i)
            if digital_read(6) == True:
                buzzer_frequency(5, 10)
                sleep(1)
                buzzer_stop(5)
                score += 1
                i -= 0.25
            if digital_read(6) == False:
                buzzer_frequency(5, 200)
                print ('fail score:', score)
                sleep(1)
                buzzer_stop(5)
                break
        else:
           buzzer_frequency(5, 200)
           print ('fail score:', score)
           sleep(1)
           buzzer_stop(5)
           break    
    if x == '':
        print ('fail score:', score)
        break
    if i < 0.5:
        i += 0.25