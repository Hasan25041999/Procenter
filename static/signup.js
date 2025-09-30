let di1=document.getElementById('shide')
let di2=document.getElementById('lhide')
let btn1=document.getElementById('signup')
let btn2=document.getElementById('next')
btn1.addEventListener('click',()=>{
    if(di1.classList.contains('d-none')){
        di1.classList.remove('d-none')
        di2.classList.add('d-none')
    }

    
})
btn2.addEventListener('click',()=>{
    di1.classList.add('d-none')
    di2.classList.remove('d-none')
})