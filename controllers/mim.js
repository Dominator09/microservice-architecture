
var A = [-10001,1,3,6,7,4,8,10009,45,12]
function sortNumber(a,b) {
    return a - b;
}
function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let i=0,least;
    least = A[i];
    A.sort(sortNumber);
    console.log("check1",A,least);
    for(i=0;i<A.length;i+=1){
        if(a[i] > 0){
            least = A[i]
            break;
        }
    }
    console.log("check2",least);
    if(least < 0 || least > 1){
        return 1;
    }
    for(i=0;i<A.length;i+=1){
        if(A[i] > 0 && A[i] == least+1){
            least = A[i]
        }
    }
    console.log("check3",least);
    if(least){
        return least + 1;
    }
    else{
        return 1;
    }
}

console.log(solution(A));