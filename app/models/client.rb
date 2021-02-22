class Client
  include Mongoid::Document

  field :name, type: String
  field :document, type: String
  field :phone, type: String
  field :score, type: Integer
  field :negative, type: Boolean
end