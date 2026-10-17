from flask import Flask, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PakTools - Free Online Tools for Pakistan</title>
<meta name="description" content="Free Online Tools - Word Counter, Age Calculator, BMI, Password Generator and more. Made in Pakistan.">
<style>
body{font-family:system-ui,sans-serif;background:#f0f4f0;margin:0;padding:0}
.header{background:linear-gradient(135deg,#006400,#00a000);color:white;padding:25px 15px;text-align:center}
.header h1{margin:0;font-size:28px}
.container{max-width:700px;margin:auto;padding:15px}
.card{background:white;border-radius:16px;padding:20px;margin:15px 0;box-shadow:0 4px 15px rgba(0,0,0,0.08)}
.card h2{margin-top:0;color:#006400;font-size:20px}
input,textarea,select{width:100%;box-sizing:border-box;padding:12px;border:1px solid #ddd;border-radius:10px;font-size:16px;margin:8px 0}
button{background:#006400;color:white;border:none;padding:12px 18px;border-radius:10px;font-weight:bold;cursor:pointer;margin:5px 5px 5px 0}
button:hover{background:#008000}
.result{background:#e8f5e9;padding:12px;border-radius:10px;margin-top:10px;font-weight:bold;color:#2e7d32}
.ad-box{background:#fffbe6;border:1px dashed #f9a825;padding:15px;text-align:center;color:#888;border-radius:10px;margin:15px 0}
.footer{text-align:center;padding:20px;color:#666;font-size:14px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
</style>
</head>
<body>
<div class="header">
<h1>PakTools 🇵🇰</h1>
<p>Pakistan's All-in-One Free Tools Website</p>
</div>

<div class="container">

<div class="ad-box">Ad Space - Yahan AdSense Ad Ayega</div>

<div class="card"><h2>1. Word & Character Counter</h2>
<textarea id="w1" rows="4" placeholder="Yahan text paste karo..." oninput="let t=this.value; document.getElementById('w1r').innerText='Words: '+t.trim().split(/\\s+/).filter(x=>x).length+' | Characters: '+t.length"></textarea>
<div id="w1r" class="result">Words: 0 | Characters: 0</div>
</div>

<div class="card"><h2>2. Age Calculator</h2>
<input type="date" id="dob">
<button onclick="let d=new Date(document.getElementById('dob').value); if(!d.getTime()) return alert('Date select karo'); let n=new Date(); let age=n.getFullYear()-d.getFullYear(); let m=n.getMonth()-d.getMonth(); if(m<0||(m===0&&n.getDate()<d.getDate())) age--; document.getElementById('ager').innerText='Aap ki umar: '+age+' saal'">Calculate</button>
<div id="ager" class="result">Result yahan ayega</div>
</div>

<div class="card"><h2>3. Text Case Converter</h2>
<textarea id="t2" rows="3" placeholder="Text likho..."></textarea><br>
<button onclick="document.getElementById('t2').value=document.getElementById('t2').value.toUpperCase()">UPPERCASE</button>
<button onclick="document.getElementById('t2').value=document.getElementById('t2').value.toLowerCase()">lowercase</button>
<button onclick="document.getElementById('t2').value=document.getElementById('t2').value.replace(/\\s+/g,' ').trim()">Remove Extra Spaces</button>
</div>

<div class="card"><h2>4. Strong Password Generator</h2>
<div class="grid"><input type="number" id="plen" value="12" min="4" max="32"><button onclick="let l=parseInt(document.getElementById('plen').value); let c='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$'; let p=''; for(let i=0;i<l;i++) p+=c[Math.floor(Math.random()*c.length)]; document.getElementById('pres').innerText=p">Generate</button></div>
<div id="pres" class="result" style="word-break:break-all">Click Generate</div>
</div>

<div class="card"><h2>5. BMI Calculator</h2>
<input type="number" id="w" placeholder="Wazan (kg) e.g. 70">
<input type="number" id="h" placeholder="Height (cm) e.g. 175">
<button onclick="let w=parseFloat(document.getElementById('w').value); let h=parseFloat(document.getElementById('h').value)/100; if(!w||!h) return alert('Wazan aur Height likho'); let b=w/(h*h); document.getElementById('bmi').innerText='BMI: '+b.toFixed(2)+' - '+(b<18.5?'Underweight':b<25?'Normal':b<30?'Overweight':'Obese')">Calculate BMI</button>
<div id="bmi" class="result"></div>
</div>

<div class="card"><h2>6. Percentage Calculator</h2>
<input type="number" id="p1" placeholder="Kitna % ? e.g. 10">
<input type="number" id="p2" placeholder="Kis ka ? e.g. 500">
<button onclick="let a=parseFloat(document.getElementById('p1').value); let b=parseFloat(document.getElementById('p2').value); document.getElementById('per').innerText=a+'% of '+b+' = '+(a*b/100)">Calculate</button>
<div id="per" class="result"></div>
</div>

<div class="ad-box">Ad Space - Yahan Dusra Ad Ayega</div>

<div class="card" style="text-align:center">
<h2 style="color:#333">About PakTools</h2>
<p>Ye website Pakistaniyon ke liye banayi gayi hai. Saare tools 100% free aur fast hain.</p>
<p><b>© 2026 PakTools - Made with ❤️ in Pakistan</b></p>
<p>Contact for Ads / Business: <b>paktools.contact@gmail.com</b></p>
</div>

</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

app.run(host='0.0.0.0', port=5000)
