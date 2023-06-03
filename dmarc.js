const dmarc = require('dmarc-solution');
const express= require('express');
const app=express();
const {PythonShell}=require('python-shell');


app.use(express.json());
app
.post('/', dmarccheck)
.get('/', mail);

let domain='';
let recieverMail='';
let senderName='';

async function dmarccheck(req, res) {
    let object= req.body;
    domain=object.domain;
    recieverMail=object.mail;
    senderName=object.name;

    try{
        const record= await dmarc.fetch(domain)
        res.status(200).json({data: record});
    }
    catch(err){
        res.status(404).json({error: 'dmarc not found. proceed to spoof'});
    }
}

let senderMail= `admin@${domain}`;

function mail(req, res){
    try{
        let options={
            scriptPath: "C:/Users/riya5/OneDrive/Documents/projects/email spoof",
            args:[senderName, senderMail, recieverMail]
        }
        PythonShell.run("spoof.py", options, (err, response)=>{
            if (err){
                console.log(err);
            }
            else{
                console.log(response);
                res.json({message: 'mail sent successfully'});
            }
        });   
             
    }
    catch(err){
        console.log(err);
    }
}



app.listen(8080,()=>{
    console.log("listening on port 8080");
});