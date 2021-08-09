function previewFile() {
    var preview = document.getElementById("blah");
    var file    = document.getElementById("images").files[0];
    var reader  = new FileReader();
    
    reader.onloadend = function () {
        
        const base64=resizeImage(reader.result)
        var processed="asd";
        
        processed=base64.then((a) => {
            console.log(typeof(a));
            // console.log(a);
            preview.src = a;
            const len=a.length;
            console.log("len:",len);
            for(i=0;i<len;i++)
            {
                var temp=a.substring(i,i+6);
                if (temp==="base64")
                {
                    break;
                }
            }
            a=a.substring(i+6+1);

            var packet_to_sent={0:`${a}`}
            console.log(packet_to_sent);

            const dataToSend = JSON.stringify(packet_to_sent);
            // const dataToSend = packet_to_sent;
            let dataReceived = ""; 
            fetch("https://ai-cat-dog-classifier.herokuapp.com/api/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: dataToSend
            })
            .then(response => response.json())
            .then(data =>{ 
                const dogscore=parseInt(data[0]["dog"]);
                const catscore=100-dogscore;
                console.log(dogscore);
                document.getElementById("score").innerHTML = `dog:${dogscore}% cat:${catscore}%`;
            })
              .catch(err => {
                console.log(err)
              })
        
        
        
        });
    }
  
    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = "";
    }
}

function resizeImage(base64Str, maxWidth = 150, maxHeight = 150) {
    return new Promise((resolve) => {
      let img = new Image()
      img.src = base64Str
      img.onload = () => {
        let canvas = document.createElement('canvas')
        canvas.width = maxWidth
        canvas.height = maxWidth
        let ctx = canvas.getContext('2d')
        ctx.drawImage(img, 0, 0, maxWidth, maxWidth)
        resolve(canvas.toDataURL())
      }
    })
  }