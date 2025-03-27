function StringChallenge(sen) { 
    const palabras = sen.replace(/[^\w\s]/g, "").split(' ');
    let palabraLarga = "";
    let palabraLargaLongitud = 0;
    for(let i=0; i<palabras.length; i++){
      if(palabras[i].length > palabraLargaLongitud){
        palabraLarga = palabras[i];
        palabraLargaLongitud = palabras[i].length;
      }
    }
    return palabraLarga;
    }
       
    
    console.log(StringChallenge("fun&!! time"));