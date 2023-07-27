let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";ctrl.style.zIndex='3';}else{elem.style.visibility="hidden";}
console.log(elem);};ctrl.addEventListener('click',()=>{toggleVisible(nav)})
cls.addEventListener('click',()=>{const nv2=document.querySelector(".nav");nv2.style.visibility="hidden";});