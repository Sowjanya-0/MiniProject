function clicked(){
  var a = document.getElementById("img_uploaded").files[0].name;

  if(a.includes("img_1")){
    document.getElementById("image_dis").src = "/static/images/Apple___Apple_scab/"+a;
    document.getElementById("result").innerHTML = "Predicted Class of image : Scab";
  }
  else if (a.includes("img_2")) {
    document.getElementById("image_dis").src = "/static/images/Apple___Black_rot/"+a;
  document.getElementById("result").innerHTML = "Predicted Class of image : Black rot";

  }
  else if (a.includes("img_3")) {
    document.getElementById("image_dis").src = "/static/images/Apple___Cedar_apple_rust/"+a;
    document.getElementById("result").innerHTML = "Predicted Class of image : Cedar apple rust";

  }
  else if (a.includes("img_4")) {
    document.getElementById("image_dis").src = "/static/images/Apple___healthy/"+a;
    document.getElementById("result").innerHTML = "Predicted Class of image : Healthy";

  }

  var souce =fake_path.split("\\").pop();
  document.getElementById("image_dis").src = "/static/images/"+souce;

}
