import wave
import struct

params = (1, 2, 44100, 0, 'NONE', 'not compressed') 
output = wave.open('sample-15s - Copy.wav', 'w')
output.setparams(params)

for i in range(0, 44100):
    value = int(32767.0 * 0.5 * (i / 44100)) 
    packed_value = struct.pack('h', value) 
    output.writeframes(packed_value)

output.close()

input_wave = wave.open('sample-15s.wav', 'r')
params = input_wave.getparams()
frames = input_wave.readframes(params.nframes)
input_wave.close()

output = wave.open('modified_sample-15s - Copy.wav', 'w')
output.setparams(params)
scaled_frames = bytearray()
for i in range(0, len(frames), 2):
    value = struct.unpack('h', frames[i:i+2])[0] 
    value = int(value * 1.5)  
    scaled_frames.extend(struct.pack('h', value))

output.writeframes(bytes(scaled_frames))
output.close()
