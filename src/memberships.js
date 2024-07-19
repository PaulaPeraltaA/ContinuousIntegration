class Membership {
    constructor(type, baseCost, features = []) {
      this.type = type;
      this.baseCost = baseCost;
      this.features = features;
    }
  
    calculateTotalCost() {
      let totalCost = this.baseCost;
      for (const feature of this.features) {
        totalCost += feature.cost;
      }
      return totalCost;
    }
  }
  
  class Feature {
    constructor(name, cost) {
      this.name = name;
      this.cost = cost;
    }
  }
  
  function applyGroupDiscount(totalCost, numberOfMembers) {
    if (numberOfMembers >= 2) {
      totalCost *= 0.9;
    }
    return totalCost;
  }
  
  function applySpecialDiscounts(totalCost) {
    if (totalCost > 400) {
      totalCost -= 50;
    } else if (totalCost > 200) {
      totalCost -= 20;
    }
    return totalCost;
  }
  
  function applyPremiumSurcharge(totalCost, isPremium) {
    if (isPremium) {
      totalCost *= 1.15;
    }
    return totalCost;
  }
  
  function validateMembershipAvailability(membership, availableMemberships) {
    if (!availableMemberships.includes(membership.type)) {
      throw new Error("Selected membership plan is not available.");
    }
  }
  
  function getTotalCost(membership, numberOfMembers, isPremium, availableMemberships) {
    try {
      validateMembershipAvailability(membership, availableMemberships);
      let totalCost = membership.calculateTotalCost();
      totalCost = applyGroupDiscount(totalCost, numberOfMembers);
      totalCost = applySpecialDiscounts(totalCost);
      totalCost = applyPremiumSurcharge(totalCost, isPremium);
      return totalCost;
    } catch (error) {
      console.error(error.message);
      return -1;
    }
  }
  
  module.exports = { Membership, Feature, getTotalCost };
  