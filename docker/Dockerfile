FROM openelevation/open-elevation

RUN apt-get update
RUN apt-get install -y vim openssh-server  


# SSH Server
RUN sed -i 's/^\(PermitRootLogin\).*/\1 yes/g' /etc/ssh/sshd_config && \
    sed -i 's/^PermitEmptyPasswords .*/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && \
    echo 'root:ai1234' > /tmp/passwd && \
    chpasswd < /tmp/passwd && \
    rm -rf /tmp/passwd 


# 生成sshkey
#RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key

RUN echo "root:ai1234"|chpasswd


#jupyter
RUN pip3 install jupyter -i https://pypi.douban.com/simple  && ln -s /usr/local/python37/bin/jupyter /usr/bin/jupyter

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN chmod +x  /run_jupyter.sh


WORKDIR /code
#CMD python3 server.py

EXPOSE 8080

EXPOSE 8888

EXPOSE 8443

EXPOSE 22
