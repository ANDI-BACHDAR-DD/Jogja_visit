#!/bin/bash
set -e

# Warna untuk output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Memulai semua service JogjaVisit secara lokal...${NC}"

# 1. API Gateway
echo -e "${GREEN}[1/5] Memulai API Gateway...${NC}"
cd api-gateway
npm install
node index.js &
cd ..

# 2. Wisata Service (Python)
echo -e "${GREEN}[2/5] Memulai Wisata Service...${NC}"
cd wisata-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 &
deactivate
cd ..

# 3. Rental Service (Node.js)
echo -e "${GREEN}[3/5] Memulai Rental Service...${NC}"
cd rental-service
npm install
node server.js &
cd ..

# 4. Kuliner Service (Python - Pengganti Go)
echo -e "${GREEN}[4/5] Memulai Kuliner Service...${NC}"
cd kuliner-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py &
deactivate
cd ..

# 5. Harvester Service (Python)
echo -e "${GREEN}[5/5] Memulai Harvester Service...${NC}"
cd harvester-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python harvester.py &
deactivate
cd ..

echo -e "${GREEN}Semua backend service telah berjalan di latar belakang!${NC}"
echo -e "API Gateway berjalan di http://localhost:4000"
echo -e "Untuk menghentikan semua service, tekan Ctrl+C pada terminal yang menjalankan script ini, atau jalankan 'pkill node && pkill python && pkill go'"

wait
