/* Joe Huck Electric — shared page behavior */
(function(){
  var $=function(s,r){return (r||document).querySelector(s)};

  /* ---------- Start new pages at the top ----------
     A fresh link click should always open a page at its top. Some embedded
     viewers restore the previous scroll position after the page loads, so on
     a normal navigation (not Back/Forward or reload, and not a #anchor link)
     reset to the top now and again shortly after load, stopping as soon as
     the visitor scrolls, taps or types. */
  try{
    var nav0=performance.getEntriesByType&&performance.getEntriesByType("navigation")[0];
    if(!location.hash&&(!nav0||nav0.type==="navigate")){
      var userMoved=false,stop=function(){userMoved=true};
      ["wheel","touchstart","keydown","mousedown"].forEach(function(ev){addEventListener(ev,stop,{once:true,passive:true})});
      var toTop=function(){
        if(userMoved)return;
        try{window.scrollTo({top:0,left:0,behavior:"instant"})}catch(e){window.scrollTo(0,0)}
        if(document.scrollingElement)document.scrollingElement.scrollTop=0;
        try{document.documentElement.scrollIntoView({block:"start",behavior:"instant"})}catch(e){document.documentElement.scrollIntoView(true)}
      };
      toTop();
      addEventListener("DOMContentLoaded",toTop);
      addEventListener("load",function(){toTop();[60,200,500,1000,1800].forEach(function(ms){setTimeout(toTop,ms)})});
      addEventListener("pageshow",toTop);
    }
  }catch(e){}
  var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};

  /* ---------- Mobile nav ---------- */
  var mb=$(".menu-btn"),nav=$("#nav");
  if(mb&&nav){
    mb.addEventListener("click",function(){var o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o)});
    nav.addEventListener("click",function(e){if(e.target.tagName==="A"){nav.classList.remove("open");mb.setAttribute("aria-expanded","false")}});
  }

  /* ---------- Town suggestions for the estimate form ---------- */
  var TOWNS=["Yardley","Lower Makefield","Newtown","New Hope","Washington Crossing","Upper Makefield","Levittown","Fairless Hills","Falls Township","Langhorne","Middletown","Morrisville","Bristol","Bensalem","Penndel","Richboro","Holland","Churchville","Southampton","Feasterville","Trevose","Croydon","Tullytown","Doylestown","Warminster","Warrington","Buckingham","Solebury","Lahaska","Furlong","Jamison","Wrightstown","Ivyland","Hulmeville","Langhorne Manor","Northampton","Chalfont","New Britain","Perkasie","Sellersville","Quakertown","Upper Southampton","Lower Southampton","Feasterville-Trevose","Plumstead","Hilltown","West Rockhill","Richland","Milford"];
  var dl=$("#townlist");
  if(dl)TOWNS.forEach(function(t){var o=document.createElement("option");o.value=t;dl.appendChild(o)});

  /* ---------- Estimate form ----------
     TODO before launch: POST to your form handler (Formspree, Netlify Forms, CRM, etc.). */
  var qf=$("#quoteForm"),qd=$("#quoteDone"),qe=$("#q-err");
  if(qf){
    qf.addEventListener("submit",function(e){
      e.preventDefault();
      var name=qf.name.value.trim(),phone=qf.phone.value.trim(),digits=phone.replace(/\D/g,"");
      if(!name||digits.length<10){qe.hidden=false;qe.textContent=!name?"Add your name so we know who to ask for.":"Enter a 10-digit phone number so we can call you back.";(!name?qf.name:qf.phone).focus();return}
      qe.hidden=true;
      var svc=qf.service?qf.service.value:"";
      $("#doneMsg").textContent="Thanks, "+name.split(" ")[0]+". We'll call you at "+phone+" within one business day"+(svc&&svc!=="Something else"?" about your "+svc.toLowerCase()+" request":"")+".";
      qf.hidden=true;qd.hidden=false;
    });
    $("#quoteReset").addEventListener("click",function(){qf.reset();qd.hidden=true;qf.hidden=false});
  }

  var yr=$("#yr");if(yr)yr.textContent=new Date().getFullYear();

})();
