from pygame import mixer

mixer.init()
mixer.music.load('mona.mp3')
mixer.music.play()
mixer.event.wait()
print ('Agora vc esta ouvindo?')
