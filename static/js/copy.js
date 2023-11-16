let copy =document.querySelector('.copy')


const clipboard = new ClipboardJS(".btn");
console.log("hi bmena");
clipboard.on('success',(e)=>{
    copy.textContent='Copied!'
    setTimeout(()=>{
       copy.textContent = "Copy";
    },3000)

})
