# uses a light python 3
FROM python:3-alpine
# where files will go
WORKDIR /app
# pip install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of my files - line below copies everything - need to use var for spaces
# COPY . .
COPY main.py client.py slashcommands.py token.txt .

CMD [ "python", "./main.py" ]

# use commands below - I built for rpi - docker needs to be running to build
# docker buildx build -t discord.py-starter --platform linux/arm64 .
# docker image ls
# to get tar file for remote server:
# docker save {ID} -o ./image.tar
# run it how you wish
# docker run discord.py-starter

# to check build
# docker buildx build -o - . > image1.tar --platform linux/arm64