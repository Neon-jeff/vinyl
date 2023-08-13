let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}};window.addEventListener('load',()=>{console.log(window.location.pathname);console.log(nav.children);})
ctrl.addEventListener('click',()=>{toggleVisible(nav)})
cls.addEventListener('click',()=>{toggleVisible(nav);});