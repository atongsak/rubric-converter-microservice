var express = require("express")
const multer = require('multer');
var app = express()

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/'); // Save files to the 'uploads' folder
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    },
});

const upload = multer({ storage: storage });

app.use(express.static("static"))

app.get("/", function (req, res, next) {
    res.status(200).sendFile(__dirname + "/index.html")
})

// Handle file upload
app.post('/upload', upload.single('file'), (req, res) => {
    res.send('File uploaded successfully!');
  });

const PORT = process.env.PORT || 3000;

app.listen(PORT, function(){
    console.log(`Server is listening on port ${PORT}`);
})

