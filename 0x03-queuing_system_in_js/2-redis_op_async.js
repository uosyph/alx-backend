import redis from 'redis';
const { promisify } = require('util')

const client = redis.createClient(); 
const asyncGet = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    console.log(await asyncGet(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
