FROM debian:sid-slim 

RUN apt-get update --fix-missing -y && apt upgrade -y \
    apt-get install -yqq --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    openssh-client \
    g++ \
    gcc \
    curl \
    gpg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*