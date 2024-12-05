// SHELL
> show dbs // doesn't show empty dbs
> use school
> show collections
> db.createCollection("students")
> db.createCollections("teachers", {capped: true, size: 10 * 1024, max: 100, autoIndexId: true}) // capped == max size in bytes,
> db.techers.drop()

> db.students.insertOne({name: "Max", age: 46, gpa: 4.1, registerDate: new Date()})
> db.students.insertMany([{name: "Pepe", age: 30}, {name: "Pupu", age: 25}])

> db.students.find()
> db.students.find({}, {name: true}) // all docs, only give name. ({query}, {projection})
> db.students.find().sort({name: 1}) // 1 = ALPHA order, -1 = REVERSE
> db.students.find().limit(2) // return only 2 documents

> db.students.updateOne({name: "Max"}, {$set: {name: "Maxi", fullTime: true}}) // ({filter}, {update})
> db.students.updateOne({_id: ObjectId("642c0..")}, {$set: {fullTime: false}}) // add field
> db.students.updateOne({_id: ...}, {$unset: {fullTime: ""}}) // remove field
> db.students.updateMany({}, {$set:{fullTime: false}}) // set or create field for many

> db.students.deleteOne({name: "Larry"})
> db.students.deleteMany({registerDate: {$exists: false}}) // if the field doesn't exists, delete

> db.students.find({name: "Larry"}).explain("executionStats")
> db.students.createIndex({name: 1}) // name_1 is the name of the index in this case, 1 == alphabetical
> db.students.getIndexes()
> db.students.dropIndex("name_1")

// DATA TYPES
age: 32                  // number
fullTime: false          // boolean
registerDate: new Date() // dates in UTC
graduationDate: null     // null
courses: ["Biology", "Chemistry", "Calculus"]              // array
address: {street: "123 fake st", city: "Somewhere"} // nested doc

// OPERATORS
$set
$unset
$exists
$ne // non equal
$lt $lte $gt $gte
$in $nin // .find({name: {$in: ["Pepe", "Koko"]}})
$and // .find({$and: [{$age: {$gt: 20, $lt: 30}}, {fullTime: true}]})
$or $nor
$not // .find({age: {$not: {$lt:30}}})
