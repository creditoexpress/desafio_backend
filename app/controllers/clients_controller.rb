class ClientsController < ApplicationController

  def create
    client = Client.create(params)
    return http_error if client.errors.empty?

    render json: client, status: :created
  end

  def identify
    client = Client.where(document: params[:document], phone: params[:phone])
    if client.empty?
      cookies.delete(:client_id)
      render json: { message: 'Cliente não encontrado'}, status: :not_found
    else
      cookies[:client_id] = client.first.id
      render json: client.first, status: :ok
    end
  end
end
