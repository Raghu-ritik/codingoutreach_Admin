// var blockchapid = document.getElementById('blockchapid');
// var blockcontent = document.getElementById('blockcontent');
// blockchapid.ondragover('mousemove',ev=>{
//     blockcontent.style.backgroundColor= "rgb(168, 109, 32)";
// });

function toggleHide(){
    let btnkuc = document.getElementById('btn-cont');
    let para = document.getElementById('blockcontent');
    if (para.style.display != 'none'){
        para.style.display = 'none';
    }
    else{
        para.style.display = 'block';
    }
}


