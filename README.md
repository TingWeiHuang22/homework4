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
以下兩張圖是吾組再進行Surf這個feature extrator的過程中，發現的一個需要注意的點，那就吾組再自行撰寫的程式中matcher=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=cross)的crossCheck的bool值為true還是false，會影響最後生成的圖片。左圖的cross為false，其圖片最後面的建築物本應是正的，卻會變成斜體的，然而右圖的cross為true，其圖片最後面的建築物則如預期一樣為正。吾組認為會造成此現在的原因在於，若是crossCheck的值不為true的話，再兩張圖片進行matching後的線會彼此交錯，而這交錯就會導致圖片中的背景因此會迥異於原本應有的形狀。是故吾組認為再不論是ORB SIFT SURF的crossCheck都應該設成true，以避免上述情況發生。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/cross_false.jpg" width="216" height="384">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SURF/combine5.jpg" width="216" height="384"><br><br>
以下所產生的gif，其crossCheck的值皆為true，至於false的部分則暫不討論。<br>
以下為透過SIFT feature extrator所產生出來的gif檔<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SIFT/giphy.gif" width="216" height="384"><br>
以下為透過SURF feature extrator所產生出來的gif檔<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SURF/giphy.gif" width="216" height="384"><br>
從上述SIFT以及SURF的GIF檔案比較中可以看出圖片最後面中的建築物，SURF的建築物會比SIFT的建築物而言相對正常。吾組認為造成其中的原因在於以下的右圖中SURF extrator所產生出來的matching的線比起左圖SIFT extrator所產生出來的matching的線相對多許多，雖然兩者彼此中的線有幾條是交錯的，然而SURF的matching的線相對大量以至於產生出來的圖片內的建築物不會有斜體的現象。<br><br>
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SIFT/matches5.jpg" width="400" height="400">
<img src="https://github.com/TingWeiHuang22/homework4/blob/master/picture/SURF/matches5.jpg" width="400" height="400">

## Add some image processing to enhance effect
