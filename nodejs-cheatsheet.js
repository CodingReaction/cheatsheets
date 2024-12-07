/////////////////////      COMMON MODULES  ///////////////////////////
fs     FILESYSTEM
http   LAUNCH SERVER / SEND REQUESTS
https  SAME WITH SSL
path
os

node-fetch
nodemon
cors
bcrypt
jsonwebtoken
express-validator
pm2


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

http.request('path', (res)=>{
  res.on('data', (chunk) => {
    console.log(`Data: ${chunk}`);}
  res.on('end', ()=> { console.log('ended'); });
});

///////////////////  RESPONSE //////////////////////////////////////

res.setHeader('Content-Type', 'text/html');
res.write('<html>...</html>');
res.json({name: "Max"});
res.statusCode = 300
res.end();

/////////////////// EXPRESS JS ///////////////////////////////////
// npx express-generator
const express = require('express');

const app = express();
const PORT = 8000;

app.get('/', (req, res) => { // app.method(PATH, HANDLER)
  res.send('Hello');
});

app.listen(PORT, ()=>{
  console.log('Listening on port ', PORT);
});

/////////////////// VALIDATOR (express-validator) ///////////////
const {check, validationResult} = require('express-validator');

router.get("", [check('title').not().isEmpty(), check('description').isLength({min: 5})], (req, res)=>{
  const errors = validationResult(req);
  if (!errors.isEmpty()){
    console.log(errors);
    throw new HttpError("something when wrong", 422);
  }
});

/////////////////// STATIC FILES /////////////////////////////////
const path = require('path');
app.use('/static', express.static(path.join(__dirname, 'public'));

app.use(express.static('public')); 	      // localhost:8000/images/cat.png
app.use('/static', express.static('public')); // localhost:8000/static/images/cat.png

////////////////// TEMPLATING HTML5 ////////////////////
 app.set('view engine', 'ejs');
 app.get(..., ()=> res.render("index", {name: "Max"})); // <%= locals.text || 'default' %>

////////////////// ROUTER /////////////////////////////////////

app.get('/', (req, res) =>{}); // path-to-regexp lib
app.use()
app.all('/secret', (req, res, next)=>{ // load middleware at a path for all HTTP methods, use '*' for all routes
  console.log("accessing");
  next();
});
app.post('/example-multiple-callbacks', (req, res, next) => next(), (req, res) => res.send('bye'));
app.get('/array-of-callbacks', [cb1, cb2, cb3]);

app.route('/chained-routes')
  .get(...)
  .post(...)

app.get('/*', (req, res) => res.sendFile(path.join(__dirname, '..', 'public', 'index.html')); // serve a frontend. route at end

const birdsRouter = express.Router();

birdsRouter.use((req, res, next) => "router middleware");
birdsRouter.get('/', (req, res) => {...});

app.use('/birds', birdsRouter);

//////////////// PARAMS, BODY ///////////////////////////
'/users/:userId'          -> req.params -> {"userId": 12}
'flights/:from-:to'       -> req.params -> {"from": "Uruguay", "to": "Argentina"}
'plantae/:genus.:species' -> req.params -> {"genus":..., "species": ...}

///////////////// RESPONSE TYPES ///////////////////////
- res.json({user: 'Max'});
- res.render(PATH_TO_VIEW, locals?={name: "Max"}, (err, html) => { res.send(html); });
- res.download('/files/report.pdf', 'my-report.pdf', options?={maxAge, root, lastModified, headers,cacheControl}, (err)=>{...});
- res.sendFile('SAME AS res.download')
- res.send('ANYTHING: json, Buffer.from("bla"), text/html, text/plain')// previously call res.set('Content-Type', 'text/html')
- res.format({            // content-negociation bassed on Accept HTTP header from request
    'text/plain': function() { res.send('hey') },
    'application/json': function() { res.send({message: 'hey'})},
    default: function() { res.status(406).send('Not acceptable') },
  });

- res.location('http://example.com'); // Set response Location HTTP header . res.location('back') is special
- res.redirect('/foo/bar'); // (301, 'http://google.com') "../login" "/foo/bar"
- res.end()   // .end() = end response without data
- res.sendStatus(404)
- res.set('Content-Type', 'text/plain') // set response HTTP header
- res.get('Content-Type') // returns HTTP response header. "text/plain" in this case

- res.status(500)
- res.type('application/json')

//////////////// MIDDLEWARES //////////////////////
app.use(morgan("combined"));
app.use((req, res, next) => { console.log('Logger'); re.requestTime = Date.now(); next(); }); // Logger + request time
app.use(cookieParser()); // cookieParser = require('cookie-parser')
app.use(async (req, res, next) => await validator(req.cookies); next() });
app.use(express.json()); //parse the body on req, req.body
app.use(express.urlenconded({extended: true}); //info that comes from forms
/////////////// LOGGER ///////////////////////////////

///////////////// READ FILES, CSV, JSON ////////////////////////////////////
req.files.avatar

///////////////// ENV /////////////////////////////////////////
const dotEnv = require("dotenv").config();
const PORT = process.env.PORT;

//////////////// SESSIONS COOKIES ///////////////////////////

///////////////// CORS CSRF //////////////////////////////////
// CORS: Access-Control-Allow-Origins
const cors = require('cors');
app.use(cors({ origin: ['http://localhost:5071/'], credentials: true, methods: ["GET", "POST"]}));

///////////////// TESTING ////////////////////////////

//////////////// MONGO DB / MONGOOSE ////////////////////////
const {MongoClient, ServerApiVersion } = require("mongodb");

const uri = `mongodb+src://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/`;
const client = new MongoClient(uri, {
  serverApi:{
    version: ServerApiVersion.v1, strict: true, deprecationErrrors: true, }});

async function run(){
  try {
    await client.connect();
    await client.db("my_db").command({ping: 1});
  } finally {
    await client.close();
}}

run().catch(console.dir);

const UserSchema = mongoose.Schema({ // Store documents in collections
  firstName: String,
  email: { type: String, unique: true},
  password: String,
  role: Boolean
});

module.exports = mongoose.model("User", UserSchema);

const user = new User({...});
const salt = bcrypt.genSaltSync(10);
const hashPassword = bcrypt.hasSync(password, salt);

user.password = hashPassword;
user.save((err, userStore) => {
  if (error) res.status(400).send({msg: "Error al crear usuario"});
  else res.status(200).send(user);
});

User.findOne({email}, (error, userStore) =>{...});

//////////////// JWT / JSONWEBTOKEN /////////////////////////
function createAccessToken(user){ // refresh token same with more expiration time
  const expToken = new Date();
  expToken.setHour(expToken.getHour() + 10);
  const payload = {
    token_type: "access",
    user_id: user._id,
    iat: Date.now(),
    exp: expToken.getTime(),
  };
  return jwt.sign(payload, JWT_SECRET_KEY);
}

function decodeToken(token){
  return jwt.decode(token, JWT_SECRET_KEY, true);
}

bcrypt.compare(password, userStore.password);

req.headers.authorization // to fetch the "Bearer TOKEN"

 const bcrypt = require("bcrypt");
 const hashedPassword = await bcrypt.hash(rawPassword, 10);
 //jsonwebtoken package
 const jwt = require("jsonwebtoken");
 if (user && (await bcrypt.compare(rawPassword, user.hashedPass))
   access = jwt.sign(
	   {id: user.id, email: user.email},
	   process.env.TOKEN_SECRET,
   	   {expiresIn: "1m"})
   return res.status(200).json({access});

   const validateToken = asyncHandler(async(req, res, next) =>
   let token;
   let authHeader = req.headers.Authorization || req.headers.authorization;
   if (authHeader && authHeader.startsWith("Bearer")){
     token = authHeader.split(" ")[1];
     jwt.verify(token, process.env.TOKEN_SECRET, (err, decoded) =>{
	     if (err) thrown new Error("user not authorized");
	     req.user = decoded.user
	     next();
     });
    }

//////////////// PASSPORT JS /////////////////////////////////

//////////////// GRAPH QL //////////////////////////////////

//////////////// TRPC    //////////////////////////////////

//////////////// ZOD //////////////////////////////////////
https://dev.to/osalumense/validating-request-data-in-expressjs-using-zod-a-comprehensive-guide-3a0j

//////////////// SOCKETS    /////////////////////////////////
IP SOCKETS
DATAGRAM SOCKETS
TCP SOCKETS
WEB SOCKETS

//////////////// NODEJS EVENT LOOP OPTIMIZATION /////////////

//////////////// DRIZZLE ORM /////////////////////////
packages: @types/node, tsx, typescrit

> npm i drizzle-orm postgres
> npm i -D drizzle-kit

> npx drizzle-kit generate:pg // generate migration file
> npx drizzle-kit generate:drop

#drizzle.config.ts
import {defineConfig} from "drizzle-kit";

export default defineConfig({
  schema: "./src/drizzle/schema.ts",
  out: "./src/drizzle/migrations",
  driver: "pg",
  dbCredentials: {
    connectionString: process.env.DATABASE_URL as string
  },
  verbose: true,
  strict: true
});

#schema.ts
import {pgTable, uuid, serial, varchar} from "drizzle-orm/pg-core";

export const UserRole = pgEnum("userRole", ["ADMIN", "BASIC"]);

export const UserTable = pgTable("user",{
  id:  uuid("id").primaryKey().defaultRandom(),
  id2: serial("id2").primaryKey(),
  name: varchar("name", {length: 255}).notNull(),
  age: integer("age").notNull(),
  email: varchar("email", {length: 255}).notNull().unique(),
  role: UserRole("userRole").default("BASIC").notNull(),
  userProfile: uuid("profileId").references(() => ProfileTable.id).notNul();
}, table => {
				return {
				   emailIndex: index("emailIndex").on(table.email),
				   uniqueNameAndAge: unique("uniqueNameAndAge").on(table.name, table.age),

  // supose a category table for many to many
  //
				   //
const PostCategoryTable = pgTable("post-category", {
  postId: ...,
  categoryId: ...,
}, table => ({pk: primaryKey({ columns: table.postId, table.categoryId})});

#migrate.ts // code for running the migrations
import "dotenv/config"
import {drizzle} from 'drizzle-orm/postgres-js';
import {migrate} from 'drizzle-orm/postgres-js/migrator';
import postgres from 'postgres';

// create a command to run this file
const migrationClient = postgres(PG_URL) // RUN a migration
await migrate(drizzle(migrationClient), {migrationFolder: '');
await migrateClient.end();

const queryClient = postgres(PG_URL); // RUN a query
const db = drizzle(queryClient, { schema, logger: true});
await db.select().drom(...)

await db.insert(UserTable).values({name: "max"});
await db.query.UserTable
