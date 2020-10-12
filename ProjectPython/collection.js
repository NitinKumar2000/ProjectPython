var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost/SubProjectDB';
MongoClient.connect(url, function (err, db) {
    if (err) throw err;

    

    console.log("Database created");
    db.close();
});