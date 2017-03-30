#################################################################
##                  SMART TOLLBOOTH PROJECT                    ##
#################################################################

from RFID import Rfid_Th
import servo

#Close the barrier when start
servo.closeBarrier()
Rfid_Th()
