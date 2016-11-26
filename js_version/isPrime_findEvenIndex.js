/**
 * 寻找素数
 */
function isPrime(num) { 
    num = Math.abs(num);
    if (num === 0 || num === 1) return false;
    for (var i = 2; i < num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

/**
 * 寻找一个数组中左右相加相等的数
 */
function findEvenIndex(arr) {
    if (arr == null || !(arr instanceof Array)) return -1;
    for (var i = 1; i < arr.length - 1; i++) {
        var leftsum = 0, rightsum = 0;
        for (var j = 0; j < i; j++) {
            leftsum = leftsum + arr[j];
        }
        for (var k = i + 1; k < arr.length; k++) {
            rightsum = rightsum + arr[k];
        } 
        if (leftsum === rightsum) return i;
    }
    return -1;
}

function arraySum(arr) {
    return arr.reduce((x, y) => x + y);
}

var arr = new Array(20,10,30,10,10,15,35);
console.log(arraySum([1, 3, 4]));
console.log(findEvenIndex(arr));