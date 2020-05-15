
from geopy.distance import geodesic
import os
from gps import *
from time import *
import time
import threading
import math
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

os.system('flite -t "Select Location. One is admissions. Two is the science building"')
input1 = input()
#print 'input 1' , input1
#time.sleep(10)
  
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
    

      os.system('clear')
      def angleFromCoordinate(lat1, long1, lat2, long2):
          math.radians(lat1)
          math.radians(lat2)
          math.radians(long1)
          math.radians(long2)
          dLon = (long2 - long1)
          print 'hello'

          y = math.sin(dLon) * math.cos(lat2)
          x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

          brng = math.atan2(y, x)

          brng = math.degrees(brng)
          brng = (brng + 360) % 360
          brng = 360 - brng  # count degrees clockwise - remove to make counter-clockwise

          return brng
     
      P1 = [gpsd.fix.latitude,gpsd.fix.longitude]
      if input1 == 1:
          P2 = [38.32024131, -85.60533464]
      if input1 == 2:
          P2 = [35,35]

      #P2 = [38.32024131, -85.60533464]
      print 'P1 ', P1
      print 'P2 ' , P2
      lat1 = math.radians(P1[0])
      lat2 = math.radians(P2[0])

      diffLong = math.radians(P1[1] - P2[1])

      x = math.sin(diffLong) * math.cos(lat2)
      y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
                                             * math.cos(lat2) * math.cos(diffLong))

      initial_bearing = math.atan2(x, y)

     
      initial_bearing = math.degrees(initial_bearing)
      compass_bearing = (initial_bearing + 360) % 360
      print 'gpsd fix ' , gpsd.fix.track

      print 'compassbearing' , compass_bearing
      print 'initial bearing', initial_bearing 

      ibpos = initial_bearing * -1
      print 'ibpos ', ibpos
      HD = (ibpos - gpsd.fix.track)
      a = angleFromCoordinate(P1[0], P1[1], P2[0], P2[1])
      
      print 'TRUE BEARING PLEASE' , a
      print 'HD' , HD
      print '______________________'
      if gpsd.fix.track == 0:
          os.system('flite -t "Zero heading"')
      elif -22.5 <= HD <= 22.5:
          #os.system('flite -t "Negative 22.5 and 22.5"')
          os.system('flite -t "Strait"')
          print 'Between -22.5 and 22.5'

      elif 22.5 <= HD <= 67.5:                            
          #os.system('flite -t "22.5 and 67.5"')
          os.system('flite -t "slight left"')
          print 'between 22.5 and 67.5'                         
      elif 67.5 <= HD <= 112.5:
          #os.system('flite -t "67.5 and 112.5"')
          os.system('flite -t "full right"')
          print   'between 67.5 and 112.5'
      elif 112.5 <= HD <= 157.5:
          #os.system('flite -t "112.5 and 157.5"')
          os.system('flite -t "Big Right"')
          print   'between 112.5 and 157.5'
      elif 157.5 <= HD <= 202.5:
          #os.system('flite -t "157 and 202"')
          os.system('flite -t "Turn Around"')
          print        'between 157.5 and 202.5'
      elif 202.5 <= HD <= 247.5:
          #os.system('flite -t "202.5 and 247.5"')
          os.system('flite -t "Big left"')
          print 'between 202.5 and 247.5'
                           
      elif 247.5 <= HD <= 262.5:
          #os.system('flite -t "247.5 and 262.5"')
          os.system('flite -t "Full left"')
          print 'between 247.5 and 262.5'
      elif 262.5 <= HD <= 337.5:
          #os.system('flite -t "262.5 and 337.5"')
          os.system('flite -t "Light Left"')
          print     'between 262.5 and 337.5 Slight Right'
      elif 337.5 <= HD <= 360:
          #os.system('flite -t "337.5 and 360"')
          os.system('flite -t "Forward"')
          print    'between 337.5 and 360. Forward'
      elif -67.5 <= HD <= -22.5:
          os.system('flite -t "slight left"')
      elif -112.5 <= HD <= -67.5:
          os.system('flite -t "full right"')
      elif -157.5 <= HD <= -112.5:
          os.system('flite -t "Big Right"')
      elif -202.5 <= HD <= -157.5:
          os.system('flite -t "Big left"')
      elif -247.5 <= -202.5:
          os.system('flite -t "Big left"')
      elif -262.5 <= HD <= -247.5:
          os.system('flite -t "Turn Around"')
      elif -337.5 <= HD <= -262.5:
          os.system('flite -t "Light Left"')
      elif -360 <= HD <= -337.5:
          os.system('flite -t "Forward"')
                                  
      else:                                               
          print                                           
          'HD Error'
      print '_____________________________'

      d = geodesic(P1,P2).ft
      os.system('flite -t "you are "')
      print d
      os.system('flite -t ' + str(int(d)) + '"feet from your location"')
      

      time.sleep(5) #set to whatever
      
     
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
