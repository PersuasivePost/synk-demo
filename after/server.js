// Tiny inventory-style API. The SAME code runs in /before and /after;
// only package.json (dependency versions) and the Dockerfile (base image) differ.
const express = require('express');
const _ = require('lodash');
const moment = require('moment');
const jwt = require('jsonwebtoken');
const axios = require('axios');
const argv = require('minimist')(process.argv.slice(2));

const app = express();
const PORT = argv.port || process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'demo-secret-change-me';

app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

const products = [
  { id: 1, name: 'USB-C Cable', qty: 120, price: 199 },
  { id: 2, name: 'Wireless Mouse', qty: 8, price: 649 },
  { id: 3, name: 'Mechanical Keyboard', qty: 25, price: 3499 },
  { id: 4, name: 'Laptop Stand', qty: 40, price: 1299 },
];

app.get('/', (req, res) => {
  res.render('index', { products: _.sortBy(products, 'name'), now: moment().format('LLL') });
});

app.get('/health', (req, res) => res.json({ status: 'ok' }));

app.get('/api/products', (req, res) => {
  res.json(_.orderBy(products, ['qty'], ['asc']));
});

app.get('/api/time', (req, res) => {
  res.json({ now: moment().toISOString(), pretty: moment().format('dddd, MMMM Do YYYY, h:mm a') });
});

app.get('/api/token', (req, res) => {
  const token = jwt.sign({ user: 'demo' }, JWT_SECRET, { expiresIn: '1h' });
  const decoded = jwt.verify(token, JWT_SECRET);
  res.json({ token, decoded });
});

app.get('/api/ping', async (req, res) => {
  const r = await axios.get(`http://localhost:${PORT}/health`);
  res.json({ upstream: r.data });
});

app.listen(PORT, () => console.log(`Demo app listening on port ${PORT}`));
