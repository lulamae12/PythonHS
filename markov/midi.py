import mido,pygame,time
import pygame.midi

clock = pygame.time.Clock()
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)
def inspect(filename):
    mid = mido.MidiFile(filename)
    
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        
        for msg in track:
            msgBytes = msg.bytes()
            
            splitMsg = str(msg).split()
            noteTime = splitMsg[len(splitMsg)-1]
            noteTime = noteTime.replace("time=","")
            noteTime = noteTime.replace(">","")
            noteTime = int(noteTime)
            

            
            print(msg)
            print(splitMsg)
            
            print(noteTime)
            print(msgBytes)
            print("")
            try:
                if splitMsg[0] == "note_on":
                    player.note_on(msgBytes[1],msgBytes[2],9)
                else:
                    player.note_off(msgBytes[1],msgBytes[2],9)
                
                
                time.sleep(.5)
            except:
                pass
            
            #time.sleep(time - 1000)
inspect("mii.mid")
player.close()