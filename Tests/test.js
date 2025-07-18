// test.js
const request = require('supertest');
const app = require('./app'); // path to your Express app

describe('API Endpoints', () => {
  it('GET / should return a welcome message', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('message', 'Welcome to the API');
  });

  it('POST /login should return a token', async () => {
    const res = await request(app)
      .post('/login')
      .send({ username: 'testuser', password: 'password123' });

    expect(res.statusCode).toBe(200);
    expect(res.body).toHaveProperty('token');
  });

  it('GET /protected should return 401 if not authenticated', async () => {
    const res = await request(app).get('/protected');
    expect(res.statusCode).toBe(401);
  });
});