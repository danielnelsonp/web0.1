const request = require("supertest");
const app = require("./server");

let server;
let testPort;

beforeAll((done) => {
  server = app.listen(0, () => {  // Use port 0 to get a random available port
    testPort = server.address().port;
    done();
  });
});

afterAll((done) => {
  server.close(done);
});

describe("GET /", () => {
  it("should return Hello, Jenkins Deployment!", async () => {
    const response = await request(`http://localhost:${testPort}`).get("/");
    expect(response.text).toBe("Hello, Jenkins Deployment!");
    expect(response.statusCode).toBe(200);
  });
});

