function numberToBinary(givenNum, length){
    let ret = []; 
    let num = givenNum;
    while(num !== 0){
        if (num % 2 === 0) 
          ret.push(" ");
        else
          ret.push("#");
        num = parseInt(num / 2);
    }
    while (ret.length < length){
      ret.push(" ");
    }
    return ret.reverse().join("")
}

function solution(n, arr1, arr2) {
    var answer = [];
    for(let i = 0; i<n; i++){
        const num = arr1[i] | arr2[i];
        answer.push(numberToBinary(num, n));
    }
    return answer;
}

function main(){
  const ret1 = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
  const ret2 = solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
  console.log(ret1);
  console.log(ret2);

}

main();
