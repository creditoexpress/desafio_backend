class FeesController < ApplicationController

  def simulate
    if cookies[:client_id].present?
      client = Client.find(cookies[:client_id])
      if client.negative
        fee = Fee.find_by(kind: 'NEGATIVADO')
      elsif client.score < 500
        fee = Fee.find_by(kind: 'SCORE_BAIXO')
      else
        fee = Fee.find_by(kind: 'SCORE_ALTO')
      end
    else
      fee = Fee.find_by(kind: 'SCORE_BAIXO')
    end
    render json: fee.calculate(params[:value], params[:plots]), status: :ok
  end
end
