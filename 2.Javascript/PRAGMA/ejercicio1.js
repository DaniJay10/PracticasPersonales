function RecursionChallenge(num) {
    if (num < 1 || num > 18){
      return "El numero debe estar entre 1 y 18";
    }else{
      if(num == 1){
        return num
      }else{
        return num * RecursionChallenge(num - 1);
      }
    }
}
console.log("Factorial: " + RecursionChallenge(19));