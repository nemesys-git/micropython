#The chorus of Hair by Little Mix. Coded by Ben Mustill-Rose, 13/06/2016.
from microbit import *
#As we're going to be playing music we'll need to import the music module:
import music

#All music has a tempo (how fast it is played) often given in beats per minute or BPM.
#The tempo of Hair is a (really quick!) 154BPM.
music.set_tempo(bpm=154)


#Parts of the chorus are repeated, so to make our program more efficient & easier to read...
#We've split the melody up into "lists" that we can use without typing all the notes out again.

#The "'Cause he was just a * and I knew it" passage:
#It's also the "I tried everything but it's useless" passage!
heWasJust=["a4:2", "b4:1", "r", "b", "r", "b", "r", "b:4", "a:2", "g:1", "r", "g:4", "a:2", "b"]

#The "Got me going mad sitting-" passage:
gotMeGoing=["a4:2", "b4:1", "r", "b", "r", "b", "r", "b:4", "a:2", "g:1", "r", "g:4"]

#The "-in this chair" passage:
#It's also the "-on the edge" passage!
thisChair=["a:2", "b", "a:6", "g", "e"]

#The "Like I don't care" passage:
likeI=["d:2", "g:4", "a:2", "b", "a:6", "g", "c"]

#The "Gotta get him out my hair" passage:
gottaGetHim=["c4:1", "c", "c", "r", "c:2", "c", "c", "c", "b3"]

#The "He pushed me so far now I'm-" passage:
hePushedMe=["d4:2", "a", "b:1", "r", "b:4", "d5:2", "b4", "a", "g:1", "r", "g:4"]

#The "#Make him disappear" passage:
makeHimDis=["d4:1", "r", "d:2", "e", "g:4", "a:2", "b", "a:6", "g", "c"]

#The "Go get him out my hair" passage (Different to the "Gotta het him" passage!):
goGetHim=["c4:2", "c", "c", "c", "c", "c", "b3"]

#Now that we've created all the lists we need for the chorus lets play some music!
#We want the chorus to play forever, we're using a "while" loop that will never exit.
while True:
    music.play("d4:2") #'Cause
    music.play(heWasJust) #he was just a * and I knew it
    music.play("r:8")
    music.play(gotMeGoing) #Got me going mad sitting-
    music.play(thisChair) #-in this chair
    music.play("r:4")
    music.play(likeI) #Like I don't care
    music.play(gottaGetHim) #Gotta get him out my hair
    music.play("r:8")
    music.play(heWasJust) #I tried everything but it's useless
    music.play("r:6")
    music.play(hePushedMe) #He pushed me so far, now I'm-
    music.play(thisChair) #-on the edge
    music.play(makeHimDis) #Make him disappear
    music.play(goGetHim) #Go get him out my hair
    music.play("r:10")