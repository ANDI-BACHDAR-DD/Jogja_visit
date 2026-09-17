require('dotenv').config();
const express = require('express');
const cors = require('cors');
const axios = require('axios');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.PORT || 4000;

// Middleware
app.use(cors());
app.use(express.json());

// Rate Limiting
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
    message: "Terlalu banyak request dari IP ini, silakan coba lagi setelah 15 menit"
});
app.use(limiter);

// Service URLs (akan di-set via .env, default ke localhost untuk development)
const WISATA_SERVICE_URL = process.env.WISATA_SERVICE_URL || 'http://localhost:8001';
const RENTAL_SERVICE_URL = process.env.RENTAL_SERVICE_URL || 'http://localhost:8002';
const KULINER_SERVICE_URL = process.env.KULINER_SERVICE_URL || 'http://localhost:8003';

// Helper function untuk forward request
const forwardRequest = async (url, req, res) => {
    try {
        const response = await axios({
            method: req.method,
            url: `${url}${req.originalUrl}`,
            data: req.body,
            headers: {
                'Authorization': req.headers['authorization']
            }
        });
        res.status(response.status).json(response.data);
    } catch (error) {
        if (error.response) {
            res.status(error.response.status).json(error.response.data);
        } else {
            res.status(500).json({ message: 'Internal Server Error', details: error.message });
        }
    }
};

// Routes
app.get('/health', (req, res) => {
    res.json({ status: 'API Gateway is running' });
});

app.use('/api/wisata', (req, res) => forwardRequest(WISATA_SERVICE_URL, req, res));
app.use('/api/rental', (req, res) => forwardRequest(RENTAL_SERVICE_URL, req, res));
app.use('/api/kuliner', (req, res) => forwardRequest(KULINER_SERVICE_URL, req, res));

app.listen(PORT, () => {
    console.log(`API Gateway berjalan di port ${PORT}`);
});
