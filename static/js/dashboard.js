let Cbtn=document.querySelector('.c-btn')
let Nbtn = document.querySelector(".n-btn")

let CList=document.querySelector('.collected')
let NList=document.querySelector('.nft')

console.log(Cbtn,Nbtn,CList,NList);


Cbtn.addEventListener('click',()=>{
    CList.classList.add('grid')
    CList.classList.remove('hidden')
    NList.classList.remove("grid");
    NList.classList.add("hidden");
    Nbtn.classList.remove('bg-gray-400')
    Nbtn.classList.add("bg-gray-200");
    Cbtn.classList.remove("bg-gray-200");
    Cbtn.classList.add('bg-gray-400')

})

Nbtn.addEventListener("click", () => {
  CList.classList.remove("grid");
  CList.classList.add("hidden");
  NList.classList.add("grid");
  NList.classList.remove("hidden");
    Nbtn.classList.add("bg-gray-400");
    Nbtn.classList.remove("bg-gray-200");
    Cbtn.classList.add("bg-gray-200");
    Cbtn.classList.remove("bg-gray-400");
});


