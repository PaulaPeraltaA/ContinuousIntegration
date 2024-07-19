const { Membership, Feature, getTotalCost } = require('../src/memberships');

test('calculates total cost correctly', () => {
  const membership = new Membership('Basic', 100, [
    new Feature('Personal Training Session', 30),
    new Feature('Group Classes', 20),
  ]);
  const totalCost = getTotalCost(membership, 3, false, ['Basic', 'Premium', 'Family']);
  expect(totalCost).toBe(135); 
});

test('returns -1 for unavailable membership', () => {
  const membership = new Membership('Gold', 200);
  const totalCost = getTotalCost(membership, 1, false, ['Basic', 'Premium', 'Family']);
  expect(totalCost).toBe(-1);
});
