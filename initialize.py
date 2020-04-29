from parent.models import Parent
from baby.models import Baby  
from event.models import Event
from django.contrib.auth.models import User

from django.utils.timezone import now

# Create super users
User.objects.create_superuser('jorge', 'jorge@gmail.com', 'jorge1357')
User.objects.create_superuser('adrian', 'adrian@gmail.com', 'adrian1357')

# create parents
jorgeparent = Parent()
jorgeparent.username = "jorge"
jorgeparent.firstname = "Jorge"      
jorgeparent.lastname = "Perez"   
jorgeparent.age = 30    
jorgeparent.save()      
      
adrianParent = Parent()
adrianParent.username = "adrian"
adrianParent.firstname = "Adrian" 
adrianParent.lastname = "Sanchez" 
adrianParent.age = 31
adrianParent.save()

# create babies
sara = Baby()
sara.firstname = "Sara"
sara.lastname = "Sanchez"      
sara.age = 2
sara.parent = adrianParent
sara.save()

lisa = Baby()
lisa.firstname = "Lisa"      
lisa.lastname = "Perez"      
lisa.age = 1 
lisa.parent = jorgeparent 
lisa.save()  


#Create Events
  
event1 = Event(type="POOP", datetime=now(), description = "1kg.",baby=lisa)
event1.save()    
  

event2 = Event(type="FEED", datetime=now(), description = "orange", baby=sara)
event2.save()    

event3 = Event(type="POOP", datetime=now(), description = "green poop", baby=sara)
event3.save()    