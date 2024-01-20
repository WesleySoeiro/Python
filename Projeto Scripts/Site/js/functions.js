lastIndex = 0

var img = document.querySelectorAll('.galeria img')

img.forEach((value, index)=>{
  document.querySelectorAll('.bullet')[index]
  .addEventListener('click',()=>{
    let lastImg = document.querySelectorAll('.galeria img')[lastIndex];
    let actualImg = document.querySelectorAll('.galeria img')[index];

    document.querySelectorAll('.bullet')[lastIndex]
    .classList.remove('initial-order');

    document.querySelectorAll('.bullet')[index]
    .classList.add('initial-order');

    lastImg.style.opacity = 0;
    actualImg.style.opacity = 1;

    lastIndex = index 
  })
}

) 