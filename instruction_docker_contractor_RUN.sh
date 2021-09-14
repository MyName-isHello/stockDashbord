#!/bin/bash
docker run -it --rm -e DISPLAY=docker.for.mac.host.internal:0 --net=host -v /Users/wtcheung/Public/file_stockDashbord/stockDashbord:/app --name doccon test /bin/bash
