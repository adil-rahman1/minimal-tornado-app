// https://stackoverflow.com/questions/1484506/random-color-generator
const getRandomColor = () => {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

const changeHeaderBackgroundColor = () => {
    const header = document.getElementById("header")
    const color = getRandomColor()
    header.style.backgroundColor = color
}
