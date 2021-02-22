Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  resources :clients, only: [:create]
  post 'clients/identify', action: :identify, controller: 'clients'
  post 'fees/simulate', action: :simulate, controller: 'fees'
end
