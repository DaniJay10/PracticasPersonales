function StringChallenge(str) { 
    let res = "";
    for(let i=0; i < str.length; i++){
    let letra = str[i];
    if(letra.match(/[a-zA-Z]/)){
      letra = String.fromCharCode(letra.charCodeAt(0) + 1);
      if (letra === '{') letra = 'a';
      if (letra === '[') letra = 'A';
    }
    if(letra.match(/[aeiou]/)) {
      letra = letra.toUpperCase();
    }
    res += letra;
  }
    return res;
  }
     
  // keep this function call here 
  console.log(StringChallenge("fun times!"));
