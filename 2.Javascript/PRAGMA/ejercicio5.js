function StringChallenge(str) { 
    let res = "";
    let cont = 1;
  
    for (let i = 0; i<str.length; i++){
      if(str[i] === str[i + 1]){
        cont ++;
      }else{
        res += cont + str[i];
        cont = 1;
      }
    }
    return res;
  
  }
     
  // keep this function call here 
  console.log(StringChallenge("aabbcde"));