import myuartwigand
import machine
import time
import sys
try:
    myuartwigand.main()
    #import ledtest
except KeyboardInterrupt:
     print('keyboard interupt')
     sys.exit()

except:
   time.sleep(10) 
   machine.reset() 
