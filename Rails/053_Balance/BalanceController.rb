class BalanceController < ApplicationController
  before_action :set_balance, only: [:show, :edit, :update, :destroy]

  # GET /balance
  def index
    @balances = Balance.all
    render json: @balances
  end

  # GET /balance/1
  def show
    render json: @balance
  end

  # POST /balance
  def create
    @balance = Balance.new(balance_params)

    if @balance.save
      render json: @balance, status: :created
    else
      render json: @balance.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /balance/1
  def update
    if @balance.update(balance_params)
      render json: @balance
    else
      render json: @balance.errors, status: :unprocessable_entity
    end
  end

  # DELETE /balance/1
  def destroy
    @balance.destroy
    head :no_content
  end

  private

  def set_balance
    @balance = Balance.find(params[:id])
  end

  def balance_params
    params.require(:balance).permit(:name)
  end
end
