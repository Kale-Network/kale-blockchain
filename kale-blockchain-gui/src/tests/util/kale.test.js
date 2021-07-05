const kale = require("../../util/kale");

describe("kale", () => {
  it("converts number mojo to kale", () => {
    const result = kale.mojo_to_kale(1000000);

    expect(result).toBe(0.000001);
  });
  it("converts string mojo to kale", () => {
    const result = kale.mojo_to_kale("1000000");

    expect(result).toBe(0.000001);
  });
  it("converts number mojo to kale string", () => {
    const result = kale.mojo_to_kale_string(1000000);

    expect(result).toBe("0.000001");
  });
  it("converts string mojo to kale string", () => {
    const result = kale.mojo_to_kale_string("1000000");

    expect(result).toBe("0.000001");
  });
  it("converts number kale to mojo", () => {
    const result = kale.kale_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it("converts string kale to mojo", () => {
    const result = kale.kale_to_mojo("0.000001");

    expect(result).toBe(1000000);
  });
  it("converts number mojo to colouredcoin", () => {
    const result = kale.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it("converts string mojo to colouredcoin", () => {
    const result = kale.mojo_to_colouredcoin("1000000");

    expect(result).toBe(1000);
  });
  it("converts number mojo to colouredcoin string", () => {
    const result = kale.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe("1,000");
  });
  it("converts string mojo to colouredcoin string", () => {
    const result = kale.mojo_to_colouredcoin_string("1000000");

    expect(result).toBe("1,000");
  });
  it("converts number colouredcoin to mojo", () => {
    const result = kale.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it("converts string colouredcoin to mojo", () => {
    const result = kale.colouredcoin_to_mojo("1000");

    expect(result).toBe(1000000);
  });
});
