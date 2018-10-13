FROM cloudera/quickstart:latest

COPY ./app/* /app/

WORKDIR /app

RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all
RUN pip install oauth2

RUN chmod +x /app/entrypoint.sh && chmod +x /app/twitterstream.py

CMD ["/app/entrypoint.sh"]