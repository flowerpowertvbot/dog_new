#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import alsaaudio
import threading


server_ip ='192.168.100.98' 
port_rx = 5009
port_tx = 5010


device = 'default'
audio_out = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, channels = 1, rate = 44100, format = alsaaudio.PCM_FORMAT_S8, periodsize = 160, device = device)
audio_in = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, channels = 1, rate = 44100, format = alsaaudio.PCM_FORMAT_S8,  periodsize = 160, device = device)



sock_rx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_tx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock_rx.connect((server_ip, port_rx))
sock_tx.connect((server_ip, port_tx))



#sock_rx.send(b'1')
#sock_rx.close()

#sock_tx.send(b'1')
#sock_tx.close()


def recieve_audio():
    while(1):
        data = sock_rx.recv(1024)
        print (data)
        audio_out.write(data)
    sock_rx.close()


recieve_audio()
