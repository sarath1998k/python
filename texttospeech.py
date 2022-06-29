from gtts import gTTS
import os
text = " hi, i am sarath krishna"
output = gTTS(text=text,lang="en",slow=False)
output.save('output.mp3')
os.system("start output.mp3")