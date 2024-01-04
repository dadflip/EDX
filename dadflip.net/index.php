<!DOCTYPE html>
<html style="background-color:lightgreen">

  <head>
    <meta charset="utf-8">

    <title>dadflip.ddns.net</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300|Sonsie+One" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  </head>
  
  <script>
	function move() {
	  var elem = document.getElementById("myBar");   
	  var width = 20;
	  var id = setInterval(frame, 10);
	  function frame() {
	    if (width >= 100) {
	      clearInterval(id);
	    } else {
	      width++; 
	      elem.style.width = width + '%'; 
	      elem.innerHTML = width * 1  + '%';
	    }
	  }
	}
</script>



  <body>
    <header>
      <h1><center>DADFLIP DDNS</center></h1>
    </header>


    <main class="w3-panel">
    	<div class="w3-container">
	  <div class="w3-bar w3-light-grey">
	    <a href="#" class="w3-bar-item w3-button">Home</a>
	    <a class="w3-bar-item w3-button" href="/main/splash/index.html">My Website</a>
	    <div class="w3-dropdown-hover">
	      <button class="w3-button">Liens</button>
	      <div class="w3-dropdown-content w3-bar-block w3-card-4">
		<center><a class="w3-bar-item w3-button" href="http://myesp.onthewifi.com/">ESP CONTROL</a></center>
		<center><a class="w3-bar-item w3-button" href="https://github.com/dadflip">GITHUB</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.tinkercad.com/dashboard">TINKERCAD (Dr. flipper)</a></center>
		<center><a class="w3-bar-item w3-button" href="https://scratch.mit.edu/mystuff/">SCRATCH MIT EDU</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.youtube.com/@dadflip">DADFLIP'S CHANNEL</a></center>
		<center><a class="w3-bar-item w3-button" href="https://cas.utbm.fr/login?service=https://monespace.utbm.fr/Login">UTBM CAS</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.riotgames.com/fr">RIOT GAMES</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.root-me.org/?page=news&lang=fr">ROOT ME</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.twitch.tv/">TWITCH</a></center>
		<center><a class="w3-bar-item w3-button" href="https://www.instagram.com/dadflip_channel/">INSTAGRAM</a></center>
	      </div>
	    </div>
	  </div>
	</div>
    
    	</br>
    	
    	<center><form action="filepost.php" method="post" enctype="multipart/form-data">
	 <div>
	   <label for="file"> Sélectionner le fichier à envoyer</label></br>
	   <input class="w3-button w3-black w3-round-xlarge" type="file" id="file" name="file" multiple>
	 </div>
	 <div>
	   <p><button onclick="move()" class="w3-button w3-black w3-round-xlarge">Envoyer</button></p>
	 </div>
	</form></center>
	
	<div class="w3-light-grey">
	  <div id="myBar" class="w3-container w3-green w3-center" style="width:20%">20%</div>
	</div>
	</br></br>
    	
    	<li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="/main/splash/index.html">GO</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-black w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="http://myesp.onthewifi.com/">ESP CONTROL</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://github.com/dadflip">GITHUB</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-black w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.tinkercad.com/dashboard">TINKERCAD</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://scratch.mit.edu/mystuff/">SCRATCH MIT EDU</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-black w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.youtube.com/@dadflip">DADFLIP'S CHANNEL</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.riotgames.com/fr">RIOT GAMES</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-black w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.root-me.org/?page=news&lang=fr">ROOT ME</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://cas.utbm.fr/login?service=https://monespace.utbm.fr/Login">UTBM CAS</a></span><br>
	  </div>
	</li>
	
	<li class="w3-bar w3-black w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.twitch.tv/">TWITCH</a></span><br>
	    </div>
	</li>
	    
	    <li class="w3-bar w3-blue w3-tiny">
	  <span onclick="this.parentElement.style.display='none'"
	  class="w3-bar-item w3-button w3-xlarge w3-right">&times;</span>
	  <!--<img src="img_avatar2.png" class="w3-bar-item w3-circle" style="width:85px"> -->
	  <div class="w3-bar-item ">
	    <span class="w3-xlarge w3-center"><a class="w3-bar-item w3-button" href="https://www.instagram.com/dadflip_channel/">INSTAGRAM</a></span><br>
	    </div>
	</li>
	
	</br>
	
    </main>

  </body>
</html>
