let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')
nav.style.visibility="hidden";let toggleVisible=function(elem){if(elem.style.visibility==="hidden"){elem.style.visibility="visible";}else{elem.style.visibility="hidden";}};window.addEventListener('load',()=>{let pattern=new RegExp(window.location.pathname,'i')
for(let i=0;i<nav.children.length;i++){console.log(nav.children[i].textContent.match(pattern));if(nav.children[i].textContent.match(pattern)){console.log(nav.children[i]);nav.children[i].classList.add("bg-purple-400 p-2 rounded-md")}}})
ctrl.addEventListener('click',()=>{toggleVisible(nav)})
cls.addEventListener('click',()=>{toggleVisible(nav);});