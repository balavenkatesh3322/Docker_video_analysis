from vidgear.gears import VideoGear
from vidgear.gears import NetGear

stream = VideoGear(source='videos/test.mp4').start() #Open any video stream
server = NetGear(address = 'localhost', port = '8000', protocol = 'tcp',  pattern = 0, receive_mode = False, logging = True, **options)

while True:
    try: 
        frame = stream.read()
        if frame is None:
            break
        server.send(frame)

    except KeyboardInterrupt:
        break

stream.stop()
writer.close()