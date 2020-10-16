function BDI(){
    var h=document.getElementById('h').value;
    var w=document.getElementById('w').value;
    var a=document.getElementById('a').value;
    var b=document.getElementById('b').value;
    var bdi=w*(a+b)/(h*h*h);
    document.getElementById("result").innerHTML="Your BDI is" + bdi;
  
    }


    