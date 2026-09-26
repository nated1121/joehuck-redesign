/* Joe Huck Electric — shared page behavior */
(function(){
  var $=function(s,r){return (r||document).querySelector(s)};
  var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};

  /* ---------- Mobile nav ---------- */
  var mb=$(".menu-btn"),nav=$("#nav");
  if(mb&&nav){
    mb.addEventListener("click",function(){var o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o)});
    nav.addEventListener("click",function(e){if(e.target.tagName==="A"){nav.classList.remove("open");mb.setAttribute("aria-expanded","false")}});
  }

  /* ---------- Homepage breaker panel (panels are server-rendered) ---------- */
  var brks=$$(".brk[role=tab]");
  function select(id,focus){
    brks.forEach(function(b){
      var on=b.dataset.id===id;
      b.setAttribute("aria-selected",on);b.tabIndex=on?0:-1;
      var p=document.getElementById(b.getAttribute("aria-controls"));
      if(p){p.hidden=!on;if(on){p.classList.remove("fade-in");void p.offsetWidth;p.classList.add("fade-in")}}
      if(on&&focus)b.focus();
    });
  }
  brks.forEach(function(b,i){
    b.addEventListener("click",function(){select(b.dataset.id)});
    b.addEventListener("keydown",function(e){
      var d={ArrowDown:1,ArrowUp:-1,ArrowRight:1,ArrowLeft:-1}[e.key];
      if(d==null)return;e.preventDefault();
      select(brks[(i+d+brks.length)%brks.length].dataset.id,true);
    });
  });

  /* ---------- "Request a quote" buttons pre-fill the form ---------- */
  document.addEventListener("click",function(e){
    var p=e.target.closest("[data-pick]");if(!p)return;
    $$("#svcChips input").forEach(function(c){if(c.value===p.dataset.pick)c.checked=true});
    var qn=$("#q-note");if(qn&&p.dataset.note&&!qn.value)qn.value=p.dataset.note;
    setTimeout(function(){var n=$("#q-name");n&&n.focus({preventScroll:true})},450);
  });

  /* ---------- Towns: datalist + "do you serve my town?" ---------- */
  var TOWNS=["Yardley","Lower Makefield","Newtown","New Hope","Washington Crossing","Upper Makefield","Levittown","Fairless Hills","Falls Township","Langhorne","Middletown","Morrisville","Bristol","Bensalem","Penndel","Richboro","Holland","Churchville","Southampton","Feasterville","Trevose","Croydon","Tullytown","Doylestown","Warminster","Warrington","Buckingham","Solebury","Lahaska","Furlong","Jamison","Wrightstown","Ivyland","Hulmeville","Langhorne Manor","Northampton","Chalfont","New Britain","Perkasie","Sellersville","Quakertown","Upper Southampton","Lower Southampton","Feasterville-Trevose","Plumstead","Hilltown","West Rockhill","Richland","Milford"];
  var dl=$("#townlist");
  if(dl)TOWNS.forEach(function(t){var o=document.createElement("option");o.value=t;dl.appendChild(o)});
  var af=$("#areaForm");
  if(af){
    var links={};try{links=JSON.parse(af.dataset.links||"{}")}catch(e){}
    var ai=$("#a-town"),ar=$("#areaResult");
    af.addEventListener("submit",function(e){
      e.preventDefault();var v=ai.value.trim();
      if(!v){ar.className="result";ar.textContent="Type a town name first.";return}
      var hit=TOWNS.find(function(t){return t.toLowerCase()===v.toLowerCase()});
      ar.textContent="";
      if(hit){
        ar.className="result yes";
        ar.appendChild(document.createTextNode("✓ Yes, we work in "+hit+". "));
        if(links[hit]){var a=document.createElement("a");a.href=links[hit];a.textContent="See our "+hit+" page";ar.appendChild(a);ar.appendChild(document.createTextNode(" or call 215-906-4634."))}
        else ar.appendChild(document.createTextNode("Request an estimate or call 215-906-4634."));
      }else{ar.className="result maybe";ar.textContent="Call 215-906-4634 and we'll let you know if we can get to "+v+".";}
    });
  }

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
      var svcs=svc?[svc]:$$("input[name=svc]:checked",qf).map(function(c){return c.value});
      $("#doneMsg").textContent="Thanks, "+name.split(" ")[0]+". We'll call you at "+phone+" within one business day"+(svcs.length?" about your "+svcs.join(", ").toLowerCase()+" request":"")+".";
      qf.hidden=true;qd.hidden=false;
    });
    $("#quoteReset").addEventListener("click",function(){qf.reset();qd.hidden=true;qf.hidden=false});
  }

  var yr=$("#yr");if(yr)yr.textContent=new Date().getFullYear();

  /* ---------- Hero ambient: current flowing through wires ---------- */
  var cv=$("#wires"),ctx=cv&&cv.getContext&&cv.getContext("2d");
  var reduce=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
  if(ctx){
    var W,H,paths=[],t=0,dpr=Math.min(window.devicePixelRatio||1,2);
    var build=function(){
      W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
      paths=[];
      for(var i=0;i<7;i++){
        var y=H*(.15+i*.11),pts=[[W*.45,y]],x=W*.45;
        while(x<W+40){x+=60+Math.random()*120;var ny=pts[pts.length-1][1];if(Math.random()<.5){pts.push([x,ny]);ny+=(Math.random()<.5?-1:1)*(20+Math.random()*30);}pts.push([x,ny])}
        paths.push({pts:pts,off:Math.random()*1000,sp:.6+Math.random()*.8});
      }
    };
    var len=function(p){var L=0;for(var i=1;i<p.length;i++)L+=Math.hypot(p[i][0]-p[i-1][0],p[i][1]-p[i-1][1]);return L};
    var at=function(p,d){for(var i=1;i<p.length;i++){var s=Math.hypot(p[i][0]-p[i-1][0],p[i][1]-p[i-1][1]);if(d<=s){var k=d/s;return[p[i-1][0]+(p[i][0]-p[i-1][0])*k,p[i-1][1]+(p[i][1]-p[i-1][1])*k]}d-=s}return p[p.length-1]};
    var draw=function(){
      ctx.clearRect(0,0,W,H);
      paths.forEach(function(w){
        ctx.beginPath();w.pts.forEach(function(p,i){i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1])});
        ctx.strokeStyle="rgba(20,20,20,.07)";ctx.lineWidth=1.2;ctx.stroke();
        var L=w.L||(w.L=len(w.pts)),d=((t*w.sp+w.off)%(L+200))-100;
        for(var k=0;k<18;k++){var q=at(w.pts,Math.max(0,Math.min(L,d-k*4)));ctx.fillStyle="rgba(110,90,50,"+(0.75-k*0.04)+")";ctx.beginPath();ctx.arc(q[0],q[1],k?1.3:2.2,0,7);ctx.fill()}
        var e0=w.pts[0];ctx.fillStyle="rgba(110,90,50,.4)";ctx.fillRect(e0[0]-2,e0[1]-2,4,4);
      });
    };
    build();addEventListener("resize",function(){build();draw()});
    if(reduce){t=300;draw()}else{(function loop(){t+=1.4;draw();requestAnimationFrame(loop)})()}
  }
})();
