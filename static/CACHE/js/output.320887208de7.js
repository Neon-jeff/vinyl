let ctrl=document.querySelector('.ctr')
let nav=document.querySelector('.nav')
let cls=document.querySelector('.cls')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}
console.log(elem);};ctrl.addEventListener('click',()=>{let nv=document.querySelector('.nav')
nv.style.visibility="visible";})
cls.addEventListener('click',()=>{let nv=document.querySelector(".nav");nv.style.visibility="hidden";});