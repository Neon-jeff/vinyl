let ctrl=document.querySelector('.ctr')
let nav=document.querySelector('.nav')
let cls=document.querySelector('.cls')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}
console.log(elem);};ctrl.addEventListener('click',()=>{const nv=document.querySelector('.nav')
nv.style.visibility="visible";})
cls.addEventListener('click',()=>{const nv2=document.querySelector(".nav");nv2.style.visibility="hidden";});