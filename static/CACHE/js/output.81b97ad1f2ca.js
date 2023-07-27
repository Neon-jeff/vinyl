let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}
console.log(elem);};ctrl.addEventListener('click',()=>{const nv=document.querySelector('.nav')
nv.style.visibility="visible";})
cls.addEventListener('click',()=>{const nv2=document.getElementsByClassName("nav")[0];nv2.style.visibility="hidden";});