
const { Membership, Feature, getTotalCost } = require('./memberships');

const availableMemberships = ['Basic', 'Premium', 'Family'];

const basicMembership = new Membership('Basic', 100, [
  new Feature('Personal Training Session', 30),
  new Feature('Group Classes', 20),
]);

const numberOfMembers = 3;
const isPremium = false;

const totalCost = getTotalCost(basicMembership, numberOfMembers, isPremium, availableMemberships);

console.log(`Total cost: ${totalCost}`);
