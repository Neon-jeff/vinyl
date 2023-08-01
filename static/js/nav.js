let ctrl=document.querySelector('.ctr')
let cls=document.querySelector('.cls')
let nav=document.querySelector('.nav')

nav.style.visibility = "hidden";
let toggleVisible = function (elem) {

  if (elem.style.visibility === "hidden") {
    elem.style.visibility = "visible";
  } else {
    elem.style.visibility = "hidden";
  }
};

window.addEventListener('load',()=>{
  let patharr = window.location.pathname.split("/");
  console.log(patharr);
  let path=patharr[patharr.length-1].slice(0,5)
  let pattern=new RegExp(path,'gi')
  for(let i=0;i<nav.children.length;i++){
    if(nav.children[i].textContent.match(pattern)){
      console.log(nav.children[i]);
      nav.children[i].style.backgroundColor = "#c582f2";
      nav.children[i].style.padding = "15px";
      nav.children[i].style.borderRadius = "5px";

    }
  }

})

ctrl.addEventListener('click',()=>{
    toggleVisible(nav)
})
cls.addEventListener('click',()=>{
    toggleVisible(nav);
})


