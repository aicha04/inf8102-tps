# Git and hardening
sudo apt update
sudo apt install git
mkdir polylab && cd polylab && git clone https://github.com/konstruktoid/hardening
cd hardening && sudo ./ubuntu.sh
sudo ufw allow ssh

# Docker https://docs.docker.com/engine/install/ubuntu/ 
sudo apt-get update
sudo apt-get install \
	ca-certificates \
	curl \
	gnupg \
	lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Docker scan and Trivy
sudo apt-get install docker-scan-plugin jq
sudo apt-get install trivy
