from tracemalloc import stop
import vlc
import time
import keyboard

def main():
    
    player = vlc.MediaPlayer() # Creates the media player
    
    video_path = input("Enter video path: ")

    video = vlc.Media(video_path)

    player.set_media(video)

    player.play()

    while(True):
        
        if keyboard.is_pressed("space"):
            player.pause()
            time.sleep(0.1)     # Breather room so pause does not continue going
            
        elif keyboard.is_pressed("s"):
            break
            
        
    
main()
