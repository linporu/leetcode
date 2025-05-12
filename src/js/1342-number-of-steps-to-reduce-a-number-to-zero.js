/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function (num) {
  let step = 0;

  while (num > 0) {
    if (num % 2 === 0) {
      num = num / 2;
      step++;
    } else {
      num--;
      step++;
    }
  }

  return step;
};
