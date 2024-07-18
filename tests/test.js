const suma = require('../src/index');

test('suma 1 + 2 para igualar 3', () => {
  expect(suma(1, 2)).toBe(3);
});
