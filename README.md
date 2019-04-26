# homework4
  
**電腦視覺特效-第六組**  
  
##  A sequence of moving-forward images in NTHU campus
拍攝的景點位於台達館後面，拍攝影片的過程中，則需要保持身體平衡進行拍攝(為了避免之後圖片matching的結果歪掉)。而在拍完影片後
，再對影片中的frame進行擷取，選出以下 Moving-foward的images!<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/0.png" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/1.png" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/2.png" width="216" height="384"><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/3.png" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/4.png" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/5.png" width="216" height="384">

## Feature extraction and matching results
以下圖片為我們透過ORB這個方法進行Feature extraction and matching所產生的結果。而左邊的圖片為第一部分中所提及的moving forward的images，右邊為上一個timestep align完的圖片擷取中間的結果。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/matches1.jpg" width="400" height="400">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/matches2.jpg" width="400" height="400">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/matches3.jpg" width="400" height="400">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/matches4.jpg" width="400" height="400">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/matches5.jpg" width="400" height="400">

## Image alignment and infinite zooming effect
以下附圖為第一部分所提及前2張 moving forward的images align後所形成的圖片。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/combine1.jpg" width="216" height="384"><br><br>
以下附圖為第一部分所提及前3張 moving forward的images align後所形成的圖片。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/combine2.jpg" width="216" height="384"><br><br>
以下附圖為第一部分所提及前4張 moving forward的images align後所形成的圖片。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/combine3.jpg" width="216" height="384"><br><br>
以下附圖為第一部分所提及前5張 moving forward的images align後所形成的圖片。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/combine4.jpg" width="216" height="384"><br><br>
以下附圖為第一部分所提及前6張 moving forward的images align後所形成的圖片。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/combine5.jpg" width="216" height="384"><br><br>
而gif檔案則為zooming effect<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/ORB/giphy.gif" width="216" height="384"><br>

## Implement different feature extrators
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SURF/combine5.jpg" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/cross_false.jpg" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SIFT/giphy.gif" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SURF/giphy.gif" width="216" height="384"><br>

## Add some image processing to enhance effect
