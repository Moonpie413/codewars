/**
 * Multiples of 3 and 5
 * https://www.codewars.com/kata/514b92a657cdc65150000006/train/javascript
 */
function solution(number) {
    for (var s = 0, i = number - 1; i > 2; i--) {
        s = i % 3 === 0 || i % 5 === 0 ? s + i : s;
    } 
    return s;
}

console.log(solution(10));