function StringChallenge(num) {
    let horas = Math.floor(num / 60);
    let minutos = num % 60;
    return horas + ":" + minutos;
}

console.log(StringChallenge(120)); // 2:00