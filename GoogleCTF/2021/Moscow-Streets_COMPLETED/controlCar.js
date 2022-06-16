function controlCar(scanArray) {
  const leftSide = Math.max(...scanArray.slice(0, 7));
  const rightSide = Math.max(...scanArray.slice(10));
  const straight = Math.min(scanArray[7], scanArray[8], scanArray[9]);
  const max = Math.max(straight, rightSide, leftSide);
  return {
    leftSide: -1,
    rightSide: 1,
    straight: 0,
  }[max];
}

