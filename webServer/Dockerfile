FROM alpine:latest
MAINTAINER from yuyong_id

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories;\
    apk --update add --no-cache python py-pip gcc python-dev musl-dev libffi-dev openssl-dev;\
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple itchatmp

COPY weChatServer.py /
RUN chmod 775 /weChatServer.py

EXPOSE 5000

CMD ["/weChatServer.py"]

