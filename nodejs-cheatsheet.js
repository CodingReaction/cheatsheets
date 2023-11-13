/////////////////////      COMMON MODULES  ///////////////////////////
fs     FILESYSTEM
http   LAUNCH SERVER / SEND REQUESTS
https  SAME WITH SSL
path
os


///////////////////// FS   //////////////////////////////////////////
fs.writeFileSync('PATH.EXTENSION', 'text');

///////////////////// HTTP / BASIC SERVER ///////////////////////////////////////////
const server = http.createServer((req, resp)=>{...});
server.listen(PORT, START_CALLBACK);

//////////////////// REQUEST ////////////////////////////////////////
req.url     // "/", "/users/33"
req.method  // GET, POST
req.headers
req.on('data', (chunk) =>{
    console.log(chunk);
});
req.on('end', () =>{
    Buffer.concat(chunks).toString();
});

///////////////////  RESPONSE //////////////////////////////////////

res.setHeader('Content-Type', 'text/html');
res.write('<html>...</html>');
res.statusCode = 300
res.end();

