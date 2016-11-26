/**
 * Sum of the first nth term of Series
 * link: https://www.codewars.com/kata/555eded1ad94b00403000071/solutions/javascript
 */
function SeriesSum(n) {
    for (var s = 0, i = 0; i < n; i++) {
        s += 1 / (1 + i * 3);
    }
    return s.toFixed(2);
}

console.log(SeriesSum(5));