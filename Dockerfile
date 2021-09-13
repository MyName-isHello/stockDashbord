FROM ubuntu:20.04
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install python3.9 -y
RUN apt-get install python3-pip -y
RUN apt-get install build-essential -y  
RUN apt-get install git -y
RUN apt-get install python3 -y 
RUN apt-get install python3-dev -y 

RUN apt-get install libsdl2-dev -y
RUN apt-get install libsdl2-image-dev -y 
RUN apt-get install libsdl2-mixer-dev -y 
RUN apt-get install libsdl2-ttf-dev -y 
RUN apt-get install libportmidi-dev -y 
RUN apt-get install libswscale-dev -y 
RUN apt-get install libavformat-dev -y 
RUN apt-get install libavcodec-dev -y 
RUN apt-get install zlib1g-dev -y

# Install gstreamer for audio, video (optional)
RUN apt-get install libgstreamer1.0 -y
RUN apt-get install gstreamer1.0-plugins-base -y
RUN apt-get install gstreamer1.0-plugins-good -y

RUN pip3 install cython

RUN pip install -r requirements.txt
RUN python src/test.py 
