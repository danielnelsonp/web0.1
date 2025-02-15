const request = require('supertest');
const app = require('./server');

describe('GET /', () => {
    it('should return Hello, Jenkins Deployment!', async () => {
        const response = await request(app).get('/');
        expect(response.text).toBe('Hello, Jenkins Deployment!');
        expect(response.statusCode).toBe(200);
    });
});
