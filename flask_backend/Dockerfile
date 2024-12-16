FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

RUN apt-get update 
RUN apt install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

RUN pip3 install flask opencv-python pandas matplotlib seaborn scipy

COPY . .

CMD ["python3", "test_b.py"]

