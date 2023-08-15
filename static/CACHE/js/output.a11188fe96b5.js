let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')
let form=document.querySelector('form')
let trans=document.querySelector(".skiptranslate");trans.firstChild().style.display='none'
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}};window.addEventListener('load',()=>{let patharr=window.location.pathname.split("/");let path=patharr[patharr.length-1].slice(0,5)
let pattern=new RegExp(path,'gi')
if(window.location.pathname=="/"){nav.children[1].style.color="#c582f2";}
for(let i=0;i<nav.children.length;i++){if(nav.children[i].textContent.match(pattern)&&window.location.pathname!='/'){nav.children[i].style.color="#c582f2";}}})
ctrl.addEventListener('click',()=>{toggleVisible(nav)})
cls.addEventListener('click',()=>{toggleVisible(nav);});