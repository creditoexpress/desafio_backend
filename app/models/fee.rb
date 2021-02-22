class Fee
  include Mongoid::Document

  field :kind, type: String
  field :rates, type: Hash

  def calculate(value, plots)
    fee = rates[plots.to_s]
    {
      value: value,
      value_with_tax: value_with_tax(value, fee),
      fee: fee,
      plot: plots
    }
  end

  def value_with_tax(value, tax)
    value + (value * tax)
  end
end